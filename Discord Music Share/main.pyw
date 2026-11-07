import os
import time
import random
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv, set_key
import pygetwindow as gw # ต้องติดตั้ง pip install pygetwindow
from core.i18n import i18n

# ชื่อไฟล์สำหรับเก็บการตั้งค่า
ENV_FILE = ".env"

def setup_config():
    """Setup Wizard สำหรับตั้งค่าผ่าน CMD"""
    # 1. เลือกภาษาก่อนเป็นอันดับแรก
    print("\n" + i18n.get("select_language"))
    lang_choice = input("Choice (1/2): ")
    selected_lang = "en" if lang_choice == '1' else "th"

    # อัปเดตภาษาใน session และบันทึกลง .env
    i18n.set_language(selected_lang)
    set_key(ENV_FILE, "APP_LANGUAGE", selected_lang)

    print("\n" + i18n.get("setup_title"))
    if os.path.exists(ENV_FILE):
        choice = input(i18n.get("setup_existing_config")).lower()
        if choice != 'y':
            return

    discord_token = input(i18n.get("input_discord_token"))
    spotify_id = input(i18n.get("input_spotify_id"))
    spotify_secret = input(i18n.get("input_spotify_secret"))
    spotify_uri = input(i18n.get("input_spotify_uri"))

    if not os.path.exists(ENV_FILE):
        open(ENV_FILE, 'a').close()

    set_key(ENV_FILE, "DISCORD_TOKEN", discord_token)
    set_key(ENV_FILE, "SPOTIFY_CLIENT_ID", spotify_id)
    set_key(ENV_FILE, "SPOTIFY_CLIENT_SECRET", spotify_secret)
    set_key(ENV_FILE, "SPOTIFY_REDIRECT_URI", spotify_uri)
    print(i18n.get("setup_success"))

def select_mode():
    """ฟังก์ชันเลือกโหมดการทำงาน"""
    print("\n" + i18n.get("mode_selection_title"))
    print(i18n.get("mode_spotify"))
    print(i18n.get("mode_youtube"))
    print(i18n.get("mode_hybrid"))

    while True:
        choice = input(i18n.get("input_mode_choice"))
        if choice in ['1', '2', '3']:
            return choice
        print(i18n.get("error_invalid_mode"))

# --- YouTube Auto-Detect Module ---
def detect_youtube_music():
    """ตรวจจับชื่อเพลงจาก Window Title ของ Browser และกรองเอาเฉพาะเพลงเท่านั้น"""
    try:
        windows = gw.getWindowsWithTitle('YouTube')
        if not windows:
            return None

        window_title = windows[0].title

        if "YouTube" in window_title:
            song_title = window_title.replace(" - YouTube", "").strip()

            # รายการ Keyword ที่กว้างขึ้นเพื่อให้ครอบคลุมเพลงทุกประเภท
            music_keywords = [
                'music', 'song', 'official', 'lyric', 'audio', 'cover',
                'remix', 'playlist', 'lofi', 'mix', 'artist', 'album',
                'mv', 'vocal', 'instrumental', 'karaoke', 'เพลง', 'ดนตรี',
                'studio', 'version', 'edit', 'acoustic', 'bass boosted', 'slowed',
                'chill', 'pop', 'rock', 'hip hop', 'rap', 'jazz', 'classical',
                'electronic', 'edm', 'trap', 'r&b', 'blues', 'country', 'reggae', 'metal', 'punk', 'folk', 'indie', 'alternative', 'soundtrack', 'OST', 'theme', 'score', 'symphony', 'orchestra', 'choir', 'opera', 'ballad', 'anthem', 'serenade', 'concerto', 'sonata', 'suite', 'aria',
                'Cover', 'remix', 'mashup', 'medley', 'tribute', 'live', 'session', 'demo', 'bootleg', 'unplugged', 'acapella', 'karaoke', 'instrumental', 'orchestral', 'symphonic', 'choral', 'vocalist', 'band', 'ensemble', 'quartet', 'trio', 'duet'
            ]

            # ตรวจสอบว่าในชื่อวิดีโอมี Keyword ของเพลงอย่างน้อย 1 คำหรือไม่
            is_music = any(keyword in song_title.lower() for keyword in music_keywords)

            if is_music:
                return f"🎧 Music: {song_title}"
            else:
                # ถ้าไม่มี Keyword เพลงเลย ให้คืนค่า None (เพื่อให้ระบบขึ้น Idle)
                return None

    except Exception as e:
        print(f"Window Detection Error: {e}")
    return None

# --- Spotify Module ---
def get_spotify_track(sp):
    try:
        track = sp.current_user_playing_track()
        if track and track['is_playing']:
            song_name = track['item']['name']
            artist_name = track['item']['artists'][0]['name']
            return f"🎧 Spotify: {song_name} - {artist_name}"
    except Exception as e:
        print(f"Spotify Error: {e}")
    return None

# --- Discord Module ---
def update_discord_status(token, text=None):
    url = "https://discord.com/api/v9/users/@me/settings"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    # ถ้า text เป็น None ให้ส่งค่าว่างเพื่อลบ Custom Status
    payload = {"custom_status": {"text": text if text else ""}}

    try:
        response = requests.patch(url, json=payload, headers=headers)
        return response.status_code == 200
    except:
        return False

def main():
    setup_config()
    load_dotenv()

    token = os.getenv("DISCORD_TOKEN")
    mode = select_mode()

    try:
        sp = None
        if mode in ['1', '3']:
            sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                client_id=os.getenv("SPOTIFY_CLIENT_ID"),
                client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
                redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
                scope="user-read-currently-playing"
            ))

        mode_name = 'Spotify' if mode=='1' else 'YouTube Auto' if mode=='2' else 'Hybrid'
        print(i18n.get("app_starting", mode_name))
        print(i18n.get("app_waiting"))

        while True:
            status_text = None

            if mode == '1': # Spotify Only
                status_text = get_spotify_track(sp)

            elif mode == '2': # YouTube Auto-Detect
                status_text = detect_youtube_music()

            elif mode == '3': # Hybrid
                status_text = get_spotify_track(sp)
                if not status_text:
                    status_text = detect_youtube_music()

            if not status_text:
                # ถ้าไม่มีเพลง ให้ส่งค่า None เพื่อลบ status
                status_text = None

            if update_discord_status(token, status_text):
                if status_text:
                    print(f"[{time.strftime('%H:%M:%S')}] {i18n.get('status_updated', status_text)}")
                else:
                    print(f"[{time.strftime('%H:%M:%S')}] {i18n.get('status_cleared')}")
            else:
                print(i18n.get("update_failed"))

            time.sleep(random.randint(30, 60))

    except KeyboardInterrupt:
        print(i18n.get("user_stop"))
    except Exception as e:
        print(i18n.get("critical_error", str(e)))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Critical Error: {e}")
    finally:
        input(i18n.get("exit_prompt"))

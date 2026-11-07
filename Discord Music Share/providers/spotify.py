import spotipy
from spotipy.oauth2 import SpotifyOAuth
from providers.base import MusicProvider, MusicTrack
import config

class SpotifyProvider(MusicProvider):
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=config.SPOTIPY_CLIENT_ID,
            client_secret=config.SPOTIPY_CLIENT_SECRET,
            redirect_uri=config.SPOTIPY_REDIRECT_URI,
            scope="user-read-currently-playing"
        ))

    def get_current_track(self):
        try:
            track_info = self.sp.current_user_playing_track()
            if not track_info or not track_info['is_playing']:
                return None

            item = track_info['item']
            return MusicTrack(
                title=item['name'],
                artist=", ".join([artist['name'] for artist in item['artists']]),
                duration_ms=item['duration_ms'],
                album_art_url=item['album']['images'][0]['url'] if item['album']['images'] else None
            )
        except Exception as e:
            print(f"Spotify Error: {e}")
            return None

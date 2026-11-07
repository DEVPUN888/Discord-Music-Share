## 🇺🇸 English

A lightweight system to share your current music from YouTube and Spotify to your Discord Custom Status using a User Token, optimized for minimal RAM and CPU usage.

### ✨ Features
- **Multi-Source Support:** Fetches music via Spotify Web API and detects YouTube music via Window Title (No API Key required).
- **Operation Modes:**
    - `Spotify Only`: Focuses exclusively on Spotify.
    - `YouTube Auto`: Automatically detects YouTube windows and filters for music content.
    - `Hybrid`: Priority order: Spotify $\rightarrow$ YouTube $\rightarrow$ Clear Status.
- **Resource Optimized:** Runs in background (`.pyw`), utilizes Lazy Loading, and features a Wake-up Condition.
- **Safety First:** Includes Anti-Ban Jitter (randomized delays) and User-Agent Masking to minimize ban risks.
- **Multi-language Support:** Available in both Thai and English.

### 🚀 Installation & Usage
1. **Install Required Libraries:**
   ```bash
   pip install pygetwindow requests python-dotenv spotipy
   ```
2. **Run the Application:**
   ```bash
   python main.pyw
   ```
3. **First-time Setup:**
   - The program will launch the **Setup Wizard**. Select your preferred language and enter:
     - Discord User Token
     - Spotify Client ID / Secret / Redirect URI
4. **Start Sharing:** Keep YouTube/Spotify and Discord open. The system will automatically update your status.

---

## ⚠️ Security Warning / คำเตือนด้านความปลอดภัย
- **User Token:** This app uses a User Token. To avoid being flagged by Discord, the app uses randomized polling intervals (Jitter). Please use it responsibly.
- **User Token:** โปรแกรมนี้ใช้ User Token เพื่อความปลอดภัยจึงมีการใช้ระบบสุ่มเวลาหน่วง (Jitter) โปรดใช้งานอย่างระมัดระวัง

## 🛠️ Technical Specs / รายละเอียดทางเทคนิค
- **Language:** Python 3.x
- **Key Libraries:** `requests`, `spotipy`, `pygetwindow`, `python-dotenv`

## By DevPUN

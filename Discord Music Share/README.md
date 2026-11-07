# 🎵 Discord Music Presence Share (Ultra-Lightweight)

A lightweight Python application that shares your current music from **Spotify** and **YouTube** to your **Discord Custom Status**.

---

## 🇹🇭 ภาษาไทย

ระบบแชร์เพลงจาก YouTube และ Spotify ไปยังสถานะ (Custom Status) ของ Discord โดยใช้ User Token และเน้นการใช้ทรัพยากรเครื่อง (RAM/CPU) ให้ต่ำที่สุด

### ✨ คุณสมบัติ
- **รองรับหลายแหล่งข้อมูล:** ดึงเพลงจาก Spotify Web API และตรวจจับ YouTube จาก Window Title (ไม่ต้องใช้ API Key)
- **โหมดการทำงาน:**
    - `Spotify Only`: เน้นดึงเพลงจาก Spotify เท่านั้น
    - `YouTube Auto`: ตรวจจับหน้าต่าง YouTube และกรองเฉพาะวิดีโอที่เป็นเพลง
    - `Hybrid`: ลำดับความสำคัญ Spotify $\rightarrow$ YouTube $\rightarrow$ Clear Status
- **ประหยัดทรัพยากร:** รันแบบ Background (`.pyw`), ใช้ Lazy Loading และมีระบบ Wake-up Condition
- **ปลอดภัย:** มีระบบ Anti-Ban Jitter (สุ่มเวลาหน่วง) และ User-Agent Masking เพื่อลดความเสี่ยงในการถูกแบน
- **รองรับ 2 ภาษา:** สามารถเลือกใช้งานได้ทั้งภาษาไทยและภาษาอังกฤษ

### 🚀 วิธีการติดตั้งและใช้งาน
1. **ติดตั้ง Libraries ที่จำเป็น:**
   ```bash
   pip install pygetwindow requests python-dotenv spotipy
   ```
2. **รันโปรแกรม:**
   ```bash
   python main.pyw
   ```
3. **การตั้งค่าครั้งแรก:**
   - โปรแกรมจะเข้าสู่ **Setup Wizard** ให้คุณเลือกภาษาและกรอกข้อมูล:
     - Discord User Token
     - Spotify Client ID / Secret / Redirect URI
4. **เริ่มใช้งาน:** เปิด YouTube หรือ Spotify และ Discord ทิ้งไว้ ระบบจะอัปเดตสถานะให้โดยอัตโนมัติ

---

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

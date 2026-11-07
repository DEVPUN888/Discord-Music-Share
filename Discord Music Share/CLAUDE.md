# Project: Discord Music Presence Share (Ultra-Lightweight)

ระบบแชร์เพลงจาก YouTube และ Spotify ไปยังสถานะ (Custom Status) ของ Discord โดยใช้ User Token และเน้นการใช้ทรัพยากรเครื่อง (RAM/CPU) ให้ต่ำที่สุด

## 📌 สถานะปัจจุบัน (Current Progress)
- [x] **สถาปัตยกรรมระบบ:** ออกแบบเป็น Modular (Spotify $\rightarrow$ YouTube $\rightarrow$ Discord)
- [x] **การตั้งค่า:** ระบบ Setup Wizard ผ่าน CMD บันทึกค่าลง `.env`
- [x] **การเชื่อมต่อ API:**
    - [x] Spotify Web API (ดึงเพลงปัจจุบัน)
    - [x] YouTube Auto-Detection (ตรวจจับจาก Window Title - ไม่ใช้ API Key)
    - [x] Discord User API (อัปเดต Custom Status)
- [x] **ระบบกรองเพลง (Music Filter):** กรองเฉพาะวิดีโอที่มี Keyword เกี่ยวกับเพลงเท่านั้น
- [x] **การจัดการทรัพยากร (Optimization):**
    - [x] Lazy Loading สำหรับ Spotify Client
    - [x] รันแบบ Background ด้วยนามสกุล `.pyw`
    - [x] ระบบ Wake-up Condition (ทำงานเมื่อเปิด Discord และเพลงเท่านั้น)
    - [x] Anti-Ban Jitter (สุ่มเวลาหน่วง 60-120 วินาที)
- [x] **การลบสถานะ:** ลบ Custom Status ทันทีเมื่อไม่มีการเล่นเพลง

## 🛠️ รายละเอียดทางเทคนิค (Technical Specs)

### Libraries ที่ใช้
- `requests`: สำหรับส่งคำขอไปยัง Discord API
- `spotipy`: สำหรับเชื่อมต่อ Spotify API
- `pygetwindow`: สำหรับตรวจจับหน้าต่าง Browser (YouTube)
- `python-dotenv`: สำหรับจัดการ Environment Variables

### โหมดการทำงาน
1. **Spotify Only:** ดึงเพลงอัตโนมัติจาก Spotify
2. **YouTube Auto:** ตรวจจับชื่อหน้าต่าง YouTube และกรองเอาเฉพาะเพลง
3. **Hybrid:** ลำดับความสำคัญ Spotify $\rightarrow$ YouTube $\rightarrow$ Clear Status

## ⚠️ คำเตือนด้านความปลอดภัย
- **User Token:** โปรแกรมนี้ใช้ User Token ซึ่งมีความเสี่ยงต่อการถูกแบนหากส่งคำขอถี่เกินไป จึงมีการใช้ระบบ Jitter และ User-Agent Masking
- **Privacy:** การใช้ `pygetwindow` จะอ่านเฉพาะชื่อหัวข้อหน้าต่าง (Window Title) เท่านั้น ไม่มีการบันทึกข้อมูลส่วนตัว

## 🚀 วิธีการติดตั้งและรัน
1. ติดตั้ง Library: `pip install pygetwindow requests python-dotenv spotipy`
2. รันไฟล์: `python main.pyw` (หรือดับเบิลคลิกไฟล์)
3. ตั้งค่าผ่าน CMD ในการรันครั้งแรก
4. เปิด YouTube/Spotify และ Discord ทิ้งไว้

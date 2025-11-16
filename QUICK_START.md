# 🚀 CineTune - Quick Start Guide

## ⚡ 5 Menit Setup

### 1️⃣ Install Dependencies (1-2 menit)
```bash
cd d:\Programming\SEMESTER_6\CineTune
pip install -r requirements.txt
```

### 2️⃣ Jalankan Aplikasi (30 detik)
```bash
python src/main.py
```

### 3️⃣ Mulai Bermain! 🎮

---

## 🎮 Cara Bermain

### **Gesture Controls:**
```
👍 Thumb Up (Jempol naik)     = Jawaban A
✋ Open Palm (Tangan terbuka)  = Jawaban B  
✌️ Two Fingers (V/Victory)    = Jawaban C
✊ Fist (Genggaman tangan)     = Jawaban D
```

### **Game Steps:**
1. **Menu** → Klik "MULAI GAME"
2. **Game Screen** → Lihat gambar film, tunjukkan gesture
3. **Result Screen** → Lihat apakah benar/salah
4. **Repeat** → Sampai 8 soal selesai
5. **Score** → Lihat hasil akhir Anda

---

## ⌨️ Keyboard Shortcuts (Testing)

Jika gesture tidak terdeteksi, bisa manual:
- **A** = Jawaban A
- **B** = Jawaban B
- **C** = Jawaban C
- **D** = Jawaban D
- **ESC** = Keluar game
- **SPACE** = Continue dari result

---

## 🐛 Troubleshooting

### ❌ "No module named cv2/pygame/mediapipe"
```bash
pip install --upgrade opencv-python pygame mediapipe
```

### ❌ "Camera tidak terdeteksi"
- Pastikan kamera terhubung & aktif
- Cek permission aplikasi
- Restart aplikasi

### ❌ "Gesture tidak terdeteksi"
- Pastikan pencahayaan cukup (di depan lampu/jendela)
- Posisikan tangan di tengah-tengah screen
- Tunjukkan gesture dengan jelas (hold 0.5 detik)

### ❌ "Audio tidak terdengar"
- Cek volume sistem
- Pastikan speaker/headphone connected
- Coba restart aplikasi

---

## 📊 Test Komponen (Optional)

Sebelum bermain, bisa test semua komponen:
```bash
python test_components.py
```

Output:
```
TEST 1: Imports        ✓ PASS
TEST 2: Data Loader    ✓ PASS
TEST 3: Game Manager   ✓ PASS
TEST 4: Gesture        ✓ PASS
TEST 5: Audio          ✓ PASS
TEST 6: UI/Pygame      ✓ PASS
────────────────────────────
Total: 5/5 PASSED ✓
```

---

## 📁 File Structure

```
CineTune/
├── src/
│   ├── main.py              # ← Run this!
│   ├── core/
│   ├── ui/
│   └── vision/
├── data/
│   ├── questions.csv
│   └── gestures.csv
├── assets/
│   ├── images/  (8 film posters)
│   └── audio/   (8 sound files)
└── requirements.txt         # Dependencies
```

---

## 💡 Tips & Tricks

### ✅ Gesture Recognition Tips
1. **Good Lighting** - Stand near window or lamp
2. **Clear Gesture** - Show hand clearly to camera
3. **Stable Hand** - Hold gesture for 0.5 second
4. **Camera Distance** - 30-60cm from camera

### 📸 Test Gesture First
```bash
# Run gesture test (optional)
cd src
python vision/gesture_detector.py
```

### 🔧 Customize Game
- Edit `data/questions.csv` untuk tambah pertanyaan baru
- Edit `src/ui/tampilan.py` untuk ubah warna/font
- Edit `src/vision/gesture_mapper.py` untuk ubah gesture sensitivity

---

## 🎯 Game Modes

### Mode 1: Normal (Current)
- 8 pertanyaan film
- Gesture detection
- Score tracking

### Mode 2: Debug (Keyboard)
- Tekan A/B/C/D untuk manual answer
- Cocok untuk testing tanpa gesture

### Mode 3: Full Screen (Future)
- Dapat di-enable di `main.py`

---

## 🎓 Project Info

**For Assignment:** Sistem Teknologi Multimedia (IF25-40305)  
**Team Members:**
- Sulthan Fatih Pradewa (122140183)
- Muhammad Fauzi Azizi (122140106)
- Ihya Razky Hidayat (122140167)

**Tech Stack:**
- Python 3.11
- Pygame (UI)
- MediaPipe (Gesture)
- OpenCV (Vision)

---

## 📞 Getting Help

1. **Error during installation?**
   - Check: `pip install --upgrade pip`
   - Then: `pip install -r requirements.txt`

2. **Gesture not working?**
   - Check lighting
   - Try keyboard shortcut (A/B/C/D)
   - Restart camera (if available)

3. **Need detailed documentation?**
   - Read: `DEVELOPER_GUIDE.md`
   - Read: `UI_DOCUMENTATION.md`
   - Read: `PROJECT_STRUCTURE.md`

---

## ✨ Quick Reference

| Action | Command |
|--------|---------|
| Run app | `python src/main.py` |
| Test components | `python test_components.py` |
| Install deps | `pip install -r requirements.txt` |
| Add questions | Edit `data/questions.csv` |
| Change colors | Edit `src/ui/tampilan.py` |
| Exit game | Press ESC |

---

## 🎬 Expected Output

When you run `python src/main.py`, you should see:

```
==================================================
  CineTune - Tebak Film Lewat Gesture
==================================================

[INIT] Loading data...
[INIT] Loaded 8 questions
[INIT] Gesture map: {'Thumb_Up': 'A', ...}
[INIT] Initializing gesture detection...
[INIT] CineTune initialized successfully!

[Pygame window opens with MENU screen]
```

---

## 🏆 Game Tips

### To Win:
1. ✅ Get good lighting
2. ✅ Know the films (it helps!)
3. ✅ Show gesture clearly
4. ✅ Hold gesture for 0.5 seconds
5. ✅ Answer all 8 questions

### Scoring:
- Correct answer = +1 point
- Wrong answer = +0 point
- **Goal:** Get 100% (8/8 correct) 🏆

---

**Ready to play? Run: `python src/main.py`**

🎮 Have fun! 🎬

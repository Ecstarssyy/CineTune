# 🎬 CineTune - PANDUAN LENGKAP MEMULAI

## 🚀 ADA 2 CARA UNTUK MEMULAI:

---

## **CARA 1: LANGSUNG MAIN (Paling Cepat) ⚡**

### **Hanya 1 Command!**

Buka PowerShell di folder project, kemudian ketik:

```powershell
python src/main.py
```

**Itu saja! Game akan langsung mulai.**

---

## **CARA 2: VERIFIKASI DULU SEBELUM MAIN (Aman) 🔧**

Jika ingin memastikan semua komponen siap:

### **Step 1: Test Semua Komponen**
```powershell
python test_components.py
```

**Tunggu sampai selesai. Anda akan melihat:**
```
================== SUMMARY ==================
[PASS] Data Loader
[PASS] Game Manager
[PASS] Gesture Detection
[PASS] Audio Player
[PASS] UI/Pygame

Total: 5/5 passed
✓ All tests passed! Ready to run: python src/main.py
```

### **Step 2: Jalankan Game**
```powershell
python src/main.py
```

---

## 📋 CHECKLIST SEBELUM MAIN

Sebelum jalankan, pastikan:

- [ ] Python 3.8+ terinstall (`python --version`)
- [ ] Kamera tersedia & berfungsi
- [ ] Pencahayaan cukup terang
- [ ] Speaker/Headphone terhubung (optional, untuk audio)
- [ ] Folder project sudah di `d:\Programming\SEMESTER_6\CineTune`

---

## 🖥️ LAYAR YANG AKAN MUNCUL

### **Layar 1: Menu Awal**
```
┌─────────────────────────────────────┐
│                                     │
│         CineTune (Kuning)           │
│   Tebak Film Lewat Gesture          │
│                                     │
│       [  MULAI GAME  ]              │
│                                     │
│  Instruksi:                         │
│  👍 Thumb Up = A                   │
│  ✋ Open Palm = B                  │
│  ✌️ Two Fingers = C                 │
│  ✊ Fist = D                        │
│                                     │
└─────────────────────────────────────┘

➜ Klik Tombol MULAI GAME
```

### **Layar 2: Game (Soal 1-8)**
```
┌──────────────────────────────────────────┐
│ Soal 1/8                  ████░░░░░░░ 12% │
├──────────────────────────────────────────┤
│                                          │
│  ┌────────────┐      ┌──────────────┐   │
│  │            │      │ [A] Jumbo    │   │
│  │   POSTER   │      │ [B] Adit     │   │
│  │   FILM     │      │ [C] Syifa    │   │
│  │            │      │ [D] Pragos   │   │
│  └────────────┘      └──────────────┘   │
│                                          │
│  Gesture Terdeteksi: Thumb Up           │
│                                          │
└──────────────────────────────────────────┘

➜ Tunjukkan gesture & tahan 0.5 detik
```

### **Layar 3: Hasil Jawaban**
```
┌──────────────────────────────────────┐
│                                      │
│          ✓ BENAR!                    │
│      (atau ✗ SALAH!)                │
│                                      │
│      Jawaban Benar: JUMBO            │
│                                      │
│         [  LANJUT  ]                 │
│                                      │
│  Atau otomatis lanjut dalam 2 detik  │
│                                      │
└──────────────────────────────────────┘

➜ Klik LANJUT atau tunggu 2 detik
```

### **Layar 4: Game Over (Akhir)**
```
┌──────────────────────────────────────┐
│                                      │
│       GAME SELESAI                   │
│                                      │
│    Skor: 7/8 (87.5%)                │
│                                      │
│    Luar Biasa! 🌟                   │
│    (atau Bagus! / Coba Lagi!)       │
│                                      │
│    [ KEMBALI KE MENU ]              │
│                                      │
└──────────────────────────────────────┘

➜ Klik untuk kembali ke Menu atau ESC untuk keluar
```

---

## 🎮 GAMEPLAY MECHANICS

### **Gesture Recognition:**

Setiap gesture harus:
1. ✅ **Terlihat jelas** di kamera
2. ✅ **Dipegang stabil** selama ~0.5 detik
3. ✅ **Gesture lengkap** (semua jari terlihat dengan jelas)

### **Gesture Mapping:**

```
Input Gesture              → Jawaban
─────────────────────────────────────
👍 Jempol naik tertinggi     → A
✋ Semua jari terbuka        → B  
✌️ Telunjuk + tengah naik    → C
✊ Semua jari menutup        → D
```

### **Score System:**

- ✅ Benar = +1 poin
- ❌ Salah = +0 poin
- **Goal:** Dapat 100% (8/8 benar) = 🏆

---

## 📸 SETUP KAMERA

### **Posisi Ideal:**

```
Monitor/Screen
     ║
┌────╨────────────────┐
│ ┌──────────────────┐│
│ │  [Kamera Area]  ││
│ │  ┌────────────┐ ││
│ │  │  YOUR HAND │ ││
│ │  │  30-60cm   │ ││
│ │  │  dari kamera││
│ │  └────────────┘ ││
│ └──────────────────┘│
└────────────────────┘

✓ Tangan di depan kamera
✓ Pencahayaan dari depan (lampu/jendela)
✓ Jangan ada cahaya dari belakang
```

### **Pencahayaan Optimal:**

- ✅ **BAIK:** Depan jendela, cahaya alami/lampu
- ❌ **BURUK:** Ruangan gelap, cahaya dari belakang
- ❌ **BURUK:** Silhouette (terlalu terang di belakang)

---

## ⌨️ KEYBOARD SHORTCUTS

Jika gesture tidak terdeteksi, bisa gunakan keyboard:

| Tombol | Action |
|--------|--------|
| **A** | Pilih jawaban A |
| **B** | Pilih jawaban B |
| **C** | Pilih jawaban C |
| **D** | Pilih jawaban D |
| **SPACE** | Lanjut dari result screen |
| **ESC** | Keluar dari game |

---

## 🐛 TROUBLESHOOTING

### ❌ "Gesture tidak terdeteksi"

**Solusi:**
1. ✓ Cek pencahayaan (harus terang)
2. ✓ Tunjukkan gesture dengan jelas
3. ✓ Tahan gesture lebih lama (coba 1-2 detik)
4. ✓ Posisikan tangan di tengah-tengah area kamera
5. ✓ Gunakan keyboard (A/B/C/D) sebagai backup

### ❌ "Kamera tidak menyala"

**Solusi:**
1. ✓ Periksa apakah app lain membuka kamera
2. ✓ Tutup app lain yang pakai kamera (zoom, skype, dll)
3. ✓ Restart aplikasi CineTune
4. ✓ Periksa Windows permission untuk kamera

### ❌ "Audio/Sound tidak terdengar"

**Solusi:**
1. ✓ Cek volume Windows (bottom right)
2. ✓ Pastikan speaker/headphone terhubung
3. ✓ Test speaker di aplikasi lain
4. ✓ Ini opsional, game tetap jalan tanpa audio

### ❌ "Error/Crash saat jalankan"

**Solusi:**
1. ✓ Lihat pesan error di console
2. ✓ Pastikan Python 3.8+
3. ✓ Reinstall dependencies: `pip install -r requirements.txt`
4. ✓ Baca QUICK_START.md

---

## 🎓 TIPS UNTUK SUKSES

### **Sebelum Main:**
- 🔦 Siapkan pencahayaan yang baik
- 📹 Test kamera (bisa pake Zoom/Skype)
- 🎮 Pastikan sudah tahu 4 gesture (A/B/C/D)

### **Saat Main:**
- 👁️ Lihat monitor/layar untuk feedback gesture
- ✋ Tunjukkan gesture dengan ekspresif
- ⏱️ Tahan gesture minimal 0.5 detik
- 🎯 Pikir jawaban sebelum tunjukkan gesture

### **Saat Gesture Tidak Deteksi:**
- 🔄 Coba lagi dari awal
- ⌨️ Gunakan keyboard (A/B/C/D) sebagai backup
- 💡 Improve pencahayaan
- 🖐️ Buat gesture lebih jelas

---

## 📊 SCORING GUIDE

Setelah game selesai, Anda akan lihat score:

```
Skor Anda    →    Pesan Motivasi
─────────────────────────────────
8/8 (100%)    →   Sempurna! 🏆
7/8 (87.5%)   →   Luar Biasa! 🌟
6/8 (75%)     →   Bagus! 👍
5/8 (62.5%)   →   Cukup baik 😊
< 5 (< 62%)   →   Coba lagi! 💪
```

---

## 🔄 FLOW DIAGRAM

```
START
  ↓
  python src/main.py
  ↓
┌─ MENU SCREEN ─────────────┐
│ Tunggu klik MULAI GAME   │
└────────┬──────────────────┘
         │
         ↓
┌─ KAMERA INITIALIZE ───────┐
│ Tunggu 2-3 detik          │
└────────┬──────────────────┘
         │
         ↓
┌─ GAME SCREEN ─────────────┐
│ LOOP 8x (soal 1-8):       │
│ 1. Tampil gambar & opsi   │
│ 2. Tunggu gesture         │
│ 3. Process & validate     │
│ 4. Show result            │
│ 5. Increment counter      │
└────────┬──────────────────┘
         │
         ↓
    Counter = 8?
         │
    No  → Back ke GAME SCREEN
    Yes → 
         ↓
┌─ GAME OVER SCREEN ────────┐
│ Tampil final score        │
│ Tunggu klik BACK TO MENU  │
└────────┬──────────────────┘
         │
         ↓
Kembali ke MENU atau EXIT?
         │
    MENU → Ulang dari MENU SCREEN
    EXIT → Close window
         ↓
       END
```

---

## 📚 DOKUMENTASI LENGKAP

Jika ingin tahu lebih detail:

| File | Untuk Apa | Waktu Baca |
|------|-----------|-----------|
| `HOW_TO_START.md` | Panduan ini (setup & main) | 5 min |
| `QUICK_START.md` | Quick reference | 2 min |
| `DEVELOPER_GUIDE.md` | Untuk develop/modify | 10 min |
| `UI_DOCUMENTATION.md` | Detail UI/UX | 15 min |
| `PROJECT_STRUCTURE.md` | Architecture | 10 min |

---

## ✨ SIAP?

### **3 Simple Steps:**

1️⃣ Buka PowerShell di folder project
```
cd d:\Programming\SEMESTER_6\CineTune
```

2️⃣ (Optional) Verify setup
```
python test_components.py
```

3️⃣ **MAIN!**
```
python src/main.py
```

---

## 🎬 SELAMAT BERMAIN! 🎮

**Anda siap untuk:**
- ✅ Menjalankan aplikasi
- ✅ Mainkan 8 soal film
- ✅ Gunakan gesture recognition
- ✅ Lihat score final

**Enjoy & Dapatkan Score 100%! 🏆**

---

**Questions? Baca dokumentasi atau coba keyboard shortcut (A/B/C/D) sebagai backup.**

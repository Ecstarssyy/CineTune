# 🎮 CineTune - CARA MEMULAI (Step-by-Step)

## ⚡ 3 Langkah Mudah untuk Main Game

---

## 📋 LANGKAH 1: Persiapan (1 Menit)

### A. Buka PowerShell/Command Prompt
```
Tekan: Windows Key + R
Ketik: powershell
Tekan: Enter
```

### B. Navigasi ke folder project
```powershell
cd d:\Programming\SEMESTER_6\CineTune
```

Atau copy & paste di PowerShell:
```powershell
Set-Location "d:\Programming\SEMESTER_6\CineTune"
```

**Verifikasi:** Seharusnya Anda melihat:
```
D:\Programming\SEMESTER_6\CineTune>
```

---

## 🔧 LANGKAH 2: Verifikasi Setup (30 Detik)

### Cek apakah dependencies sudah install
```powershell
python -m pip list | findstr pygame
```

**Output yang benar:**
```
pygame                2.6.1
```

### Cek MediaPipe
```powershell
python -c "import mediapipe; print('MediaPipe OK')"
```

**Output yang benar:**
```
MediaPipe OK
```

---

## 🎮 LANGKAH 3: JALANKAN GAME! (30 Detik)

### Command untuk main:
```powershell
python src/main.py
```

### Yang akan terjadi:
1. ✅ Console menampilkan pesan startup
2. ✅ Pygame window terbuka (1280x720)
3. ✅ Menu screen muncul dengan judul "CineTune"
4. ✅ Tombol "MULAI GAME" siap diklik

---

## 🎬 LANGKAH 4: MAIN GAME (5-10 Menit)

### Setelah window terbuka:

#### **Step A: Menu Screen**
```
Anda akan melihat:
├─ Judul: CineTune (besar, kuning)
├─ Subtitle: Tebak Film Lewat Gesture
├─ Tombol: MULAI GAME (biru)
└─ Instructions: Gesture mapping (A/B/C/D)
```

**Action:** Klik tombol "MULAI GAME"

#### **Step B: Siapkan Kamera**
```
Game akan mencoba membuka kamera Anda
- Pastikan kamera LED menyala
- Pastikan pencahayaan cukup (depan lampu/jendela)
- Tunggu 2-3 detik untuk inisialisasi
```

#### **Step C: Game Screen Pertama**
```
Anda akan melihat:
├─ Bagian kiri: Poster film
├─ Bagian kanan: 4 pilihan (A, B, C, D)
├─ Atas: Progress bar (Soal 1/8)
└─ Bawah: "Posisikan tangan di depan kamera..."
```

**Action:** Tunjukkan tangan Anda ke kamera

#### **Step D: Pilih Jawaban dengan Gesture**
```
Gesture yang dikenali:

👍 THUMB UP (Jempol naik)     = Jawaban A
✋ OPEN PALM (Tangan terbuka)  = Jawaban B
✌️ TWO FINGERS (V gesture)    = Jawaban C
✊ FIST (Genggaman tertutup)   = Jawaban D
```

**Tips:**
- Tunjukkan gesture dengan JELAS
- TAHAN gesture selama **0.5 detik** (½ detik)
- Pastikan tangan terlihat di monitor/webcam

#### **Step E: Lihat Hasilnya**
```
Setelah gesture terdeteksi:
├─ Screen berubah ke RESULT SCREEN
├─ Tampil: ✓ BENAR! atau ✗ SALAH!
├─ Tampil: Jawaban yang benar
├─ Tombol: LANJUT
└─ atau Auto-continue dalam 2 detik
```

#### **Step F: Lanjut ke Soal Berikutnya**
```
Soal 2/8, 3/8, ... sampai 8/8
Proses repeat untuk semua pertanyaan
```

#### **Step G: Lihat Score Final**
```
Setelah soal ke-8 selesai:
├─ GAME OVER SCREEN muncul
├─ Tampil: Total Score (X/8)
├─ Tampil: Persentase (Y%)
├─ Tampil: Pesan motivasi
│  ├─ Jika 80%+: "Luar Biasa! 🌟"
│  ├─ Jika 60-80%: "Bagus! 👍"
│  └─ Jika <60%: "Coba lagi! 💪"
└─ Tombol: KEMBALI KE MENU
```

---

## ⌨️ TOMBOL TAMBAHAN (Optional)

Selama bermain, Anda bisa gunakan:

| Tombol | Fungsi |
|--------|--------|
| **A** | Submit jawaban A (tanpa gesture) |
| **B** | Submit jawaban B (tanpa gesture) |
| **C** | Submit jawaban C (tanpa gesture) |
| **D** | Submit jawaban D (tanpa gesture) |
| **SPACE** | Lanjut dari result screen |
| **ESC** | Keluar dari game |

---

## 🎥 TIPS GESTURE RECOGNITION

### ✅ Untuk Deteksi Bagus:
1. **Pencahayaan**: Pastikan cukup terang
   - Ideal: Depan jendela atau lampu
   - Jangan: Cahaya dari belakang

2. **Posisi Tangan**: Letakkan di depan kamera
   - Tinggi: Di level mata
   - Jarak: 30-60cm dari kamera

3. **Gesture Jelas**: Tunjukkan dengan jelas
   - Pastikan semua jari terlihat
   - Jangan gerakkan tangan terlalu cepat

4. **Hold Time**: Tahan gesture 0.5 detik
   - Terlalu cepat = tidak terdeteksi
   - Bisa kembali dan coba lagi

### ❌ Masalah & Solusi:

**Gestur tidak terdeteksi:**
- ✓ Cek pencahayaan
- ✓ Pastikan tangan terlihat jelas di kamera
- ✓ Tunjukkan gesture dengan jelas
- ✓ Tahan lebih lama (coba 1 detik)
- ✓ Gunakan keyboard (A/B/C/D) sebagai backup

**Kamera tidak nyala:**
- ✓ Cek apakah ada app lain yang pakai kamera
- ✓ Restart aplikasi
- ✓ Cek setting permission Windows

**Terjadi error:**
- ✓ Lihat pesan error di console
- ✓ Tutup dan buka lagi
- ✓ Baca QUICK_START.md untuk troubleshooting

---

## 📊 CONTOH GAMEPLAY

### Game Flow Lengkap:

```
START
  ↓
┌─────────────────────────────────────┐
│ MENU SCREEN                         │
│ [MULAI GAME]                        │
└─────────┬───────────────────────────┘
          │ Click START
          ↓
┌─────────────────────────────────────┐
│ SOAL 1/8 - JUMBO                    │
│ [Poster]  [A] [B] [C] [D]          │
│ Gesture: Tunggu...                  │
└─────────┬───────────────────────────┘
          │ Show gesture (Thumb Up)
          ↓
┌─────────────────────────────────────┐
│ ✓ BENAR!                            │
│ Jawaban: JUMBO                      │
│ [LANJUT] atau auto-continue 2 detik │
└─────────┬───────────────────────────┘
          │
          ├─→ SOAL 2/8
          ├─→ SOAL 3/8
          ├─→ ...
          └─→ SOAL 8/8
                  │
                  ↓
        ┌─────────────────────┐
        │ GAME OVER           │
        │ Score: 7/8 (87.5%)  │
        │ Luar Biasa! 🌟      │
        │ [KEMBALI KE MENU]   │
        └─────────────────────┘
```

---

## 📁 FILE YANG DIJALANKAN

Ketika Anda run `python src/main.py`, sistem akan:

1. **Load data:**
   - 8 pertanyaan dari `data/questions.csv`
   - Gesture mapping dari `data/gestures.csv`

2. **Initialize komponen:**
   - Buka kamera (OpenCV)
   - Load MediaPipe (gesture detection)
   - Start Pygame (UI rendering)
   - Setup audio (pygame mixer)

3. **Display menu:**
   - Tunggu user click START

4. **Run game loop:**
   - Setiap frame: deteksi gesture
   - Proses jawaban user
   - Update score
   - Display hasil

5. **Cleanup:**
   - Tutup kamera
   - Hentikan audio
   - Close window

---

## 🎮 PERMAINAN YANG TERSEDIA

### 8 Film yang ditanyakan:

1. **Jumbo** - Film Indonesia (2014)
   - Opsi: Jumbo, Adit & Jarwo, Syifa, Pragos
   - Jawaban: **A (Jumbo)**

2. **Pirates of the Caribbean** - Aksi/Petualangan
   - Opsi: Roman Polankis, Pirates of the Caribbean, Cuthroat Island, The Pirates
   - Jawaban: **B (Pirates of the Caribbean)**

3. **Boboiboy** - Animasi/Superhero
   - Opsi: Amato, Tok Kasa, Boboiboy, Papazola
   - Jawaban: **C (Boboiboy)**

4. **Inception** - Sci-Fi/Mind-Bending
   - Opsi: Inception, Tenet, Interstellar, The Matrix
   - Jawaban: **A (Inception)**

5. **Titanic** - Drama/Romance
   - Opsi: Titanic, Pearl Harbor, The Notebook, Poseidon
   - Jawaban: **A (Titanic)**

6. **Naruto** - Anime/Action
   - Opsi: The Ninja, Ninja Saga, Ninja Scroll, Naruto
   - Jawaban: **D (Naruto)**

7. **Star Wars** - Sci-Fi/Space Opera
   - Opsi: Star Trek, Guardians of the Galaxy, Star Wars, Dune
   - Jawaban: **C (Star Wars)**

8. **Harry Potter** - Fantasy/Magic
   - Opsi: Fantastic Beasts, The Lord of the Rings, The Chronicles of Narnia, Harry Potter
   - Jawaban: **D (Harry Potter)**

---

## 🏁 SELESAI!

Setelah game over, Anda bisa:
- ✅ Klik "KEMBALI KE MENU" untuk main lagi
- ✅ Tekan ESC untuk keluar
- ✅ Coba dapat score 100% (8/8)! 🏆

---

## 📞 PERLU BANTUAN?

Jika ada masalah:

1. **Setup issue?**
   → Baca `QUICK_START.md`

2. **Gesture tidak jalan?**
   → Gunakan keyboard (A/B/C/D) sebagai backup

3. **Error saat run?**
   → Lihat pesan error, biasanya ada solusinya

4. **Ingin customize?**
   → Baca `DEVELOPER_GUIDE.md`

---

## 🎯 RINGKAS - 3 COMMAND SAJA:

```powershell
# 1. Masuk folder
cd d:\Programming\SEMESTER_6\CineTune

# 2. (Optional) Verify setup
python test_components.py

# 3. MAIN!
python src/main.py
```

---

**READY? LET'S PLAY! 🎮🎬**

Tinggal run command `python src/main.py` dan enjoy!

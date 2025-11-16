# 🎮 CineTune - Dokumentasi Developer

## 📋 Daftar Isi
1. [Instalasi & Setup](#instalasi--setup)
2. [Struktur Kode](#struktur-kode)
3. [Komponen Utama](#komponen-utama)
4. [Alur Game](#alur-game)
5. [Debugging & Testing](#debugging--testing)

---

## 🚀 Instalasi & Setup

### Prerequisites
- Python 3.8+
- Webcam/Camera

### Langkah-langkah Instalasi

```bash
# 1. Clone repository
cd d:\Programming\SEMESTER_6\CineTune

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run aplikasi
python src/main.py
```

### Troubleshooting Dependencies
Jika ada error import:
```bash
pip install --upgrade pygame opencv-python mediapipe numpy
```

---

## 📂 Struktur Kode

```
src/
├── main.py                 # Entry point aplikasi
│
├── core/
│   ├── data_loader.py      # Load CSV data (questions & gestures)
│   ├── game_manager.py     # Game logic & state management
│   └── audio_player.py     # Audio/sound effects handler
│
├── ui/
│   ├── tampilan.py         # UI rendering (Pygame)
│   └── frame_utama.py      # Main application class
│
└── vision/
    ├── gesture_detector.py # Hand detection (MediaPipe)
    └── gesture_mapper.py   # Landmark to gesture mapping
```

---

## 🎯 Komponen Utama

### 1. **GestureDetector** (`vision/gesture_detector.py`)
Mendeteksi tangan dan ekstrak 21 landmarks (titik koordinat jari)

**Input:** Frame video (BGR)
**Output:** List of landmarks + frame dengan drawing

```python
detector = GestureDetector()
landmarks, frame = detector.detect(frame)
```

### 2. **GestureMapper** (`vision/gesture_mapper.py`)
Map landmarks ke gesture (A/B/C/D)

**Rules:**
- **A (👍 Thumb Up)**: Jempol tertinggi
- **B (✋ Open Palm)**: Semua jari terbuka
- **C (☝️ Index Up)**: Hanya telunjuk tertinggi
- **D (✊ Fist)**: Semua jari tertutup

### 3. **DataLoader** (`core/data_loader.py`)
Load pertanyaan dari `data/questions.csv` dan gesture mapping dari `data/gestures.csv`

```python
questions = load_questions()      # List of question dicts
gestures = load_gesture_map()     # Dict of gesture->answer mapping
```

### 4. **GameManager** (`core/game_manager.py`)
Handle game logic: soal, scoring, state

```python
gm = GameManager(questions)
gm.start_game()

# During game
current_q = gm.get_current_question()
result = gm.submit_answer("A")
gm.next_question()

# Check status
print(gm.get_stats())
```

### 5. **AudioPlayer** (`core/audio_player.py`)
Play sound effects & question audio

```python
player = AudioPlayer()
player.play_question_audio("path/to/audio.wav")
player.play_correct_sound(base_dir)
player.play_wrong_sound(base_dir)
```

### 6. **GameUI** (`ui/tampilan.py`)
Render UI dengan Pygame

```python
ui = GameUI(width=1280, height=720)

# Draw different screens
ui.draw_menu()
ui.draw_game(question_num, total, image, options, gesture)
ui.draw_result(is_correct, answer, correct)
ui.draw_game_over(score, total, correct_count)
```

### 7. **CineTuneApp** (`ui/frame_utama.py`)
Main application class yang mengintegrasikan semua komponen

---

## 🎮 Alur Game

```
┌─────────────────┐
│   MENU SCREEN   │
│  Tekan START    │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────┐
│   GAME SCREEN               │
│ • Tampil gambar pertanyaan  │
│ • Tunggu gesture pemain     │
│ • Gesture hold 0.5 detik    │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│   RESULT SCREEN             │
│ • Show benar/salah          │
│ • Tampil jawaban benar      │
│ • Tunggu 2 detik / click    │
└────────┬────────────────────┘
         │
         ├─→ Lebih lanjut? ──→ GAME SCREEN (soal berikutnya)
         │
         └─→ Semua selesai? ──→ GAME OVER SCREEN
                                     │
                                     ▼
                              ┌──────────────┐
                              │ GAME OVER    │
                              │ Show score   │
                              │ Back to menu │
                              └──────────────┘
```

---

## 🐛 Debugging & Testing

### Debug Mode
Di `frame_utama.py`, Anda bisa submit answer dengan keyboard (development only):

```python
# A/B/C/D keys untuk manual submit
if event.key == pygame.K_a:  # Submit answer A
    self.submit_answer('A')
```

### Test Individual Components

**Test GestureDetector:**
```bash
python src/main.py  # Akan show gesture di console
```

**Test DataLoader:**
```bash
cd src/core
python data_loader.py
```

**Test GameManager:**
```bash
cd src/core
python game_manager.py
```

**Test AudioPlayer:**
```bash
cd src/core
python audio_player.py
```

### Common Issues

**1. Gesture tidak terdeteksi**
- Pastikan pencahayaan cukup
- Posisikan tangan di depan kamera
- Adjust detection confidence di `gesture_detector.py` (min_detection_confidence)

**2. Audio tidak terdengar**
- Pastikan Pygame mixer initialized
- Check volume setting

**3. Camera error**
- Check apakah camera terbuka di aplikasi lain
- Update driver camera

---

## 📝 Customization

### Mengubah Gesture Rules
Edit `gesture_mapper.py`:

```python
def map(self, landmarks):
    # Sesuaikan threshold dan logic di sini
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    # ... modify rules
```

### Menambah Pertanyaan
Edit `data/questions.csv`:

```csv
id,image_path,audio_path,option_a,option_b,option_c,option_d,answer
9,assets/images/movie.jpg,assets/audio/movie.wav,Opt A,Opt B,Opt C,Opt D,A
```

### Mengubah UI Appearance
Edit `ui/tampilan.py`:

```python
class Colors:
    # Customize colors
    BLUE = (0, 102, 204)  # Main color
    # ... more colors

# Customize fonts
self.font_large = pygame.font.Font(None, 64)
```

---

## 🔗 File Dependencies

```
frame_utama.py (main app)
├── tampilan.py (UI rendering)
├── game_manager.py (game logic)
├── audio_player.py (sounds)
├── data_loader.py (load CSV)
├── gesture_detector.py (hand detection)
└── gesture_mapper.py (landmark mapping)
```

---

## 📊 Data Format

### questions.csv
```csv
id,image_path,audio_path,option_a,option_b,option_c,option_d,answer
1,assets/images/jumbo.jpg,assets/audio/jumbo.wav,JUMBO,ADIT & JARWO,Syifa,Pragos,A
```

### gestures.csv
```csv
gesture_name,answer,description
Thumb_Up,A,Angkat jempol ke atas
Open_Palm,B,Tangan terbuka penuh
Two_Fingers,C,Telunjuk dan jari tengah membentuk 'V'
Fist,D,Genggaman tangan tertutup
```

---

## ✨ Features Implementation Status

- ✅ Gesture Detection (MediaPipe)
- ✅ Game Logic & State Management
- ✅ UI/UX (Pygame)
- ✅ Data Loading (CSV)
- ✅ Audio Player (basic)
- ⏳ Leaderboard/High Scores (future)
- ⏳ Difficulty Levels (future)
- ⏳ Multiplayer (future)

---

**Last Updated:** November 17, 2025
**Project:** CineTune - Tebak Film Lewat Gesture

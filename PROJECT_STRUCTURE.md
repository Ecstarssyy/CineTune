# 📱 CineTune - Project Structure Overview

## 🎯 Project Goal
**CineTune** adalah aplikasi game interaktif untuk menebak film melalui gesture recognition tangan secara real-time.

---

## 📂 Direktori Project

```
CineTune/
│
├── 📄 README.md                    # Project overview
├── 📄 requirements.txt              # Dependencies list
├── 📄 DEVELOPER_GUIDE.md            # Developer documentation
├── 📄 UI_DOCUMENTATION.md           # UI/UX documentation
├── 📄 PROJECT_STRUCTURE.md          # Ini file
├── 📄 test_components.py            # Testing script
│
├── 📁 assets/                       # Media files
│   ├── 📁 images/                   # Film posters (8 images)
│   │   ├── jumbo.jpg
│   │   ├── piratesofthecaribbean.jpg
│   │   ├── boboiboy.jpg
│   │   ├── inception.jpg
│   │   ├── titanic.jpg
│   │   ├── naruto.jpg
│   │   ├── starwars.jpg
│   │   └── harrypotter.jpg
│   │
│   └── 📁 audio/                    # Sound files (8 audio)
│       ├── jumbo.wav
│       ├── piratesofthecaribbean.wav
│       ├── boboiboy.wav
│       ├── inception.wav
│       ├── titanic.wav
│       ├── naruto.wav
│       ├── starwars.wav
│       └── harrypotter.wav
│
├── 📁 data/                         # Data files (CSV)
│   ├── questions.csv                # Quiz questions & answers
│   └── gestures.csv                 # Gesture to answer mapping
│
└── 📁 src/                          # Source code
    │
    ├── 📄 main.py                   # Application entry point
    │
    ├── 📁 core/                     # Core game logic
    │   ├── data_loader.py           # Load CSV data
    │   ├── game_manager.py          # Game state & logic
    │   └── audio_player.py          # Audio handling
    │
    ├── 📁 ui/                       # User interface
    │   ├── tampilan.py              # UI rendering (Pygame)
    │   └── frame_utama.py           # Main application
    │
    └── 📁 vision/                   # Computer vision
        ├── gesture_detector.py      # Hand detection (MediaPipe)
        └── gesture_mapper.py        # Landmark to gesture conversion
```

---

## 🔄 Component Dependencies

```
main.py
  └── frame_utama.py (CineTuneApp)
       ├── tampilan.py (GameUI)
       ├── game_manager.py (GameManager)
       ├── audio_player.py (AudioPlayer)
       ├── data_loader.py
       ├── gesture_detector.py
       └── gesture_mapper.py

test_components.py
  ├── data_loader.py
  ├── game_manager.py
  ├── gesture_detector.py
  ├── gesture_mapper.py
  ├── audio_player.py
  └── tampilan.py
```

---

## 🔄 Game State Flow

```
┌─────────────┐
│   START     │
└──────┬──────┘
       │
       ▼
┌──────────────────────┐
│   MENU_SCREEN        │
│  [START GAME Button] │
└──────┬───────────────┘
       │ Click START
       ▼
┌──────────────────────────────────────┐
│         GAME_SCREEN                  │
│  ┌──────────────────────────────┐   │
│  │ Question Image (Poster Film) │   │
│  └──────────────────────────────┘   │
│  Options: [A] [B] [C] [D]           │
│  Gesture Detection: (Show detected)  │
│  Progress: 1/8                       │
└──────┬───────────────────────────────┘
       │ Gesture detected & held (0.5s)
       ▼
┌──────────────────────────────────────┐
│       RESULT_SCREEN                  │
│  ✓ BENAR / ✗ SALAH                  │
│  Jawaban Benar: [X]                 │
│  [LANJUT Button] or 2 sec auto      │
└──────┬───────────────────────────────┘
       │ Continue
       ├─→ More questions? ──→ GAME_SCREEN (soal berikutnya)
       │
       └─→ All done? ──────────→ GAME_OVER_SCREEN
                                    │
                                    ▼
                        ┌─────────────────────────┐
                        │  GAME_OVER_SCREEN       │
                        │  Score: X/N (Y%)        │
                        │  Message & Stats        │
                        │  [BACK TO MENU Button]  │
                        └──────────┬──────────────┘
                                   │
                                   ▼
                               MENU_SCREEN (loop)
```

---

## 💾 Data Structures

### questions.csv
```csv
id,image_path,audio_path,option_a,option_b,option_c,option_d,answer
1,assets/images/jumbo.jpg,assets/audio/jumbo.wav,JUMBO,ADIT & JARWO,Syifa,Pragos,A
...
```

**Format:**
- `id`: Unique question ID
- `image_path`: Path to film poster image
- `audio_path`: Path to audio file (question audio)
- `option_a/b/c/d`: Answer options
- `answer`: Correct answer (A/B/C/D)

### gestures.csv
```csv
gesture_name,answer,description
Thumb_Up,A,Angkat jempol ke atas
Open_Palm,B,Tangan terbuka penuh
Two_Fingers,C,Telunjuk dan jari tengah membentuk 'V'
Fist,D,Genggaman tangan tertutup
```

**Format:**
- `gesture_name`: Name of gesture
- `answer`: Mapped answer (A/B/C/D)
- `description`: Description

---

## 🎨 Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **UI/Graphics** | Pygame 2.6.1 | Rendering interface |
| **Vision** | MediaPipe 0.10.21 | Hand gesture detection |
| **Vision** | OpenCV 4.10.0 | Image processing |
| **Core** | Python 3.11 | Programming language |
| **Data** | CSV | Store questions/gestures |
| **Audio** | Pygame Mixer | Sound effects |
| **Math** | NumPy 1.26.4 | Numerical operations |

---

## 📊 Key Classes & Functions

### GameUI (ui/tampilan.py)
```python
class GameUI:
    def __init__(width=1280, height=720)
    def draw_menu() -> button_rect
    def draw_game(question_num, total, image, options, gesture) -> option_buttons
    def draw_result(is_correct, answer, correct_answer) -> button_rect
    def draw_game_over(score, total, correct_answers) -> button_rect
    def load_image(image_path, max_width, max_height) -> pygame.Surface
    def quit()
```

### GameManager (core/game_manager.py)
```python
class GameManager:
    def __init__(questions)
    def start_game()
    def get_current_question() -> dict
    def submit_answer(gesture) -> dict
    def next_question()
    def is_game_over() -> bool
    def get_stats() -> dict
    def get_percentage() -> float
```

### CineTuneApp (ui/frame_utama.py)
```python
class CineTuneApp:
    def __init__()
    def run()  # Main game loop
    def handle_menu_state()
    def handle_game_state()
    def handle_result_state()
    def handle_game_over_state()
    def submit_answer(gesture)
    def get_camera_frame() -> (surface, gesture, frame)
    def cleanup()
```

### AudioPlayer (core/audio_player.py)
```python
class AudioPlayer:
    def __init__()
    def play_sound(file_path)
    def play_correct_sound(base_dir)
    def play_wrong_sound(base_dir)
    def play_beep(frequency, duration)
    def set_volume(volume: 0.0-1.0)
    def quit()
```

### GestureDetector (vision/gesture_detector.py)
```python
class GestureDetector:
    def __init__()
    def detect(frame) -> (landmarks, frame_with_drawing)
```

### GestureMapper (vision/gesture_mapper.py)
```python
class GestureMapper:
    def map(landmarks) -> gesture (A/B/C/D or None)
```

---

## 🚀 Execution Flow

### 1. Application Start
```
python src/main.py
  │
  ├─ pygame.init()
  ├─ CineTuneApp.__init__()
  │  ├─ load_questions() from CSV
  │  ├─ load_gesture_map() from CSV
  │  ├─ Initialize GameManager
  │  ├─ Initialize GameUI
  │  ├─ Initialize GestureDetector
  │  └─ Initialize AudioPlayer
  │
  └─ app.run()
```

### 2. Main Game Loop
```
while running:
    if state == MENU:
        display menu
        wait for START click
        → change state to GAME
    
    elif state == GAME:
        get camera frame
        detect gesture
        display question + options
        wait for gesture submission
        → change state to RESULT
    
    elif state == RESULT:
        display correct/wrong
        wait 2 sec or click LANJUT
        move to next question
        → change state to GAME or GAME_OVER
    
    elif state == GAME_OVER:
        display final score
        wait for BACK TO MENU
        → change state to MENU
    
    clock.tick(60)  # 60 FPS
```

---

## 📈 Performance Metrics

| Metric | Target | Notes |
|--------|--------|-------|
| **FPS** | 60 | Smooth gameplay |
| **Gesture Detection Latency** | <100ms | Real-time feedback |
| **Memory Usage** | <500MB | Efficient processing |
| **Image Load Time** | <500ms | Instant display |
| **Audio Latency** | <50ms | Immediate feedback |

---

## 🧪 Testing Strategy

### Component Tests
- `test_components.py` provides unit testing for all components
- Run: `python test_components.py`
- Tests: Data loading, Game manager, Gesture detection, Audio, UI

### Manual Testing
- Play the game end-to-end
- Test gesture recognition with different hand positions
- Verify audio playback
- Check UI responsiveness

---

## 🔧 Configuration & Customization

### Window Size
Edit `frame_utama.py`:
```python
self.ui = GameUI(width=1280, height=720)
```

### Gesture Thresholds
Edit `gesture_mapper.py`:
```python
# Adjust these values for sensitivity
if thumb_tip[1] < index_tip[1] - 50:  # More strict
```

### Gesture Hold Time
Edit `frame_utama.py`:
```python
self.gesture_hold_time = 0.5  # seconds
```

### Audio Volume
Edit `audio_player.py`:
```python
player.set_volume(0.8)  # 80% volume
```

---

## 🐛 Debugging

### Enable Debug Mode
In `frame_utama.py`, uncomment debug prints:
```python
print(f"[DEBUG] Current gesture: {gesture}")
print(f"[DEBUG] Game state: {self.game_manager.phase}")
```

### Check Gesture Detection
Press A/B/C/D keys manually to test without gesture:
```python
elif event.key == pygame.K_a:
    self.submit_answer('A')
```

### Monitor FPS
Add to main loop:
```python
print(f"FPS: {self.ui.clock.get_fps():.1f}")
```

---

## 📖 Documentation Files

1. **README.md** - Project description & features
2. **DEVELOPER_GUIDE.md** - Development & customization guide
3. **UI_DOCUMENTATION.md** - UI/UX detailed documentation
4. **PROJECT_STRUCTURE.md** - This file (architecture overview)

---

## ✅ Implementation Checklist

- ✅ Menu Screen implementation
- ✅ Game Screen implementation
- ✅ Result Screen implementation
- ✅ Game Over Screen implementation
- ✅ Gesture detection integration
- ✅ Audio player integration
- ✅ Game manager integration
- ✅ Data loading (CSV)
- ✅ Camera input handling
- ✅ State management
- ✅ Event handling
- ✅ Component testing
- ✅ Documentation

---

## 🎯 Next Steps

1. **Run the application:**
   ```bash
   python src/main.py
   ```

2. **Test gesture recognition:**
   - Show hand to camera
   - Try different gestures (A, B, C, D)

3. **Play a full game:**
   - Click START
   - Answer all 8 questions
   - Check final score

4. **Customize if needed:**
   - Edit colors in `tampilan.py`
   - Adjust gesture sensitivity in `gesture_mapper.py`
   - Add more questions in `data/questions.csv`

---

**Last Updated:** November 17, 2025  
**Status:** Complete & Ready for Production

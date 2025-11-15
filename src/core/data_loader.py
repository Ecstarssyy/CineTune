import csv

# ==========================================
# PATH ABSOLUTE KE FILE CSV (EDIT INI)
# ==========================================
QUESTIONS_CSV = r"D:\CineTune\data\questions.csv"
GESTURES_CSV  = r"D:\CineTune\data\gestures.csv"
# ==========================================


def load_questions():
    questions = []
    try:
        with open(QUESTIONS_CSV, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                questions.append({
                    "id": int(row["id"]),
                    "image_path": row["image_path"],
                    "audio_path": row["audio_path"],
                    "options": {
                        "A": row["option_a"],
                        "B": row["option_b"],
                        "C": row["option_c"],
                        "D": row["option_d"],
                    },
                    "answer": row["answer"].strip().upper(),
                })
    except Exception as e:
        print("[ERROR] Gagal load questions:", e)
    return questions


def load_gesture_map():
    gestures = {}
    try:
        with open(GESTURES_CSV, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                gestures[row["gesture_name"]] = row["answer"].strip().upper()
    except Exception as e:
        print("[ERROR] Gagal load gestures:", e)
    return gestures


if __name__ == "__main__":
    print("[TEST] Path file:")
    print("Questions CSV:", QUESTIONS_CSV)
    print("Gestures CSV :", GESTURES_CSV)

    qs = load_questions()
    print("\nLoaded questions:", len(qs))
    if qs:
        print("Sample question:", qs[0])

    gm = load_gesture_map()
    print("\nGesture map:", gm)

#!/usr/bin/env python3
"""
Test script untuk validasi semua komponen CineTune
Run: python test_components.py
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """Test semua imports"""
    print("=" * 60)
    print("TEST 1: Validasi Imports")
    print("=" * 60)
    
    try:
        print("  ✓ Importing cv2...", end=" ")
        import cv2
        print("OK")
    except ImportError as e:
        print(f"FAILED - {e}")
    
    try:
        print("  ✓ Importing pygame...", end=" ")
        import pygame
        print("OK")
    except ImportError as e:
        print(f"FAILED - {e}")
    
    try:
        print("  ✓ Importing mediapipe...", end=" ")
        import mediapipe
        print("OK")
    except ImportError as e:
        print(f"FAILED - {e}")
    
    try:
        print("  ✓ Importing numpy...", end=" ")
        import numpy
        print("OK")
    except ImportError as e:
        print(f"FAILED - {e}")
    
    print()

def test_data_loader():
    """Test data loader"""
    print("=" * 60)
    print("TEST 2: Data Loader")
    print("=" * 60)
    
    try:
        from core.data_loader import load_questions, load_gesture_map
        
        print("  ✓ Loading questions...", end=" ")
        questions = load_questions()
        print(f"OK ({len(questions)} questions)")
        
        if questions:
            print(f"  ✓ Sample question: {questions[0]['id']}")
            print(f"    - Image: {os.path.exists(questions[0]['image'])}")
            print(f"    - Options: {questions[0]['options']}")
            print(f"    - Answer: {questions[0]['answer']}")
        
        print("  ✓ Loading gestures...", end=" ")
        gestures = load_gesture_map()
        print(f"OK ({len(gestures)} gestures)")
        print(f"    Gesture map: {gestures}")
        
        print()
        return True
    except Exception as e:
        print(f"FAILED - {e}")
        import traceback
        traceback.print_exc()
        print()
        return False

def test_game_manager():
    """Test game manager"""
    print("=" * 60)
    print("TEST 3: Game Manager")
    print("=" * 60)
    
    try:
        from core.data_loader import load_questions
        from core.game_manager import GameManager
        
        print("  ✓ Creating GameManager...", end=" ")
        questions = load_questions()
        gm = GameManager(questions)
        print("OK")
        
        print(f"  ✓ Total questions: {gm.get_total_questions()}")
        
        print("  ✓ Starting game...", end=" ")
        gm.start_game()
        print("OK")
        
        print(f"  ✓ Current question: {gm.get_current_question_number()}")
        
        q = gm.get_current_question()
        if q:
            print(f"  ✓ Question options: {list(q['options'].keys())}")
        
        print("  ✓ Submitting answer A...", end=" ")
        result = gm.submit_answer('A')
        print("OK")
        print(f"    - Result: {result}")
        
        print("  ✓ Game stats:", end=" ")
        stats = gm.get_stats()
        print(f"{stats}")
        
        print()
        return True
    except Exception as e:
        print(f"FAILED - {e}")
        import traceback
        traceback.print_exc()
        print()
        return False

def test_gesture_detector():
    """Test gesture detector"""
    print("=" * 60)
    print("TEST 4: Gesture Detector & Mapper")
    print("=" * 60)
    
    try:
        from vision.gesture_detector import GestureDetector
        from vision.gesture_mapper import GestureMapper
        
        print("  ✓ Creating GestureDetector...", end=" ")
        detector = GestureDetector()
        print("OK")
        
        print("  ✓ Creating GestureMapper...", end=" ")
        mapper = GestureMapper()
        print("OK")
        
        print("  ✓ [NOTE] To fully test, run: python src/main.py")
        print("    and show your hand to the camera")
        
        print()
        return True
    except Exception as e:
        print(f"FAILED - {e}")
        import traceback
        traceback.print_exc()
        print()
        return False

def test_audio_player():
    """Test audio player"""
    print("=" * 60)
    print("TEST 5: Audio Player")
    print("=" * 60)
    
    try:
        from core.audio_player import AudioPlayer
        
        print("  ✓ Creating AudioPlayer...", end=" ")
        player = AudioPlayer()
        print("OK")
        
        print(f"  ✓ Mixer initialized: {player.is_initialized}")
        
        if player.is_initialized:
            print("  ✓ Testing beep sound...", end=" ")
            player.play_beep(frequency=440, duration=200)
            print("OK (check if you heard sound)")
        
        print()
        return True
    except Exception as e:
        print(f"FAILED - {e}")
        import traceback
        traceback.print_exc()
        print()
        return False

def test_ui():
    """Test UI"""
    print("=" * 60)
    print("TEST 6: UI/Pygame")
    print("=" * 60)
    
    try:
        from ui.tampilan import GameUI, GameState
        
        print("  ✓ Initializing GameUI...", end=" ")
        ui = GameUI(width=1280, height=720)
        print("OK")
        
        print(f"  ✓ Window size: {ui.width}x{ui.height}")
        print(f"  ✓ Current state: {ui.state.name}")
        
        print("  ✓ Fonts loaded: OK")
        
        print("  ✓ [NOTE] To fully test, run: python src/main.py")
        
        ui.quit()
        print()
        return True
    except Exception as e:
        print(f"FAILED - {e}")
        import traceback
        traceback.print_exc()
        print()
        return False

def main():
    """Run all tests"""
    print("\n")
    print("=" * 60)
    print("  CineTune - Component Test Suite".center(60))
    print("=" * 60)
    print("\n")
    
    results = []
    
    test_imports()
    results.append(("Data Loader", test_data_loader()))
    results.append(("Game Manager", test_game_manager()))
    results.append(("Gesture Detection", test_gesture_detector()))
    results.append(("Audio Player", test_audio_player()))
    results.append(("UI/Pygame", test_ui()))
    
    # Summary
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    for name, result in results:
        status = "PASS" if result else "FAIL"
        print(f"  [{status}] {name}")
    
    passed = sum(1 for _, r in results if r)
    total = len(results)
    
    print()
    print(f"Total: {passed}/{total} passed")
    print()
    
    if passed == total:
        print("[OK] All tests passed! Ready to run: python src/main.py")
    else:
        print("[WARNING] Some tests failed. Check dependencies.")
    
    print()

if __name__ == "__main__":
    main()

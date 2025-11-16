import sys
import os

# Add ui directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ui.frame_utama import CineTuneApp

def main():
    """Main entry point"""
    print("=" * 50)
    print("  CineTune - Tebak Film Lewat Gesture")
    print("=" * 50)
    print()
    
    try:
        app = CineTuneApp()
        app.run()
    except KeyboardInterrupt:
        print("\n[INFO] Application interrupted by user")
    except Exception as e:
        print(f"[ERROR] Application error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        try:
            app.cleanup()
        except:
            pass

if __name__ == "__main__":
    main()

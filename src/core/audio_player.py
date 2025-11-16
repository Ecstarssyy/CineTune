import pygame
import os
from pathlib import Path

# ==========================================
# AUDIO PLAYER CLASS
# ==========================================
class AudioPlayer:
    def __init__(self):
        """Initialize audio player"""
        try:
            pygame.mixer.init()
            self.is_initialized = True
            self.current_sound = None
            self.sound_effects = {}
        except Exception as e:
            print(f"[WARNING] Pygame mixer tidak tersedia: {e}")
            self.is_initialized = False
    
    def load_sound(self, file_path):
        """Load a sound file"""
        if not self.is_initialized:
            return None
        
        try:
            if os.path.exists(file_path):
                sound = pygame.mixer.Sound(file_path)
                return sound
            else:
                print(f"[WARNING] File audio tidak ditemukan: {file_path}")
                return None
        except Exception as e:
            print(f"[ERROR] Gagal load audio {file_path}: {e}")
            return None
    
    def play_sound(self, file_path):
        """Play a sound effect"""
        if not self.is_initialized:
            return
        
        sound = self.load_sound(file_path)
        if sound:
            try:
                sound.play()
                self.current_sound = sound
            except Exception as e:
                print(f"[ERROR] Gagal play sound: {e}")
    
    def play_question_audio(self, file_path):
        """Play question audio"""
        self.play_sound(file_path)
    
    def stop(self):
        """Stop all sounds"""
        if not self.is_initialized:
            return
        try:
            pygame.mixer.stop()
        except Exception as e:
            print(f"[ERROR] Gagal stop audio: {e}")
    
    def play_correct_sound(self, base_dir):
        """Play sound effect for correct answer"""
        # Create a simple beep sound if file doesn't exist
        if not self.is_initialized:
            return
        
        try:
            # Try to load a correct sound (if exists)
            correct_sounds = [
                os.path.join(base_dir, "assets", "audio", "correct.wav"),
            ]
            for sound_path in correct_sounds:
                if os.path.exists(sound_path):
                    self.play_sound(sound_path)
                    return
            
            # Fallback: create beep programmatically
            self.play_beep(frequency=1000, duration=200)
        except Exception as e:
            print(f"[WARNING] Gagal play correct sound: {e}")
    
    def play_wrong_sound(self, base_dir):
        """Play sound effect for wrong answer"""
        if not self.is_initialized:
            return
        
        try:
            # Try to load a wrong sound (if exists)
            wrong_sounds = [
                os.path.join(base_dir, "assets", "audio", "wrong.wav"),
            ]
            for sound_path in wrong_sounds:
                if os.path.exists(sound_path):
                    self.play_sound(sound_path)
                    return
            
            # Fallback: create beep programmatically
            self.play_beep(frequency=300, duration=300)
        except Exception as e:
            print(f"[WARNING] Gagal play wrong sound: {e}")
    
    def play_beep(self, frequency=440, duration=200, sample_rate=22050):
        """Generate and play a simple beep sound"""
        if not self.is_initialized:
            return
        
        try:
            import math
            import numpy as np
            
            # Generate beep
            frames = int(duration * sample_rate / 1000)
            arr = np.sin(2.0 * math.pi * frequency * np.linspace(0, duration / 1000, frames))
            arr = (arr * 32767).astype(np.int16)
            arr = np.repeat(arr.reshape(frames, 1), 2, axis=1)
            
            sound = pygame.sndarray.make_sound(arr)
            sound.play()
        except Exception as e:
            print(f"[WARNING] Tidak bisa generate beep: {e}")
    
    def set_volume(self, volume):
        """Set master volume (0.0 - 1.0)"""
        if not self.is_initialized:
            return
        
        try:
            pygame.mixer.music.set_volume(max(0.0, min(1.0, volume)))
        except Exception as e:
            print(f"[WARNING] Gagal set volume: {e}")
    
    def quit(self):
        """Stop and quit audio"""
        if self.is_initialized:
            try:
                pygame.mixer.quit()
            except Exception as e:
                print(f"[WARNING] Error saat quit audio: {e}")


if __name__ == "__main__":
    # Test audio player
    import time
    
    player = AudioPlayer()
    
    print("[TEST] Audio Player initialized")
    print(f"Mixer available: {player.is_initialized}")
    
    if player.is_initialized:
        print("\nPlaying beep test...")
        player.play_beep(frequency=440, duration=500)
        time.sleep(1)
        
        print("Test completed")
    
    player.quit()

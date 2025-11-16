import pygame
import os
from enum import Enum

# ==========================================
# CONSTANTS & COLORS
# ==========================================
class Colors:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    DARK_GRAY = (30, 30, 30)
    LIGHT_GRAY = (200, 200, 200)
    BLUE = (0, 102, 204)
    DARK_BLUE = (0, 51, 102)
    GREEN = (0, 200, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 165, 0)

class GameState(Enum):
    MENU = 1
    GAME = 2
    RESULT = 3
    GAME_OVER = 4

# ==========================================
# UI UTILITIES
# ==========================================
def draw_text(surface, text, font, color, rect):
    """Draw text centered in a rect"""
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)

def draw_button(surface, text, rect, font, bg_color, text_color, hover=False):
    """Draw a button with optional hover effect"""
    if hover:
        pygame.draw.rect(surface, (min(bg_color[0] + 30, 255), 
                                   min(bg_color[1] + 30, 255), 
                                   min(bg_color[2] + 30, 255)), rect, border_radius=10)
    else:
        pygame.draw.rect(surface, bg_color, rect, border_radius=10)
    
    pygame.draw.rect(surface, text_color, rect, 3, border_radius=10)
    draw_text(surface, text, font, text_color, rect)

# ==========================================
# UI CLASS
# ==========================================
class GameUI:
    def __init__(self, width=1280, height=720):
        # Initialize pygame if not already initialized
        if not pygame.get_init():
            pygame.init()
        
        # Initialize font module if not already initialized
        if not pygame.font.get_init():
            pygame.font.init()
        
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("CineTune - Tebak Film Lewat Gesture")
        
        # Fonts
        self.font_large = pygame.font.Font(None, 64)
        self.font_medium = pygame.font.Font(None, 48)
        self.font_small = pygame.font.Font(None, 32)
        self.font_tiny = pygame.font.Font(None, 24)
        
        # Clock
        self.clock = pygame.time.Clock()
        
        # Current state
        self.state = GameState.MENU
        
    def draw_menu(self):
        """Draw main menu screen"""
        self.screen.fill(Colors.DARK_GRAY)
        
        # Title
        title_rect = pygame.Rect(0, 100, self.width, 100)
        draw_text(self.screen, "CineTune", self.font_large, Colors.YELLOW, title_rect)
        
        subtitle_rect = pygame.Rect(0, 200, self.width, 50)
        draw_text(self.screen, "Tebak Film Lewat Gesture", self.font_small, Colors.LIGHT_GRAY, subtitle_rect)
        
        # Start button
        start_button = pygame.Rect(self.width // 2 - 150, 350, 300, 70)
        draw_button(self.screen, "MULAI GAME", start_button, self.font_medium, 
                   Colors.BLUE, Colors.WHITE, hover=False)
        
        # Instructions
        instructions = [
            "👍 Thumb Up (Jempol Naik) = Jawaban A",
            "✋ Open Palm (Tangan Terbuka) = Jawaban B",
            "✌️ Two Fingers (V) = Jawaban C",
            "✊ Fist (Genggaman) = Jawaban D",
        ]
        
        y_pos = 470
        for instruction in instructions:
            instr_surface = self.font_tiny.render(instruction, True, Colors.LIGHT_GRAY)
            self.screen.blit(instr_surface, (100, y_pos))
            y_pos += 35
        
        pygame.display.flip()
        return start_button
    
    def draw_game(self, question_num, total_questions, image_surface, options, 
                  current_gesture=None, gesture_confidence=0, camera_frame=None):
        """Draw game screen with question, image, and options"""
        self.screen.fill(Colors.DARK_GRAY)
        
        # Header - Question number and progress
        header_text = f"Soal {question_num}/{total_questions}"
        header_surface = self.font_medium.render(header_text, True, Colors.YELLOW)
        self.screen.blit(header_surface, (20, 20))
        
        # Progress bar
        progress_width = (question_num / total_questions) * (self.width - 40)
        pygame.draw.rect(self.screen, Colors.BLUE, (20, 70, progress_width, 15))
        pygame.draw.rect(self.screen, Colors.LIGHT_GRAY, (20, 70, self.width - 40, 15), 2)
        
        # Camera preview (top-left or top-center)
        if camera_frame:
            # Scale camera frame to fit
            cam_width = 320
            cam_height = 240
            try:
                camera_frame_scaled = pygame.transform.scale(camera_frame, (cam_width, cam_height))
                cam_x = 20
                cam_y = 100
                self.screen.blit(camera_frame_scaled, (cam_x, cam_y))
                # Draw border around camera
                pygame.draw.rect(self.screen, Colors.GREEN, (cam_x, cam_y, cam_width, cam_height), 3)
            except:
                pass
        
        # Image display (left side, below camera)
        if image_surface:
            img_x = 20
            img_y = 360
            self.screen.blit(image_surface, (img_x, img_y))
        
        # Options display (right side)
        options_x = self.width - 480
        options_y = 120
        option_height = 120
        option_width = 420
        
        option_buttons = {}
        for idx, (key, text) in enumerate(options.items()):
            y = options_y + idx * (option_height + 15)
            button_rect = pygame.Rect(options_x, y, option_width, option_height)
            option_buttons[key] = button_rect
            
            # Draw button
            draw_button(self.screen, f"{key}: {text}", button_rect, self.font_small,
                       Colors.DARK_BLUE, Colors.WHITE, hover=False)
        
        # Current gesture detection display (bottom)
        if current_gesture:
            gesture_text = f"Gesture Terdeteksi: {current_gesture}"
            if gesture_confidence > 0:
                gesture_text += f" ({gesture_confidence:.0%})"
            gesture_surface = self.font_small.render(gesture_text, True, Colors.GREEN)
            self.screen.blit(gesture_surface, (20, self.height - 60))
        else:
            no_gesture = "Posisikan tangan di depan kamera..."
            no_gesture_surface = self.font_small.render(no_gesture, True, Colors.YELLOW)
            self.screen.blit(no_gesture_surface, (20, self.height - 60))
        
        pygame.display.flip()
        return option_buttons
    
    def draw_result(self, is_correct, answer_key, correct_answer, feedback_text=""):
        """Draw result screen after answering"""
        self.screen.fill(Colors.DARK_GRAY)
        
        if is_correct:
            result_color = Colors.GREEN
            result_text = "✓ BENAR!"
        else:
            result_color = Colors.RED
            result_text = "✗ SALAH!"
        
        # Result title
        result_rect = pygame.Rect(0, 150, self.width, 100)
        draw_text(self.screen, result_text, self.font_large, result_color, result_rect)
        
        # Feedback
        if feedback_text:
            feedback_surface = self.font_small.render(feedback_text, True, Colors.LIGHT_GRAY)
            feedback_rect = feedback_surface.get_rect(center=(self.width // 2, 300))
            self.screen.blit(feedback_surface, feedback_rect)
        
        # Show correct answer
        correct_text = f"Jawaban Benar: {correct_answer}"
        correct_surface = self.font_medium.render(correct_text, True, Colors.YELLOW)
        correct_rect = correct_surface.get_rect(center=(self.width // 2, 400))
        self.screen.blit(correct_surface, correct_rect)
        
        # Continue button
        continue_button = pygame.Rect(self.width // 2 - 150, 550, 300, 70)
        draw_button(self.screen, "LANJUT", continue_button, self.font_medium,
                   Colors.BLUE, Colors.WHITE, hover=False)
        
        pygame.display.flip()
        return continue_button
    
    def draw_game_over(self, score, total_questions, correct_answers):
        """Draw game over screen"""
        self.screen.fill(Colors.DARK_GRAY)
        
        # Game over title
        title_rect = pygame.Rect(0, 80, self.width, 100)
        draw_text(self.screen, "GAME SELESAI", self.font_large, Colors.YELLOW, title_rect)
        
        # Score display
        percentage = (correct_answers / total_questions * 100) if total_questions > 0 else 0
        score_text = f"Skor: {score}/{total_questions} ({percentage:.1f}%)"
        score_rect = pygame.Rect(0, 250, self.width, 60)
        draw_text(self.screen, score_text, self.font_medium, Colors.GREEN, score_rect)
        
        # Result message
        if percentage >= 80:
            message = "Luar Biasa! 🌟"
            message_color = Colors.GREEN
        elif percentage >= 60:
            message = "Bagus! 👍"
            message_color = Colors.YELLOW
        else:
            message = "Coba lagi! 💪"
            message_color = Colors.ORANGE
        
        message_rect = pygame.Rect(0, 350, self.width, 60)
        draw_text(self.screen, message, self.font_medium, message_color, message_rect)
        
        # Menu button
        menu_button = pygame.Rect(self.width // 2 - 150, 550, 300, 70)
        draw_button(self.screen, "KEMBALI KE MENU", menu_button, self.font_medium,
                   Colors.BLUE, Colors.WHITE, hover=False)
        
        pygame.display.flip()
        return menu_button
    
    def draw_camera_preview(self, frame_surface, x=0, y=100):
        """Draw camera preview (for gesture detection)"""
        if frame_surface:
            self.screen.blit(frame_surface, (x, y))
            # Draw border
            pygame.draw.rect(self.screen, Colors.GREEN, 
                           (x, y, frame_surface.get_width(), frame_surface.get_height()), 3)
    
    def load_image(self, image_path, max_width=400, max_height=400):
        """Load and scale image for display"""
        try:
            img = pygame.image.load(image_path)
            img.set_colorkey(Colors.BLACK)  # Remove black background if any
            
            # Scale image
            img_rect = img.get_rect()
            scale_factor = min(max_width / img_rect.width, max_height / img_rect.height)
            new_size = (int(img_rect.width * scale_factor), int(img_rect.height * scale_factor))
            img = pygame.transform.scale(img, new_size)
            
            return img
        except Exception as e:
            print(f"[ERROR] Gagal load image {image_path}: {e}")
            return None
    
    def quit(self):
        """Cleanup"""
        pygame.quit()


if __name__ == "__main__":
    pygame.init()
    ui = GameUI()
    
    # Test menu
    running = True
    while running:
        button = ui.draw_menu()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    print("Start button clicked!")
        
        ui.clock.tick(60)
    
    ui.quit()

import random
import os
from enum import Enum

# ==========================================
# GAME STATE ENUM
# ==========================================
class GamePhase(Enum):
    IDLE = 0
    WAITING_ANSWER = 1
    SHOWING_RESULT = 2
    GAME_OVER = 3

# ==========================================
# GAME MANAGER CLASS
# ==========================================
class GameManager:
    def __init__(self, questions):
        """
        Initialize game manager
        
        Args:
            questions: List of question dicts with structure:
                {
                    "id": int,
                    "image": str (path),
                    "audio": str (path),
                    "options": {"A": str, "B": str, "C": str, "D": str},
                    "answer": str (A/B/C/D)
                }
        """
        self.questions = questions if questions else []
        self.current_question_idx = 0
        self.score = 0
        self.answered_count = 0
        self.phase = GamePhase.IDLE
        
        # Shuffle questions
        if self.questions:
            random.shuffle(self.questions)
    
    def start_game(self):
        """Start the game"""
        self.current_question_idx = 0
        self.score = 0
        self.answered_count = 0
        self.phase = GamePhase.WAITING_ANSWER
    
    def get_current_question(self):
        """Get current question"""
        if self.is_game_over():
            return None
        return self.questions[self.current_question_idx]
    
    def get_current_question_number(self):
        """Get current question number (1-indexed)"""
        return self.current_question_idx + 1
    
    def get_total_questions(self):
        """Get total number of questions"""
        return len(self.questions)
    
    def submit_answer(self, gesture_answer):
        """
        Submit an answer
        
        Args:
            gesture_answer: str (A/B/C/D)
        
        Returns:
            dict with keys:
                - is_correct: bool
                - correct_answer: str
                - user_answer: str
        """
        if self.is_game_over():
            return None
        
        current_q = self.get_current_question()
        if not current_q:
            return None
        
        correct_answer = current_q["answer"]
        is_correct = gesture_answer == correct_answer
        
        if is_correct:
            self.score += 1
        
        self.answered_count += 1
        self.phase = GamePhase.SHOWING_RESULT
        
        result = {
            "is_correct": is_correct,
            "correct_answer": correct_answer,
            "user_answer": gesture_answer,
        }
        
        return result
    
    def next_question(self):
        """Move to next question"""
        self.current_question_idx += 1
        
        if self.is_game_over():
            self.phase = GamePhase.GAME_OVER
        else:
            self.phase = GamePhase.WAITING_ANSWER
    
    def is_game_over(self):
        """Check if game is over"""
        return self.current_question_idx >= len(self.questions)
    
    def get_score(self):
        """Get current score"""
        return self.score
    
    def get_percentage(self):
        """Get correct answer percentage"""
        if self.answered_count == 0:
            return 0
        return (self.score / self.answered_count) * 100
    
    def get_stats(self):
        """Get game statistics"""
        return {
            "total_questions": len(self.questions),
            "answered_count": self.answered_count,
            "score": self.score,
            "percentage": self.get_percentage(),
            "phase": self.phase.name,
        }
    
    def reset(self):
        """Reset game"""
        self.__init__(self.questions)


if __name__ == "__main__":
    # Test game manager
    test_questions = [
        {
            "id": 1,
            "image": "path/to/image.jpg",
            "audio": "path/to/audio.wav",
            "options": {"A": "Option A", "B": "Option B", "C": "Option C", "D": "Option D"},
            "answer": "A"
        },
        {
            "id": 2,
            "image": "path/to/image2.jpg",
            "audio": "path/to/audio2.wav",
            "options": {"A": "Option A", "B": "Option B", "C": "Option C", "D": "Option D"},
            "answer": "B"
        },
    ]
    
    gm = GameManager(test_questions)
    print("[TEST] GameManager initialized")
    print(f"Total questions: {gm.get_total_questions()}")
    
    gm.start_game()
    print(f"\nGame started. Phase: {gm.phase.name}")
    
    q1 = gm.get_current_question()
    print(f"Q{gm.get_current_question_number()}: {q1['options']}")
    
    result = gm.submit_answer("A")
    print(f"Submitted answer 'A': {result}")
    
    gm.next_question()
    print(f"\nQ{gm.get_current_question_number()}: Moving to next question")
    
    result2 = gm.submit_answer("B")
    print(f"Submitted answer 'B': {result2}")
    
    gm.next_question()
    print(f"\nGame over: {gm.is_game_over()}")
    print(f"Stats: {gm.get_stats()}")

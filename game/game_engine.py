import pygame
from .paddle import Paddle
from .ball import Ball

# Game Constants
WHITE = (255, 255, 255)

class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # ... (other attributes are the same) ...
        self.player = Paddle(10, height // 2 - 50, 10, 100)
        self.ai = Paddle(width - 20, height // 2 - 50, 10, 100)
        self.ball = Ball(width // 2, height // 2, 15, 15, width, height)
        self.player_score = 0
        self.ai_score = 0
        self.font = pygame.font.SysFont(None, 50)
        self.winning_score = 3
        self.game_state = "playing"
        self.winner_text = ""

        # --- Load Sound Effects ---
        try:
            self.hit_sound = pygame.mixer.Sound("assets/paddle_hit.wav")
            self.wall_sound = pygame.mixer.Sound("assets/wall_bounce.wav")
            self.score_sound = pygame.mixer.Sound("assets/score_point.wav")
        except pygame.error as e:
            print(f"Error loading sound file: {e}")
            # Create dummy sound objects if files are missing
            self.hit_sound = pygame.mixer.Sound(buffer=b'')
            self.wall_sound = pygame.mixer.Sound(buffer=b'')
            self.score_sound = pygame.mixer.Sound(buffer=b'')


    def handle_input(self):
        # ... (no changes here) ...
        if self.game_state == "playing":
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.player.move(-self.player.speed, self.height)
            if keys[pygame.K_s]:
                self.player.move(self.player.speed, self.height)

    def update(self):
        if self.game_state == "playing":
            # --- Play sounds based on events ---
            if self.ball.move():
                self.wall_sound.play() # Play wall bounce sound
            
            if self.ball.check_collision(self.player, self.ai):
                self.hit_sound.play() # Play paddle hit sound

            # Check for scoring
            if self.ball.x <= 0:
                self.ai_score += 1
                self.ball.reset()
                self.score_sound.play() # Play score sound
            elif self.ball.x + self.ball.width >= self.width:
                self.player_score += 1
                self.ball.reset()
                self.score_sound.play() # Play score sound

            self.ai.auto_track(self.ball, self.height)
            
            # Check for a winner
            if self.player_score >= self.winning_score:
                self.winner_text = "Player Wins!"
                self.game_state = "game_over"
            elif self.ai_score >= self.winning_score:
                self.winner_text = "AI Wins!"
                self.game_state = "game_over"

    # ... (render and reset_game methods are the same) ...
    def render(self, screen):
        if self.game_state == "game_over":
            self.render_game_over(screen)
        else:
            pygame.draw.rect(screen, WHITE, self.player.rect())
            pygame.draw.rect(screen, WHITE, self.ai.rect())
            pygame.draw.ellipse(screen, WHITE, self.ball.rect())
            pygame.draw.aaline(screen, WHITE, (self.width//2, 0), (self.width//2, self.height))
            player_text = self.font.render(str(self.player_score), True, WHITE)
            ai_text = self.font.render(str(self.ai_score), True, WHITE)
            screen.blit(player_text, (self.width//4 - player_text.get_width()//2, 20))
            screen.blit(ai_text, (self.width * 3//4 - ai_text.get_width()//2, 20))
    
    def render_game_over(self, screen):
        title_font = pygame.font.SysFont(None, 70)
        option_font = pygame.font.SysFont(None, 40)
        winner_surface = title_font.render(self.winner_text, True, WHITE)
        screen.blit(winner_surface, (self.width//2 - winner_surface.get_width()//2, self.height//4))
        options = ["Best of 3 (Press 3)", "Best of 5 (Press 5)", "Best of 7 (Press 7)", "Exit (Press ESC)"]
        for i, option in enumerate(options):
            option_surface = option_font.render(option, True, WHITE)
            y_pos = self.height//2 + i * 40
            screen.blit(option_surface, (self.width//2 - option_surface.get_width()//2, y_pos))

    def reset_game(self, new_score_target):
        self.winning_score = new_score_target
        self.player_score = 0
        self.ai_score = 0
        self.winner_text = ""
        self.game_state = "playing"
        self.ball.reset()
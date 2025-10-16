import pygame
import random

class Ball:
    def __init__(self, x, y, width, height, screen_width, screen_height):
        # ... (init method is the same) ...
        self.original_x = x
        self.original_y = y
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.velocity_x = random.choice([-7, 7])
        self.velocity_y = random.choice([-5, 5])

    def move(self):
        """Moves the ball and returns True if it bounces off a wall."""
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Bounce off top and bottom walls
        if self.y <= 0 or self.y + self.height >= self.screen_height:
            self.velocity_y *= -1
            return True # <-- RETURN TRUE ON BOUNCE
        return False

    def check_collision(self, player, ai):
        """Checks for paddle collision and returns True if one occurs."""
        ball_rect = self.rect()
        player_rect = player.rect()
        ai_rect = ai.rect()

        if self.velocity_x < 0:
            if ball_rect.colliderect(player_rect):
                self.velocity_x *= -1
                self.x = player.x + player.width
                return True # <-- RETURN TRUE ON COLLISION
        
        if self.velocity_x > 0:
            if ball_rect.colliderect(ai_rect):
                self.velocity_x *= -1
                self.x = ai.x - self.width
                return True # <-- RETURN TRUE ON COLLISION
        
        return False

    # ... (reset and rect methods are the same) ...
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.velocity_x *= -1
        self.velocity_y = random.choice([-5, -4, -3, 3, 4, 5])

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
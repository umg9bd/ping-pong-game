import pygame
import random

class Ball:
    def __init__(self, x, y, width, height, screen_width, screen_height):
        self.original_x = x
        self.original_y = y
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height
        # Increased base speed
        self.velocity_x = random.choice([-7, 7])
        self.velocity_y = random.choice([-5, 5])

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Bounce off top and bottom walls
        if self.y <= 0 or self.y + self.height >= self.screen_height:
            self.velocity_y *= -1

    def check_collision(self, player, ai):
        # Check collision based on ball's direction
        if self.velocity_x < 0: # Moving left, check player
            if self.rect().colliderect(player.rect()):
                self.velocity_x *= -1
        elif self.velocity_x > 0: # Moving right, check AI
            if self.rect().colliderect(ai.rect()):
                self.velocity_x *= -1

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.velocity_x *= -1
        # Ensure y velocity is not 0
        self.velocity_y = random.choice([-5, -4, -3, 3, 4, 5])

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
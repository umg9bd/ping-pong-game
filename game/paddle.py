import pygame

class Paddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 6 # Adjusted speed slightly

    def move(self, dy, screen_height):
        self.y += dy
        # Keep the paddle on the screen
        if self.y < 0:
            self.y = 0
        if self.y + self.height > screen_height:
            self.y = screen_height - self.height

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def auto_track(self, ball, screen_height):
        # Improved AI: track the center of the ball for smoother movement
        paddle_center = self.y + self.height / 2
        ball_center = ball.y + ball.height / 2
        
        if paddle_center < ball_center - 5: # -5 adds a small dead zone
            self.move(self.speed, screen_height)
        elif paddle_center > ball_center + 5: # +5 adds a small dead zone
            self.move(-self.speed, screen_height)
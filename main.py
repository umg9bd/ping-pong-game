import pygame
from game.game_engine import GameEngine

# Initialize pygame/Start application
pygame.init()
pygame.mixer.init() # <-- INITIALIZE THE MIXER

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong - Pygame Version")

BLACK = (0, 0, 0)
FPS = 60

clock = pygame.time.Clock()
engine = GameEngine(WIDTH, HEIGHT)

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if engine.game_state == "game_over":
                    if event.key == pygame.K_3:
                        engine.reset_game(3)
                    elif event.key == pygame.K_5:
                        engine.reset_game(5)
                    elif event.key == pygame.K_7:
                        engine.reset_game(7)
                    elif event.key == pygame.K_ESCAPE:
                        running = False

        SCREEN.fill(BLACK)

        engine.handle_input()
        engine.update()
        engine.render(SCREEN)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
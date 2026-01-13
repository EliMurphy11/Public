"""Quick preview for the Ship sprite (renders the ship/chicken nugget)."""
import sys
import pygame
from settings import Settings
from ship import Ship


def run_preview():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption('Ship Preview')

    class Dummy:
        pass

    ai = Dummy()
    ai.screen = screen
    ai.settings = settings

    ship = Ship(ai)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False

        screen.fill(settings.bg_color)
        ship.blitme()
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    run_preview()

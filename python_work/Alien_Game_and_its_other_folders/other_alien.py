import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
        """Overall class to manage game assets and behavior."""
        def __init__(self): 
            pygame.display.set_caption("Alien Invasion")

            # Set the background color.
            self.bg_color = (128, 0, 128)
            pygame.init() 
            self.settings = Settings()

            self.screen = pygame.display.set_mode((1200, 1500))
            (self.settings.screen_width, self.settings.screen_height) = self.screen.get_size()
            pygame.display.set_caption("Alien Invasion")

            self.ship = Ship(self)

            # Set the background color
            self.bg_color = (50, 100, 150)

        def run_game(self):
            """Start the main loop for the game"""
            while True:
                self._check_events()

                # Redraw the screen during each pass through the loop
                self.screen.fill(self.bg_color)
                self.ship.blitme()

                # Make the most recently drawn screen visible.
                pygame.display.flip()

        def _check_events(self):
            """Respond to keypresses and mouse events."""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

class Ship: 
        """A class to manage the ship."""

        def __init__(self, ai_game):
            """Initialize the ship and set its starting position.""" 
            self.screen = ai_game.screen
            self.screen_rect = ai_game.screen.get_rect()
            
            # Load the ship image and get its rect.
            self.image = pygame.image.load('images/Dr Ppper can.png')
            self.rect = self.image.get_rect()
            # Start each new ship at the bottom center of the screen.
            self.rect.midbottom = self.screen_rect.midbottom

        def blitme(self):
            """Draw the ship at its current location."""
            self.screen.blit(self.image, self.rect)

if __name__ == '__main__':
        ai = AlienInvasion()
        ai.run_game()
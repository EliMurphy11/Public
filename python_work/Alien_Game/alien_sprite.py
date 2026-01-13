import os
import pygame


class Alien(pygame.sprite.Sprite):
    """A simple alien sprite."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Try to load an image if provided, otherwise use a rect
        img_path = os.path.join(os.path.dirname(__file__), 'images', 'alien.png')
        if os.path.isfile(img_path):
            try:
                self.image = pygame.image.load(img_path).convert_alpha()
            except Exception:
                self.image = None
        else:
            self.image = None

        if self.image:
            self.rect = self.image.get_rect()
        else:
            self.rect = pygame.Rect(0, 0, 50, 36)

        # Start each new alien near the top-left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien horizontally."""
        self.x += self.settings.alien_speed
        self.rect.x = int(self.x)

    def blitme(self):
        if self.image:
            self.screen.blit(self.image, self.rect)
        else:
            pygame.draw.rect(self.screen, (100, 220, 100), self.rect)
import os
import pygame


class Alien(pygame.sprite.Sprite):
    """A simple alien sprite."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Try to load an image if provided, otherwise use a rect
        img_path = os.path.join(os.path.dirname(__file__), 'images', 'alien.png')
        if os.path.isfile(img_path):
            try:
                self.image = pygame.image.load(img_path).convert_alpha()
            except Exception:
                self.image = None
        else:
            self.image = None

        if self.image:
            self.rect = self.image.get_rect()
        else:
            self.rect = pygame.Rect(0, 0, 50, 36)

        # Start each new alien near the top-left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien horizontally."""
        self.x += self.settings.alien_speed
        self.rect.x = int(self.x)

    def blitme(self):
        if self.image:
            self.screen.blit(self.image, self.rect)
        else:
            pygame.draw.rect(self.screen, (100, 220, 100), self.rect)

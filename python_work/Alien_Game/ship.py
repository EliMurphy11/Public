import os
import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        # Try to load a chicken nugget image, then a ship image;
        # if none are present, draw a nugget-like Surface at runtime.
        self.image = None
        images_dir = os.path.join(os.path.dirname(__file__), 'images')
        chicken_path = os.path.join(images_dir, 'chicken_nugget.png')
        ship_path = os.path.join(images_dir, 'ship.bmp')

        if os.path.isfile(chicken_path):
            try:
                self.image = pygame.image.load(chicken_path).convert_alpha()
            except Exception:
                self.image = None
        elif os.path.isfile(ship_path):
            try:
                self.image = pygame.image.load(ship_path).convert_alpha()
            except Exception:
                self.image = None

        if not self.image:
            # draw a simple chicken-nugget shaped surface
            w, h = 60, 48
            surf = pygame.Surface((w, h), pygame.SRCALPHA)
            # base nugget color
            base = (210, 160, 90)
            # darker spots
            spot = (160, 110, 50)
            # draw base blob (multiple overlapping ellipses)
            pygame.draw.ellipse(surf, base, (2, 6, w-4, h-16))
            pygame.draw.ellipse(surf, base, (6, 0, w-12, h-12))
            # darker texture spots
            pygame.draw.circle(surf, spot, (int(w*0.3), int(h*0.35)), 6)
            pygame.draw.circle(surf, spot, (int(w*0.65), int(h*0.5)), 5)
            pygame.draw.circle(surf, spot, (int(w*0.45), int(h*0.7)), 4)
            self.image = surf

        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = int(self.x)

    def blitme(self):
        """Draw the ship at its current location."""
        if self.image:
            self.screen.blit(self.image, self.rect)
        else:
            pygame.draw.rect(self.screen, (200, 200, 200), self.rect)



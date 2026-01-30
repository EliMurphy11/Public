import os
import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        # Load the ship image
        self.image = self._load_ship_image()
        self.rect = self.image.get_rect() if self.image else None

        if self.image:
            self.rect = self.image.get_rect()
        else:
            # Default ship size if image loading fails
            w, h = 60, 60
            self.rect = pygame.Rect(0, 0, w, h)

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Aim vector (normalized). Default points up.
        self.aim_x = 0.0
        self.aim_y = -1.0
        # Aim control flags (WASD)
        self.aim_up = False
        self.aim_down = False
        self.aim_left = False
        self.aim_right = False

    def _load_ship_image(self):
        """Loads the ship image, handling potential errors."""
        ship_path = os.path.join(os.path.dirname(__file__), 'images', 'chicken_nugget.png')
        try:
            if os.path.isfile(ship_path):
                return pygame.image.load(ship_path).convert_alpha()
            else:
                print(f"Warning: Ship image not found at {ship_path}")
                return None
        except pygame.error as e:
            print(f"Error loading ship image: {e}")
            return None

    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        self._update_aim()

    def _update_aim(self):
        """Update aim based on aim flags."""
        ax = 0.0
        ay = 0.0
        if self.aim_up:
            ay -= 1.0
        if self.aim_down:
            ay += 1.0
        if self.aim_left:
            ax -= 1.0
        if self.aim_right:
            ax += 1.0

        if ax == 0.0 and ay == 0.0:
            return  # Keep previous aim

        mag = (ax * ax + ay * ay) ** 0.5
        if mag != 0:
            self.aim_x = ax / mag
            self.aim_y = ay / mag

    def blitme(self):
        """Draw the ship at its current location."""
        if self.image:
            self.screen.blit(self.image, self.rect)
        else:
            self._draw_default_ship()

    def _draw_default_ship(self):
        """Draws a simple espresso cup icon when no image is available."""
        surf = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        w, h = self.rect.width, self.rect.height
        # saucer
        pygame.draw.ellipse(surf, (200, 170, 120), (w * 0.05, h * 0.65, w * 0.9, h * 0.3))
        # cup body
        cup_rect = pygame.Rect(int(w * 0.2), int(h * 0.25), int(w * 0.6), int(h * 0.45))
        pygame.draw.rect(surf, (120, 60, 20), cup_rect, border_radius=6)
        # foam / crema
        pygame.draw.ellipse(surf, (210, 180, 140), (int(w * 0.25), int(h * 0.28), int(w * 0.5), int(h * 0.25)))
        # handle (simple circle segment)
        handle_center = (int(w * 0.82), int(h * 0.45))
        pygame.draw.circle(surf, (120, 60, 20), handle_center, int(h * 0.13))
        pygame.draw.circle(surf, (0, 0, 0, 0), handle_center, int(h * 0.08))
        self.screen.blit(surf, self.rect)

    def get_rect(self):
        """Return the ship's rect object."""
        return self.rect
    # start each new ship at bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
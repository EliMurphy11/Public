import os
import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        # Try to load an image; fall back to a simple rect if missing
        self.image = None
        ship_path = os.path.join(os.path.dirname(__file__), 'images', 'ship.bmp')
        if os.path.isfile(ship_path):
            try:
                self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'espresso.png')).convert_alpha()
            except Exception:
                self.image = None

        if self.image:
            self.rect = self.image.get_rect()
        else:
            # default ship size
            w, h = 60, 48
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

    def update(self):
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
        # Update aim based on aim flags
        ax = 0.0
        ay = 0.0
        if getattr(self, 'aim_up', False):
            ay -= 1.0
        if getattr(self, 'aim_down', False):
            ay += 1.0
        if getattr(self, 'aim_left', False):
            ax -= 1.0
        if getattr(self, 'aim_right', False):
            ax += 1.0
        if ax == 0.0 and ay == 0.0:
            # keep previous aim
            return
        mag = (ax * ax + ay * ay) ** 0.5
        if mag != 0:
            self.aim_x = ax / mag
            self.aim_y = ay / mag

    def blitme(self):
        if self.image:
            self.screen.blit(self.image, self.rect)
        else:
            # draw a simple espresso cup icon when no image is available
            surf = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
            w, h = self.rect.width, self.rect.height
            # saucer
            pygame.draw.ellipse(surf, (200, 170, 120), (w*0.05, h*0.65, w*0.9, h*0.3))
            # cup body
            cup_rect = pygame.Rect(int(w*0.2), int(h*0.25), int(w*0.6), int(h*0.45))
            pygame.draw.rect(surf, (120, 60, 20), cup_rect, border_radius=6)
            # foam / crema
            pygame.draw.ellipse(surf, (210, 180, 140), (int(w*0.25), int(h*0.28), int(w*0.5), int(h*0.25)))
            # handle (simple circle segment)
            handle_center = (int(w*0.82), int(h*0.45))
            pygame.draw.circle(surf, (120, 60, 20), handle_center, int(h*0.13))
            pygame.draw.circle(surf, (0, 0, 0, 0), handle_center, int(h*0.08))
            self.screen.blit(surf, self.rect)

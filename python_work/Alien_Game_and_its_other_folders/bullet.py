import pygame


class Bullet(pygame.sprite.Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Position and direction: default spawn at ship center
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.center = ai_game.ship.rect.center

        # Keep float position for smooth dt-based motion
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Direction vector (normalized). Force bullets to fire straight upward.
        aim_x = 0.0
        aim_y = -1.0
        # Normalize
        mag = (aim_x * aim_x + aim_y * aim_y) ** 0.5
        if mag == 0:
            mag = 1.0
        # dx/dy expressed in pixels per second
        self.dx = (aim_x / mag) * self.settings.bullet_speed
        self.dy = (aim_y / mag) * self.settings.bullet_speed

    def update(self, dt=0.0):
        # Move by dx/dy (pixels per second scaled by dt seconds)
        self.x += self.dx * dt
    
        

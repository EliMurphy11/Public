import os
import random
import pygame

class Star(pygame.sprite.Sprite):
    """A small star that moves downward and wraps to the top."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        w, h = self.settings.screen_width, self.settings.screen_height
        # Create a small surface for the star (1-3 px)
        size = random.randint(1, 3)
        surf = pygame.Surface((size, size), pygame.SRCALPHA)
        color = (255, 255, 255, random.randint(120, 255))
        pygame.draw.rect(surf, color, surf.get_rect())
        self.image = surf
        self.rect = self.image.get_rect()
        # Random start position
        self.rect.x = random.randrange(0, w)
        self.rect.y = random.randrange(0, h)
        self.y = float(self.rect.y)
        # speed in pixels/second
        self.vy = random.uniform(self.settings.bg_star_speed[0], self.settings.bg_star_speed[1])

    def update(self, dt):
        # dt in seconds
        self.y += self.vy * dt
        if self.y > self.settings.screen_height:
            # wrap to top
            self.y = -self.rect.height
            self.rect.x = random.randrange(0, self.settings.screen_width)
            self.vy = random.uniform(self.settings.bg_star_speed[0], self.settings.bg_star_speed[1])
        self.rect.y = int(self.y)


class Planet(pygame.sprite.Sprite):
    """A larger decorative planet that drifts downward and slightly sideways."""

    def __init__(self, ai_game):
        super().__init__()
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        w, h = self.settings.screen_width, self.settings.screen_height

        # Try to find a planet image; otherwise draw a circle.
        img_candidates = [
            os.path.join(os.path.dirname(__file__), 'images', 'planet1.png'),
            os.path.join(os.getcwd(), 'python_work', 'Alien_Game', 'images', 'planet1.png'),
        ]
        img = None
        for p in img_candidates:
            if os.path.isfile(p):
                try:
                    img = pygame.image.load(p).convert_alpha()
                    break
                except Exception:
                    img = None

        if img:
            # scale to a reasonable size
            scale = random.uniform(0.35, 0.7)
            new_size = (max(20, int(img.get_width() * scale)), max(20, int(img.get_height() * scale)))
            try:
                img = pygame.transform.smoothscale(img, new_size)
            except Exception:
                pass
            self.image = img
        else:
            radius = random.randint(18, 48)
            surf = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
            color = (random.randint(80, 255), random.randint(80, 255), random.randint(80, 255), 220)
            pygame.draw.circle(surf, color, (radius, radius), radius)
            # add a faint ring
            pygame.draw.circle(surf, (255, 255, 255, 30), (radius, radius), radius, 2)
            self.image = surf

        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, w - self.rect.width)
        self.rect.y = random.randrange(-h, 0)
        self.y = float(self.rect.y)
        self.vy = random.uniform(self.settings.bg_planet_speed[0], self.settings.bg_planet_speed[1])
        # slight horizontal drift
        self.vx = random.uniform(-10, 10)

    def update(self, dt):
        self.y += self.vy * dt
        self.rect.x += int(self.vx * dt)
        if self.y > self.settings.screen_height + self.rect.height:
            # respawn at top
            self.rect.x = random.randrange(0, self.settings.screen_width - self.rect.width)
            self.y = random.randrange(-self.settings.screen_height, -self.rect.height)
            self.vy = random.uniform(self.settings.bg_planet_speed[0], self.settings.bg_planet_speed[1])
            self.vx = random.uniform(-10, 10)
        self.rect.y = int(self.y)

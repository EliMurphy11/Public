# create a background for alien.py with planets and stars 
import pygame
import random
#  creatde a background for alien.py with planets and stars
from settings import Settings
class Background:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.stars = pygame.sprite.Group()
        self.planets = pygame.sprite.Group()
        self._create_background()

    def _create_background(self):
        # Create stars
        for _ in range(self.settings.bg_star_count):
            star = Star(self.screen, self.settings)
            self.stars.add(star)

        # Create planets
        for _ in range(self.settings.bg_planet_count):
            planet = Planet(self.screen, self.settings)
            self.planets.add(planet)

    def update(self, dt):
        self.stars.update(dt)
        self.planets.update(dt)

    def draw(self):
        self.stars.draw(self.screen)
        self.planets.draw(self.screen)
class Star(pygame.sprite.Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.speed = random.uniform(*self.settings.bg_star_speed)
        self.image = pygame.Surface((2, 2))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, self.settings.screen_width)
        self.rect.y = random.randrange(0, self.settings.screen_height)
        self.y = float(self.rect.y)

    def update(self, dt):
        self.y += self.speed * dt
        if self.y > self.settings.screen_height:
            self.y = 0
            self.rect.x = random.randrange(0, self.settings.screen_width)
        self.rect.y = int(self.y)
class Planet(pygame.sprite.Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.speed = random.uniform(*self.settings.bg_planet_speed)
        size = random.randint(30, 100)
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        color = random.choice([(200, 100, 100), (100, 200, 100), (100, 100, 200), (200, 200, 100), (200, 100, 200)])
        pygame.draw.circle(self.image, color, (size // 2, size // 2), size // 2)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, self.settings.screen_width - size)
        self.rect.y = random.randrange(0, self.settings.screen_height)
        self.y = float(self.rect.y)

    def update(self, dt):
        self.y += self.speed * dt
        if self.y > self.settings.screen_height:
            self.y = -self.rect.height
            self.rect.x = random.randrange(0, self.settings.screen_width - self.rect.width)
        self.rect.y = int(self.y)
       
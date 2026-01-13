import random
import math
import pygame

class ConfettiParticle(pygame.sprite.Sprite):
    def __init__(self, ai_game, x, y):
        super().__init__()
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        # random small rectangle
        w = random.randint(2, 6)
        h = random.randint(6, 14)
        surf = pygame.Surface((w, h), pygame.SRCALPHA)
        color = random.choice([(255, 30, 30), (40, 200, 60), (40, 120, 255), (255, 200, 30), (200, 80, 200)])
        pygame.draw.rect(surf, color, surf.get_rect())
        self.image = surf
        self.rect = self.image.get_rect(center=(int(x), int(y)))
        # initial velocities (px/sec)
        self.vx = random.uniform(-120, 120)
        self.vy = random.uniform(-260, -80)  # shoot upward
        # angular rotation
        self.angle = random.uniform(0, 360)
        self.angular_v = random.uniform(-180, 180)
        self.spawn_time = pygame.time.get_ticks()

    def update(self, dt):
        # dt in seconds
        # apply gravity
        self.vy += 480 * dt
        self.rect.x += int(self.vx * dt)
        self.rect.y += int(self.vy * dt)
        self.angle += self.angular_v * dt
        # rotate image for visual effect
        try:
            self.rotated = pygame.transform.rotate(self.image, self.angle)
            old_center = self.rect.center
            self.image = self.rotated
            self.rect = self.image.get_rect(center=old_center)
        except Exception:
            pass
        # remove if off-screen bottom
        if self.rect.top > self.settings.screen_height + 50:
            self.kill()


class Trophy(pygame.sprite.Sprite):
    def __init__(self, ai_game, x, y):
        super().__init__()
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        # draw a simple trophy: cup + base
        w = 64
        h = 80
        surf = pygame.Surface((w, h), pygame.SRCALPHA)
        # cup
        pygame.draw.ellipse(surf, (230, 200, 40), (8, 8, w - 16, int(h * 0.5)))
        # stem
        pygame.draw.rect(surf, (200, 160, 30), (w // 2 - 8, int(h * 0.5), 16, int(h * 0.18)))
        # base
        pygame.draw.rect(surf, (100, 80, 30), (w // 4, int(h * 0.7), w // 2, int(h * 0.15)))
        # handles
        pygame.draw.arc(surf, (200, 160, 30), (-8, 4, 36, 40), 3.14 / 2, 3.14, 4)
        pygame.draw.arc(surf, (200, 160, 30), (w - 28, 4, 36, 40), 0, 3.14 / 2, 4)
        self.image = surf
        self.orig_image = surf.copy()
        self.rect = self.image.get_rect(center=(int(x), int(y)))
        # trophy will float up slightly and pulse
        self.vy = -20
        self.t = 0.0

    def update(self, dt):
        self.t += dt
        # float up and down a bit
        self.rect.y += int(self.vy * dt + 6 * math.sin(self.t * 2.0))
        # simple pulse via scaling
        scale = 1.0 + 0.05 * math.sin(self.t * 3.0)
        try:
            nw = max(1, int(self.orig_image.get_width() * scale))
            nh = max(1, int(self.orig_image.get_height() * scale))
            img = pygame.transform.smoothscale(self.orig_image, (nw, nh))
            old_center = self.rect.center
            self.image = img
            self.rect = self.image.get_rect(center=old_center)
        except Exception:
            pass

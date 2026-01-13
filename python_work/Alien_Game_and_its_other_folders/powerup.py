import os
import random
import pygame


class LaserPickup(pygame.sprite.Sprite):
    """A pickup that grants the ship a laser ability when collected."""

    def __init__(self, ai_game, x=None, y=None):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        size = 48
        surf = pygame.Surface((size, size), pygame.SRCALPHA)
        # draw a filled circle with a darker border
        center = (size // 2, size // 2)
        pygame.draw.circle(surf, (255, 200, 40), center, size // 2)
        pygame.draw.circle(surf, (200, 140, 10), center, size // 2, 3)
        # draw centered text 'LASER'
        try:
            font = pygame.font.Font(None, 20)
            txt = font.render('LASER', True, (20, 20, 20))
            txt_rect = txt.get_rect(center=center)
            surf.blit(txt, txt_rect)
        except Exception:
            pass
        self.image = surf
        self.rect = self.image.get_rect()
        if x is None or y is None:
            self.rect.x = random.randrange(50, self.settings.screen_width - 50)
            self.rect.y = random.randrange(50, int(self.settings.screen_height * 0.6))
        else:
            self.rect.center = (int(x), int(y))

    def update(self, dt=None):
        # pickups are static; no update required but keep signature
        return


class LaserBeam(pygame.sprite.Sprite):
    """A beam that can be fired as a fast projectile or held continuously.

    If `persistent` is True the beam is rendered as a long line from the ship
    upwards and follows the ship horizontally until released.
    """

    def __init__(self, ai_game, origin, dir_x, dir_y, persistent=False):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.origin = origin
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.persistent = persistent

        if self.persistent:
            # Long vertical beam that spans from ship up to the top of screen
            ship_x = int(origin[0])
            top_y = 0
            bottom_y = int(origin[1] - 8)
            beam_height = max(8, bottom_y - top_y)
            w = 8
            surf = pygame.Surface((w, beam_height), pygame.SRCALPHA)
            pygame.draw.rect(surf, (255, 40, 40, 220), (0, 0, w, beam_height))
            self.image = surf
            # place so bottom of the beam meets slightly above ship
            self.rect = self.image.get_rect(midbottom=(ship_x, bottom_y))
            self.x = float(self.rect.x)
            self.y = float(self.rect.y)
        else:
            # Short fast projectile beam (single-shot)
            w, h = 6, 28
            surf = pygame.Surface((w, h), pygame.SRCALPHA)
            pygame.draw.rect(surf, (255, 60, 60), (0, 0, w, h))
            try:
                angle = -pygame.math.Vector2(dir_x, dir_y).angle_to((0, -1))
                if abs(angle) > 1e-6:
                    surf = pygame.transform.rotate(surf, angle)
            except Exception:
                pass
            self.image = surf
            self.rect = self.image.get_rect(center=(int(origin[0]), int(origin[1] - 20)))
            self.x = float(self.rect.x)
            self.y = float(self.rect.y)
            self.speed = 900.0
            mag = (dir_x * dir_x + dir_y * dir_y) ** 0.5
            if mag == 0:
                mag = 1.0
            self.vx = (dir_x / mag) * self.speed
            self.vy = (dir_y / mag) * self.speed

        self.spawn_time = pygame.time.get_ticks()
        self.duration = ai_game.settings.laser_beam_duration

    def update(self, dt=0.0):
        if self.persistent:
            # follow ship horizontally so beam moves with player
            try:
                ship_center_x = int(self.origin[0])
                # move rect to keep midbottom aligned with ship x
                self.rect.midbottom = (ship_center_x, self.rect.midbottom[1])
                self.x = float(self.rect.x)
                self.y = float(self.rect.y)
            except Exception:
                pass
        else:
            # move beam along its velocity
            self.x += self.vx * dt
            self.y += self.vy * dt
            self.rect.x = int(self.x)
            self.rect.y = int(self.y)

        # remove if off-screen or expired (for non-persistent) or if persistent but duration exceeded
        if (not self.persistent and (self.rect.bottom < 0 or self.rect.top > self.settings.screen_height)):
            self.kill()
        if pygame.time.get_ticks() - self.spawn_time > self.duration:
            # allow persistent beams to last as long as held; non-persistent still expire
            if not self.persistent:
                self.kill()
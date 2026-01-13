import os
import pygame


class Alien(pygame.sprite.Sprite):
    """A simple alien sprite."""

    # Shared cached image for all Alien instances (load only once)
    _shared_image = None
    _loaded_from = None

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Try multiple candidate image names for a Sabrina Carpenter face
        # and search multiple image directories (local and the two project
        # copies that sometimes contain images). This helps when the image
        # lives in `python_work/Alien_Game/images` or
        # `python_work/Alien_Game_clean/images`.
        filenames = [
            'sabrina_carpenter.png',
            'sabrina.png',
            'sabrina_carpenter_face.png',
            'sabrina_carpenter.webp',
            'sabrina.webp',
            'sabrina_carpenter_face.webp',
            'alien.png',
        ]

        search_dirs = [
            os.path.join(os.path.dirname(__file__), 'images'),
            os.path.join(os.getcwd(), 'python_work', 'Alien_Game', 'images'),
            os.path.join(os.getcwd(), 'python_work', 'Alien_Game_clean', 'images'),
        ]

        # If we've already loaded the image previously, reuse it.
        if Alien._shared_image is None:
            img = None
            loaded_from = None
            for d in search_dirs:
                for name in filenames:
                    img_path = os.path.join(d, name)
                    if os.path.isfile(img_path):
                        try:
                            img = pygame.image.load(img_path).convert_alpha()
                            loaded_from = img_path
                            break
                        except Exception:
                            img = None
                if img:
                    break

            if img:
                try:
                    img = pygame.transform.smoothscale(img, (64, 48))
                except Exception:
                    pass

            Alien._shared_image = img
            Alien._loaded_from = loaded_from
            if loaded_from:
                # Print once so you can verify which file was used.
                print('Alien image loaded from:', loaded_from)

        self.image = Alien._shared_image

        # (Scaling already applied to shared image if present.)

        if self.image:
            self.rect = self.image.get_rect()
        else:
            self.rect = pygame.Rect(0, 0, 50, 36)

        # Starting position values (float) for smooth movement
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Time tracking for per-alien acceleration
        self.spawn_time = pygame.time.get_ticks()
        self.last_update = self.spawn_time
        # Vertical velocity in pixels/second
        self.vy = float(self.settings.alien_speed)

    def update(self):
        """Move the alien downward. The longer it survives, the faster it moves.

        Speeds are treated in pixels/second; use real-time deltas so behavior is
        stable across frame rates.
        """
        now = pygame.time.get_ticks()
        dt = (now - self.last_update) / 1000.0
        if dt <= 0:
            return
        self.last_update = now

        # Increase velocity based on survival time
        survival = (now - self.spawn_time) / 1000.0
        self.vy = float(self.settings.alien_speed) + float(self.settings.alien_acceleration) * survival

        # Move down by vy * dt (pixels). Keep float y for smooth movement.
        self.y += self.vy * dt
        self.rect.y = int(self.y)

    def blitme(self):
        if self.image:
            self.screen.blit(self.image, self.rect)
        else:
            pygame.draw.rect(self.screen, (100, 220, 100), self.rect)

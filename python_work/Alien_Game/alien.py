import sys
import os
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien_sprite import Alien


class AlienInvasion:
    """Minimal Alien Invasion game (original implementation)."""

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.bg_color = self.settings.bg_color

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def _create_fleet(self):
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = min(6, max(1, available_space_x // (alien_width * 2)))

        for alien_number in range(int(number_aliens_x)):
            a = Alien(self)
            a.x = alien_width + 2 * alien_width * alien_number
            a.rect.x = int(a.x)
            a.rect.y = alien.rect.height + 10
            self.aliens.add(a)

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            self.bullets.add(Bullet(self))

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        for alien in self.aliens.sprites():
            alien.blitme()

        pygame.display.flip()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()

            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

            pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

            for alien in self.aliens.sprites():
                alien.update()

            self._update_screen()
            self.clock.tick(60)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
import sys
import os
import pygame

import sys
import os
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien_sprite import Alien


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()

        # load settings
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        # background color
        self.bg_color = self.settings.bg_color

        # ship
        self.ship = Ship(self)

        # sprite groups
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # create a small fleet (for demo, 1 row of 6 aliens)
        self._create_fleet()

    def _create_fleet(self):
        """Create a row of aliens across the top."""
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = min(6, max(1, available_space_x // (alien_width * 2)))

        for alien_number in range(int(number_aliens_x)):
            a = Alien(self)
            a.x = alien_width + 2 * alien_width * alien_number
            a.rect.x = int(a.x)
            a.rect.y = alien.rect.height + 10
            self.aliens.add(a)

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        if self.ship:
            self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        for alien in self.aliens.sprites():
            alien.blitme()

        pygame.display.flip()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()

            # remove bullets that have left the screen
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

            # simple collision: remove bullet and alien on collision
            pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

            # update aliens
            for alien in self.aliens.sprites():
                alien.update()

            self._update_screen()
            self.clock.tick(60)


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
from ship import Ship
from bullet import Bullet
from alien_sprite import Alien


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()

        # load settings
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        # background color
        self.bg_color = self.settings.bg_color

        # ship
        self.ship = Ship(self)

        # sprite groups
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        import sys
        import os
        import pygame

        from settings import Settings
        from ship import Ship
        from bullet import Bullet
        from alien_sprite import Alien


        class AlienInvasion:
            """Overall class to manage game assets and behavior."""

            def __init__(self):
                """Initialize the game and create game resources."""
                pygame.init()
                self.clock = pygame.time.Clock()

                # load settings
                self.settings = Settings()
                self.screen = pygame.display.set_mode(
                    (self.settings.screen_width, self.settings.screen_height)
                )
                pygame.display.set_caption("Alien Invasion")

                # background color
                self.bg_color = self.settings.bg_color

                # ship
                self.ship = Ship(self)

                # sprite groups
                self.bullets = pygame.sprite.Group()
                self.aliens = pygame.sprite.Group()

                # create a small fleet (for demo, 1 row of 6 aliens)
                self._create_fleet()

            def _create_fleet(self):
                """Create a row of aliens across the top."""
                alien = Alien(self)
                alien_width = alien.rect.width
                available_space_x = self.settings.screen_width - (2 * alien_width)
                number_aliens_x = min(6, max(1, available_space_x // (alien_width * 2)))

                for alien_number in range(int(number_aliens_x)):
                    a = Alien(self)
                    a.x = alien_width + 2 * alien_width * alien_number
                    a.rect.x = int(a.x)
                    a.rect.y = alien.rect.height + 10
                    self.aliens.add(a)

            def _fire_bullet(self):
                """Create a new bullet and add it to the bullets group."""
                if len(self.bullets) < self.settings.bullets_allowed:
                    new_bullet = Bullet(self)
                    self.bullets.add(new_bullet)

            def _check_events(self):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            self.ship.moving_right = True
                        elif event.key == pygame.K_LEFT:
                            self.ship.moving_left = True
                        elif event.key == pygame.K_SPACE:
                            self._fire_bullet()
                        elif event.key == pygame.K_q:
                            pygame.quit()
                            sys.exit()
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT:
                            self.ship.moving_right = False
                        elif event.key == pygame.K_LEFT:
                            self.ship.moving_left = False

            def _update_screen(self):
                self.screen.fill(self.bg_color)
                if self.ship:
                    self.ship.blitme()

                for bullet in self.bullets.sprites():
                    bullet.draw_bullet()

                for alien in self.aliens.sprites():
                    alien.blitme()

                pygame.display.flip()

            def run_game(self):
                """Start the main loop for the game."""
                while True:
                    self._check_events()
                    self.ship.update()
                    self.bullets.update()

                    # remove bullets that have left the screen
                    for bullet in self.bullets.copy():
                        if bullet.rect.bottom <= 0:
                            self.bullets.remove(bullet)

                    # simple collision: remove bullet and alien on collision
                    collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

                    # update aliens
                    for alien in self.aliens.sprites():
                        alien.update()

                    self._update_screen()
                    self.clock.tick(60)


        if __name__ == "__main__":
            ai = AlienInvasion()
            ai.run_game()


    def _load_extra_image(self):

    
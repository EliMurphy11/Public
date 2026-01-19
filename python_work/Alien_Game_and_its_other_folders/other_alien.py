import sys
import pygame
import os
import random
from pygame.sprite import Sprite, Group

# --- SETTINGS ---
class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (10, 10, 30)
        self.ship_speed = 5.0
        self.bullet_speed = 7.0
        self.alien_speed = 2.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.ship_limit = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.alien_points = 10

# --- SPRITES ---
class Ship(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load image
        self.image = pygame.image.load('images/espresso.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (75, 75))
        
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self, moving_right, moving_left):
        if moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/sabrina.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
            
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

# --- MAIN GAME ---
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Espresso vs Sabrina")

        self.ship = Ship(self)
        self.aliens = Group()
        self.bullets = Group()
        self.game_active = True
        
        # Movement flags
        self.moving_right = False
        self.moving_left = False
        
        self._create_fleet()

    def _create_fleet(self):
        for row_number in range(3):
            for alien_number in range(10):
                alien = Alien(self)
                alien.x = 80 + 100 * alien_number
                alien.rect.x = alien.x
                alien.rect.y = 80 + 80 * row_number
                self.aliens.add(alien)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

    def _fire_bullet(self):
        if len(self.bullets) < 3:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            print("Alien hit!")

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.moving_left = True
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.moving_left = False

    def run_game(self):
        while True:
            self._check_events()
            
            if self.game_active:
                self.ship.update(self.moving_right, self.moving_left)
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

            # run the game at 60 FPS
            pygame.time.Clock().tick(60)
                

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
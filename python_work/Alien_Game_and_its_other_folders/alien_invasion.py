import sys
import pygame
from settings import Settings
import os
import random
from ship import Ship
from bullet import Bullet
from alien_sprite import Alien
from effects import ConfettiParticle, Trophy
from powerup import LaserPickup, LaserBeam
from high_scores import HighScores


class AlienInvasion:
    
    
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.settings = Settings()
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship

        # Prefer an explicit chicken-nugget ship image if available.
        # Try both the working project and the clean project image locations.
        try:
            nugget_path = os.path.join(os.getcwd(), 'python_work', 'Alien_Game', 'images', 'paxon.jpeg')
            if not os.path.exists(nugget_path):
                nugget_path = os.path.join(os.getcwd(), 'python_work', 'Alien_Game_clean', 'images', 'paxon.jpeg')

            if os.path.exists(nugget_path):
                nugget_img = pygame.image.load(nugget_path).convert_alpha()
                # scale to a sensible in-game size (Ship code commonly uses ~96x64)
                nugget_img = pygame.transform.smoothscale(nugget_img, (80, 50))
                self.ship.image = nugget_img
                self.ship.rect = self.ship.image.get_rect()
                # place ship at the bottom center (same behavior as Ship.blitme / init)
                self.ship.rect.midbottom = (self.settings.screen_width // 2, self.settings.screen_height - 10)
                # keep any numeric x position used by Ship.update()
                if hasattr(self.ship, 'x'):
                    self.ship.x = float(self.ship.rect.x)
        except Exception as e:
            # Don't crash the game if loading fails; keep the original ship image.
            print('Warning: failed to load chicken nugget image:', e)

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        # Background sprites
        self.stars = pygame.sprite.Group()
        self.planets = pygame.sprite.Group()

        # Game state
        self.game_active = True

   

        # Prepare a small ship icon for the HUD (scaled copy of the ship image or a rect)
        hud_w, hud_h = 40, 28
        if self.ship and getattr(self.ship, 'image', None):
            try:
                self.hud_ship_image = pygame.transform.smoothscale(self.ship.image, (hud_w, hud_h))
            except Exception:
                self.hud_ship_image = pygame.Surface((hud_w, hud_h), pygame.SRCALPHA)
                pygame.draw.rect(self.hud_ship_image, (200, 200, 200), self.hud_ship_image.get_rect())
        else:
            self.hud_ship_image = pygame.Surface((hud_w, hud_h), pygame.SRCALPHA)
            pygame.draw.rect(self.hud_ship_image, (150, 200, 200), self.hud_ship_image.get_rect())

        self._create_fleet

     
        # celebration effects
        self.confetti = pygame.sprite.Group()
        self.trophies = pygame.sprite.Group()
        # Laser / pickup state
        self.pickup = None
        self.last_pickup_spawn = pygame.time.get_ticks()
        self.beams = pygame.sprite.Group()
        self.laser_enabled = False
        self.laser_expires_at = 0
        self.last_laser_fire = 0
# Track whether space is held for persistent laser
        self.space_held = False
        # First-life pickup scheduling
        self.first_life_lost_at = None
        self.pickup_scheduled_at = None
        self.pickup_spawned_after_first_life = False
        # End-screen state: message text and timing
        self.end_message = None
        self.end_message_shown_at = None
        # Minimum time (ms) the end screen should be clearly visible
        self.end_message_duration = 5000

        # Score and level system
        self.high_scores = HighScores()
        self.score = 0
        self.level = 1
        self.aliens_killed_this_level = 0
        
        
        self.show_high_scores_screen

    def _create_fleet(self):
        # Create a grid (rows x cols) of aliens. This makes more aliens on
        # screen and gives them vertical spacing. Columns are computed to fit
        # the screen; rows capped to avoid filling the whole screen.
        sample = Alien(self)
        alien_w = sample.rect.width
        alien_h = sample.rect.height

        available_space_x = self.settings.screen_width - (2 * alien_w)
        cols = max(1, available_space_x // (alien_w * 2))
        cols = int(min(10, cols))

        # Vertical space: leave room for the ship at the bottom; start near top
        available_space_y = self.settings.screen_height - (3 * alien_h) - 100
        rows = max(1, available_space_y // (alien_h * 2))
        rows = int(min(5, rows))

        x_offset = alien_w
        y_offset = 20

        for row in range(rows):
            for col in range(cols):
                a = Alien(self)
                a.x = x_offset + 2 * alien_w * col
                a.rect.x = int(a.x)
                a.y = y_offset + (2 * alien_h * row)
                a.rect.y = int(a.y)
                # Ensure per-alien time tracking starts from their placement
                a.spawn_time = pygame.time.get_ticks()
                a.last_update = a.spawn_time
                self.aliens.add(a)

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            self.bullets.add(Bullet(self))

    def show_high_scores_screen(self):
        """Display high scores before game starts."""
        scores = self.high_scores.get_top_scores(10)
        if not scores:
            return  # no high scores yet
        # render high scores text
        lines = ["HIGH SCORES"]
        for i, entry in enumerate(scores, 1):
            lines.append(f"{i}. {entry['initials']:3s} {entry['score']:6d}")
        # show on screen briefly
        self._show_message('\n'.join(lines))
        pygame.time.delay

    def _get_player_initials(self):
        """Show a screen prompting player to enter their initials (3 chars max)."""
        initials = " "
        input_active = True
        cursor_visible = True
        cursor_time = 0
        while input_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        input_active = False
                elif event.key == pygame.K_BACKSPACE:
                        initials = initials[:-1]
                elif len(initials) < 3:
                        # accept letters and numbers
                        char = event.unicode.upper()
                        if char.isalnum():
                            initials += char
cursor_time = 0
cursor_visible = True
            # update cursor blink
cursor_time += 16
if cursor_time > 500:
                cursor_visible = not cursor_visible
                cursor_time = 0
def __init__(self):
    super().__init__()
    # load the screen
    title_font = pygame.font.Font(self.settings.font_name, 56)
    title = title_font.render("ENTER YOUR INITIALS", True, self.settings.text_color)
    title_rect = title.get_rect(center=(self.settings.screen_width // 2, 100))
    # load the full game screen
    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
    self.clock = pygame.time.Clock()
    pygame.mixer.init()  # Initialize the mixer module
    self.settings = Settings()
    self.bg_color = self.settings.bg_color
 # render prompt
    self.screen.fill(self.bg_color)


def _show_leaderboard_with_player(self, player_initials, player_score):
        """Display the leaderboard highlighting where the player ranked."""
        # Find player's rank
        scores = self.high_scores.get_top_scores(10)
        player_rank = None
        for i, entry in enumerate(scores, 1):
            if entry['initials'] == player_initials and entry['score'] == player_score:
                player_rank = i 
        while input_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    input_active = False

            self.screen.fill(self.bg_color)
            title_font = pygame.font.Font(self.settings.font_name, 56)
            title = title_font.render("HIGH SCORES", True, self.settings.text_color)
            title_rect = title.get_rect(center=(self.settings.screen_width // 2, 40))
            self.screen.blit(title, title_rect)

            # leaderboard entries
            entry_font = pygame.font.Font(self.settings.font_name, 36)
            y = 120
            for i, score_entry in enumerate(scores, 1):
                # highlight player's entry in a different color
                if i == player_rank:
                    color = (50, 215,0)  # green for player
                else:
                    color = self.settings.text_color
                text = f"{i:2d}. {score_entry['initials']:3s}  {score_entry['score']:6d}"
                surf = entry_font.render(text, True, color)
                self.screen.blit(surf, (self.settings.screen_width // 2 - 150, y))
                y += 50

            # hint to continue
            hint_font = pygame.font.Font(self.settings.font_name, 28)
            hint = hint_font.render("Press any key to continue", True, self.settings.text_color)
            hint_rect = hint.get_rect(center=(self.settings.screen_width // 2, self.settings.screen_height - 60))
            self.screen.blit(hint, hint_rect)
            pygame.display.flip()
            self.clock.tick(60)

def _level_up(self):
        """Handle level progression: increase difficulty and create new alien fleet."""
        self.level += 1
        self.aliens_killed_this_level = 0
        # increase alien speed for this level
        level_speed_multiplier = 1.0 + (self.level - 1) * 0.3
        self.settings.alien_speed = max(20, int(20 * level_speed_multiplier))
        # create new fleet
        self.aliens.empty()
        self._create_fleet()
        # reset pickup scheduling for next level
        self.first_life_lost_at = None
        self.pickup_scheduled_at = None
        self.pickup_spawned_after_first_life = False
        # Schedule a new pickup for this level (spawn within 1-3 seconds)
        now = pygame.time.get_ticks()
        self.pickup_scheduled_at = now + random.randint(1000, 3000)


def _show_message(self, text):
        """Render a centered message on the screen."""
        surf = self.msg_font.render(text, True, self.settings.text_color)
        rect = surf.get_rect(center=(self.settings.screen_width // 2, self.settings.screen_height // 2))
        self.screen.fill(self.bg_color)
        self.screen.blit(surf, rect)
        pygame.display.flip()

def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Movement keys (arrow keys and WASD)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.ship.moving_left = True
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.ship.moving_up = True
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.ship.moving_down = True

                # Also update aim flags when WASD or arrows are used so diagonal aiming works
                if event.key == pygame.K_w:
                    self.ship.aim_up = True
                if event.key == pygame.K_s:
                    self.ship.aim_down = True
                if event.key == pygame.K_a:
                    self.ship.aim_left = True
                if event.key == pygame.K_d:
                    self.ship.aim_right = True
                if event.key == pygame.K_UP:
                    self.ship.aim_up = True
                if event.key == pygame.K_DOWN:
                    self.ship.aim_down = True
                if event.key == pygame.K_LEFT:
                    self.ship.aim_left = True
                if event.key == pygame.K_RIGHT:
                    self.ship.aim_right = True

                # Fire (space): laser if enabled otherwise a normal bullet
                if event.key == pygame.K_SPACE:
                    now = pygame.time.get_ticks()
                    if self.laser_enabled:
                        # start a persistent laser beam while space is held
                        if not self.space_held:
                            origin = self.ship.rect.center
                            bx, by = 0.0, -1.0
                            beam = LaserBeam(self, origin, bx, by, persistent=True)
                            # store origin reference so beam can follow ship; beam will be killed on KEYUP
                            beam.origin = self.ship.rect.center
                            self.beams.add(beam)
                            self.space_held = True
                    else:
                        # normal bullet fired once on keydown
                        self._fire_bullet()

                # Quit / Restart
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r and not self.game_active:
                    self._restart_game()

            elif event.type == pygame.KEYUP:
                # Movement keys
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.ship.moving_left = False
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.ship.moving_up = False
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.ship.moving_down = False

                # Aim flags
                if event.key == pygame.K_w:
                    self.ship.aim_up = False
                if event.key == pygame.K_s:
                    self.ship.aim_down = False
                if event.key == pygame.K_a:
                    self.ship.aim_left = False
                if event.key == pygame.K_d:
                    self.ship.aim_right = False
                if event.key == pygame.K_UP:
                    self.ship.aim_up = False
                if event.key == pygame.K_DOWN:
                    self.ship.aim_down = False
                if event.key == pygame.K_LEFT:
                    self.ship.aim_left = False
                if event.key == pygame.K_RIGHT:
                    self.ship.aim_right = False

                # On SPACE release, stop persistent laser beams
                if event.key == pygame.K_SPACE:
                    if self.space_held:
                        self.space_held = False
                        for beam in list(self.beams):
                            if getattr(beam, 'persistent', False):
                                beam.kill()

def _spawn_win_effects(self):
        """Spawn confetti and trophies for the win celebration."""
        # spawn a burst of confetti from the center-top area
        cx = self.settings.screen_width // 2
        cy = int(self.settings.screen_height * 0.35)
        for _ in range(120):
            c = ConfettiParticle(self, cx + random.randint(-200, 200), cy + random.randint(-20, 20))
            self.confetti.add(c)

        # spawn 3 trophies across the center
        spacing = 140
        center_x = self.settings.screen_width // 2
        y = int(self.settings.screen_height * 0.5)
        for i in (-1, 0, 1):
            t = Trophy(self, center_x + i * spacing, y)
            self.trophies.add(t)

def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Movement keys (arrow keys and WASD)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.ship.moving_left = True
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.ship.moving_up = True
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.ship.moving_down = True

                # Also update aim flags when WASD or arrows are used so diagonal aiming works
                if event.key == pygame.K_w:
                    self.ship.aim_up = True
                if event.key == pygame.K_s:
                    self.ship.aim_down = True
                if event.key == pygame.K_a:
                    self.ship.aim_left = True
                if event.key == pygame.K_d:
                    self.ship.aim_right = True
                if event.key == pygame.K_UP:
                    self.ship.aim_up = True
                if event.key == pygame.K_DOWN:
                    self.ship.aim_down = True
                if event.key == pygame.K_LEFT:
                    self.ship.aim_left = True
                if event.key == pygame.K_RIGHT:
                    self.ship.aim_right = True

                # Fire (space): laser if enabled otherwise a normal bullet
                if event.key == pygame.K_SPACE:
                    now = pygame.time.get_ticks()
                    if self.laser_enabled:
                        # start a persistent laser beam while space is held
                        if not self.space_held:
                            origin = self.ship.rect.center
                            bx, by = 0.0, -1.0
                            beam = LaserBeam(self, origin, bx, by, persistent=True)
                            # store origin reference so beam can follow ship; beam will be killed on KEYUP
                            beam.origin = self.ship.rect.center
                            self.beams.add(beam)
                            self.space_held = True
                    else:
                        # normal bullet fired once on keydown
                        self._fire_bullet()

                # Quit / Restart
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r and not self.game_active:
                    self._restart_game()

            elif event.type == pygame.KEYUP:
                # Movement keys
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.ship.moving_left = False
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.ship.moving_up = False
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.ship.moving_down = False

                # Aim flags
                if event.key == pygame.K_w:
                    self.ship.aim_up = False
                if event.key == pygame.K_s:
                    self.ship.aim_down = False
                if event.key == pygame.K_a:
                    self.ship.aim_left = False
                if event.key == pygame.K_d:
                    self.ship.aim_right = False
                if event.key == pygame.K_UP:
                    self.ship.aim_up = False
                if event.key == pygame.K_DOWN:
                    self.ship.aim_down = False
                if event.key == pygame.K_LEFT:
                    self.ship.aim_left = False
                if event.key == pygame.K_RIGHT:
                    self.ship.aim_right = False

                # On SPACE release, stop persistent laser beams
                if event.key == pygame.K_SPACE:
                    if self.space_held:
                        self.space_held = False
                        for beam in list(self.beams):
                            if getattr(beam, 'persistent', False):
                                beam.kill()
                        for beam in list(self.beams):
                            if getattr(beam, 'persistent', False):
                                beam.kill()

def _update_screen(self):
        self.screen.fill(self.bg_color)
        # Draw background elements behind everything
        for p in self.planets.sprites():
            p.blit = getattr(p, 'image', None)
            if p.blit:
                self.screen.blit(p.image, p.rect)
        for s in self.stars.sprites():
            self.screen.blit(s.image, s.rect)
        if self.ship:
            self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Draw laser beams (if any)
        for beam in list(self.beams):
            try:
                self.screen.blit(beam.image, beam.rect)
            except Exception:
                pass

        # Draw pickup if present
        if self.pickup:
            try:
                self.screen.blit(self.pickup.image, self.pickup.rect)
            except Exception:
                pass

        for alien in self.aliens.sprites():
            alien.blitme()

        # Draw HUD: small ship icons for lives
        self._draw_lives()

        # Draw score and level
        self._draw_score_and_level()

        # If an end message is set, render an overlay so it's clearly visible
        if self.end_message:
            # semi-transparent overlay
            overlay = pygame.Surface((self.settings.screen_width, self.settings.screen_height), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 160))
            self.screen.blit(overlay, (0, 0))
            # Draw trophies and confetti above the overlay so they're visible
            for t in self.trophies.sprites():
                try:
                    self.screen.blit(t.image, t.rect)
                except Exception:
                    pass
            for c in self.confetti.sprites():
                try:
                    self.screen.blit(c.image, c.rect)
                except Exception:
                    pass

            # Main end message
            lines = [self.end_message]
            # Hint about restart (already included in message) but render smaller line below
            lines.append('Press R to restart or Q to quit')

            for i, line in enumerate(lines):
                font = self.msg_font if i == 0 else self.hud_font
                surf = font.render(line, True, self.settings.text_color)
                rect = surf.get_rect(center=(self.settings.screen_width // 2, self.settings.screen_height // 2 + i * (font.get_linesize() + 6)))
                self.screen.blit(surf, rect)

        pygame.display.flip()

        def run_game(self):
         while True:
            self._check_events()
            # Play background music while game is active
            
            if self.game_active:
                # update background first (pass dt)
                dt = self.clock.get_time() / 1000.0
                for s in self.stars.sprites():
                    s.update(dt)
                for p in self.planets.sprites():
                    p.update(dt)
                # update confetti and trophies if any (shouldn't be during active play,
                # but keep in case effects linger)
                for c in list(self.confetti):
                    c.update(dt)
                for t in list(self.trophies):
                    t.update(dt)

                if self.ship:
                    self.ship.update()
                # update bullets with dt so movement is frame-rate independent
                self.bullets.update(dt)

                for bullet in list(self.bullets):
                    if bullet.rect.bottom <= 0:
                        self.bullets.remove(bullet)

                # Handle bullet collisions with aliens and award points
                hit_aliens = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
                for _ in hit_aliens:
                    self.score += 10
                    self.aliens_killed_this_level += 1

                # Update and handle laser beams (pass dt for consistency)
                self.beams.update(dt)
                # beams destroy aliens they hit and award points
                if self.beams:
                    hit_by_beam = pygame.sprite.groupcollide(self.beams, self.aliens, False, True)
                    for _ in hit_by_beam:
                        self.score += 10
                        self.aliens_killed_this_level += 1

                # Spawn pickups occasionally (if none active)
                now = pygame.time.get_ticks()

                # Spawn pickups when scheduled (either on level-up or first life lost)
                if self.pickup_scheduled_at and not self.pickup:
                    if now >= self.pickup_scheduled_at:
                        # spawn under aliens if possible
                        try:
                            spawn_x = random.randrange(80, self.settings.screen_width - 80)
                            if len(self.aliens) > 0:
                                max_bottom = max(a.rect.bottom for a in self.aliens)
                                # place a bit lower than the alien formation but above the ship
                                spawn_y = min(max_bottom + 60, self.settings.screen_height - 140)
                            else:
                                spawn_y = self.settings.screen_height - 200
                            self.pickup = LaserPickup(self, spawn_x, spawn_y)
                        except Exception:
                            self.pickup = None
                        self.pickup_scheduled_at = None  # clear scheduling after spawn
                        self.pickup_spawned_after_first_life = True

                # Check pickup collection
                if self.pickup and self.pickup.rect.colliderect(self.ship.rect):
                    self.laser_enabled = True
                    self.laser_expires_at = now + self.settings.laser_duration
                    self.pickup = None

                # Disable laser if expired
                if self.laser_enabled and now > self.laser_expires_at:
                    self.laser_enabled = False

                # Update aliens and check for collisions with the ship
                for alien in list(self.aliens):
                    alien.update()
                    if alien.rect.colliderect(self.ship.rect):
                        # Ship hit
                        self._ship_hit(alien)
                    # If any alien reaches the bottom, handle as a life loss
                    elif alien.rect.bottom >= self.settings.screen_height:
                        self._aliens_reach_bottom()
                        break

                # Win condition: all aliens destroyed -> next level
                if not self.aliens:
                    if self.lives > 0:
                        # proceed to next level
                        self._level_up()
                    else:
                        # game over after last life lost
                        self.game_active = False
                        self.end_message = f'GAME OVER - Final Score: {self.score}'
                        self.end_message_shown_at = pygame.time.get_ticks()
                        self._show_message(self.end_message)
                        # prompt for initials and save if qualified
                        if self.high_scores.is_high_score(self.score):
                            initials = self._get_player_initials()
                            self.high_scores.add_score(initials, self.score)
                            self._show_leaderboard_with_player(initials, self.score)
                            self.end_message = f'Score saved! {initials} - {self.score}'


            else:
                # Game inactive: show appropriate message if lives exhausted
                if self.lives <= 0 and not self.end_message:
                    self.end_message = f'GAME OVER - Final Score: {self.score}'
                    self.end_message_shown_at = pygame.time.get_ticks()
                    self._show_message(self.end_message)
                    # prompt for initials and save if qualified
                    if self.high_scores.is_high_score(self.score):
                        initials = self._get_player_initials()
                        self.high_scores.add_score(initials, self.score)
                        self._show_leaderboard_with_player(initials, self.score)

                # If an end_message exists and this was a WIN, update celebration effects
                if self.end_message and 'YOU WIN' in (self.end_message or ''):
                    dt = self.clock.get_time() / 1000.0
                    for c in list(self.confetti):
                        c.update(dt)
                    for t in list(self.trophies):
                        t.update(dt)

            self._update_screen()
            self.clock.tick(60)

def _ship_hit(self, alien):
        """Handle ship being hit by an alien: explosion, lives decrement, reset or game over."""
        # Remove the alien that hit the ship
        try:
            self.aliens.remove(alien)
        except Exception:
            pass

        # Explosion visual: draw a red circle over the ship briefly
        expl_surf = pygame.Surface((self.ship.rect.width * 2, self.ship.rect.height * 2), pygame.SRCALPHA)
        pygame.draw.circle(expl_surf, (255, 100, 0, 220), (expl_surf.get_width() // 2, expl_surf.get_height() // 2), max(self.ship.rect.width, self.ship.rect.height))
        expl_rect = expl_surf.get_rect(center=self.ship.rect.center)
        self.screen.blit(expl_surf, expl_rect)
        pygame.display.flip()
        # short pause so player sees explosion
        pygame.time.delay(500)

        # decrement lives
        self.lives -= 1

        # If this is the first life lost, schedule a pickup within 3 seconds
        if self.first_life_lost_at is None and self.lives == (self.settings.ship_limit - 1):
            now = pygame.time.get_ticks()
            self.first_life_lost_at = now
            # schedule a spawn time somewhere within the next 3 seconds
            self.pickup_scheduled_at = now + random.randint(200, 3000)

        # If this is the first life lost, schedule a pickup within 3 seconds
        if self.first_life_lost_at is None and self.lives == (self.settings.ship_limit - 1):
            now = pygame.time.get_ticks()
            self.first_life_lost_at = now
            # schedule a spawn time somewhere within the next 3 seconds
            self.pickup_scheduled_at = now + random.randint(200, 3000)

        # clear bullets
        self.bullets.empty()
        # clear beams and pickups
        self.beams.empty()
        self.pickup = None
        self.laser_enabled = False

        if self.lives > 0:
            # Reset ship and fleet
            self.ship.rect.midbottom = (self.settings.screen_width // 2, self.settings.screen_height - 10)
            if hasattr(self.ship, 'x'):
                self.ship.x = float(self.ship.rect.x)
            # Recreate a new fleet
            self.aliens.empty()
            self._create_fleet()
        else:
            # No lives left -> game over
            self.game_active = False
            self._stop_background_music()
            self.end_message = 'GAME OVER - Press R to restart or Q to quit'
            self.end_message_shown_at = pygame.time.get_ticks()
            self._show_message(self.end_message)

def _restart_game(self):
        """Restart the game to initial state."""
        # Show a brief countdown so the player can prepare
        for sec in (3, 2, 1):
            self.end_message = f'Restarting in {sec}...'
            self.end_message_shown_at = pygame.time.get_ticks()
            # allow some event processing so OS doesn't mark window as unresponsive
            pygame.event.pump()
            # render and pause
            self._update_screen()
            pygame.time.delay(700)

        # Reset game state
        self.lives = self.settings.ship_limit
        self.score = 0
        self.level = 1
        self.aliens_killed_this_level = 0
        self.bullets.empty()
        self.aliens.empty()
        self.beams.empty()
        self.pickup = None
        self.laser_enabled = False
        self.first_life_lost_at = None
        self.pickup_scheduled_at = None
        self.pickup_spawned_after_first_life = False
        self._create_fleet()
        # Reset ship
        self.ship.rect.midbottom = (self.settings.screen_width // 2, self.settings.screen_height - 10)
        if hasattr(self.ship, 'x'):
            self.ship.x = float(self.ship.rect.x)
        # clear end message and resume
        self.end_message = None
        self.end_message_shown_at = None
        self.game_active = True
        # Restart music
        self._play_background_music()

def _draw_lives(self):
        """Draw small ship icons for remaining lives in the HUD area."""
        pad = 8
        x = 10
        y = 10
        for i in range(max(0, self.lives)):
            self.screen.blit(self.hud_ship_image, (x + i * (self.hud_ship_image.get_width() + pad), y))

def _draw_score_and_level(self):
        """Draw current score and level in the top-right HUD."""
        score_text = self.hud_font.render(f"Score: {self.score}", True, self.settings.text_color)
        level_text = self.hud_font.render(f"Level: {self.level}", True, self.settings.text_color)
        score_rect = score_text.get_rect(topright=(self.settings.screen_width - 10, 10))
        level_rect = level_text.get_rect(topright=(self.settings.screen_width - 10, score_rect.bottom + 5))
        self.screen.blit(score_text, score_rect)
        self.screen.blit(level_text, level_rect)

def _aliens_reach_bottom(self):
        """Handle the case where aliens reach the bottom: explosion, lose a life, reset or game over."""
        # Draw explosions at each alien's position for visual effect
        try:
            for alien in list(self.aliens):
                expl_surf = pygame.Surface((alien.rect.width * 2, alien.rect.height * 2), pygame.SRCALPHA)
                pygame.draw.circle(expl_surf, (255, 80, 0, 220), (expl_surf.get_width() // 2, expl_surf.get_height() // 2), max(alien.rect.width, alien.rect.height))
                expl_rect = expl_surf.get_rect(center=alien.rect.center)
                self.screen.blit(expl_surf, expl_rect)
            pygame.display.flip()
            pygame.time.delay(600)
        except Exception:
            pass

        # decrement lives
        self.lives -= 1

        # clear bullets and aliens
        self.bullets.empty()
        self.aliens.empty()
        self.beams.empty()
        self.pickup = None

        if self.lives > 0:
            # Reset ship and recreate fleet
            self.ship.rect.midbottom = (self.settings.screen_width // 2, self.settings.screen_height - 10)
            if hasattr(self.ship, 'x'):
                self.ship.x = float(self.ship.rect.x)
            self._create_fleet()
        else:
            # Game over
            self.game_active = False
            self.end_message = 'GAME OVER - Press R to restart or Q to quit'
            self.end_message_shown_at = pygame.time.get_ticks()
            self._show_message(self.end_message)
def _draw_score_and_level(self):
        """Draw current score and level in the top-right HUD."""
        score_text = self.hud_font.render(f"Score: {self.score}", True, self.settings.text_color)
        level_text = self.hud_font.render(f"Level: {self.level}", True, self.settings.text_color)
        score_rect = score_text.get_rect(topright=(self.settings.screen_width - 10, 10))
        level_rect = level_text.get_rect(topright=(self.settings.screen_width - 10, score_rect.bottom + 5))
        self.screen.blit(score_text, score_rect)
        self.screen.blit(level_text, level_rect)

def _aliens_reach_bottom(self):

        """Handle the case where aliens reach the bottom: explosion, lose a life, reset or game over."""
        # Draw explosions at each alien's position for visual effect
        try:
            for alien in list(self.aliens):
                expl_surf = pygame.Surface((alien.rect.width * 2, alien.rect.height * 2), pygame.SRCALPHA)
                pygame.draw.circle(expl_surf, (255, 80, 0, 220), (expl_surf.get_width() // 2, expl_surf.get_height() // 2), max(alien.rect.width, alien.rect.height))
                expl_rect = expl_surf.get_rect(center=alien.rect.center)
                self.screen.blit(expl_surf, expl_rect)
            pygame.display.flip()
            pygame.time.delay(600)
        except Exception:
            pass

        # decrement lives
        self.lives -= 1

        # clear bullets and aliens
        self.bullets.empty()
        self.aliens.empty()
        self.beams.empty()
        self.pickup = None
        # run an instance of the game
        if self.lives > 0:
            # Reset ship and recreate fleet
            self.ship.rect.midbottom = (self.settings.screen_width // 2, self.settings.screen_height - 10)
            if hasattr(self.ship, 'x'):
                self.ship.x = float(self.ship.rect.x)
            self._create_fleet()
        else:
            # Game over
            self.game_active = False
            self.end_message = 'GAME OVER - Press R to restart or Q to quit'
            self.end_message_shown_at = pygame.time.get_ticks()
            self._show_message(self.end_message)
def _get_player_initials(self):
        """Prompt the player to enter their initials for high score recording."""
        initials = ""
        input_active = True
        cursor_time = 0
        cursor_visible = True

        while input_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if initials:
                            input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        initials = initials[:-1]
                    else:
                        char = event.unicode.upper()
                        if char.isalnum():
                            initials += char

            # update cursor blink
            cursor_time += 16
            if cursor_time > 500:
                cursor_visible = not cursor_visible
                cursor_time = 0

            # render prompt
            self.screen.fill(self.bg_color)
            title_font = pygame.font.Font(self.settings.font_name, 56)
            title = title_font.render("ENTER YOUR INITIALS", True, self.settings.text_color)
            title_rect = title.get_rect(center=(self.settings.screen_width // 2, 100))
            self.screen.blit(title, title_rect)

            entry_font = pygame.font.Font(self.settings.font_name, 48)
            entry_text = initials + ("|" if cursor_visible else "")
            entry_surf = entry_font.render(entry_text, True, self.settings.text_color)
            entry_rect = entry_surf.get_rect(center=(self.settings.screen_width // 2, 200))
            self.screen.blit(entry_surf, entry_rect)

            pygame.display.flip()
            self.clock.tick(60)

        return initials
def _show_leaderboard_with_player(self, initials, score):
        """Display the leaderboard with the player's entry highlighted."""
        scores = self.high_scores.get_scores()
        player_rank = None
        for i, entry in enumerate(scores, 1):
            if entry['initials'] == initials and entry['score'] == score:
                player_rank = i
                break

        showing = True
        while showing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    showing = False  # exit on any key press

            self.screen.fill(self.bg_color)
            # title
            title_font = pygame.font.Font(self.settings.font_name, 64)
            title = title_font.render("LEADERBOARD", True, self.settings.text_color)
            title_rect = title.get_rect(center=(self.settings.screen_width // 2, 40))
            self.screen.blit(title, title_rect)

            # leaderboard entries
            entry_font = pygame.font.Font(self.settings.font_name, 36)
            y = 120
            for i, score_entry in enumerate(scores, 1):
                # highlight player's entry in a different color
                if i == player_rank:
                    color = (50, 215,0)  # green for player
                else:
                    color = self.settings.text_color
                text = f"{i:2d}. {score_entry['initials']:3s}  {score_entry['score']:6d}"
                surf = entry_font.render(text, True, color)
                self.screen.blit(surf, (self.settings.screen_width // 2 - 150, y))
                y += 50

            # hint to continue
            hint_font = pygame.font.Font(self.settings.font_name, 28)
            hint = hint_font.render("Press any key to continue", True, self.settings.text_color)
            hint_rect = hint.get_rect(center=(self.settings.screen_width // 2, self.settings.screen_height - 60))
            self.screen.blit(hint, hint_rect)
            pygame.display.flip()
            self.clock.tick(60)
       

if __name__ == '__main__':
        ai = AlienInvasion()
        ai.run_game()



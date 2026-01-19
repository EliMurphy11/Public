class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        # Screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (10, 15, 40)

        # Ship
        self.ship_speed = 5

        # Bullet
        self.bullet_speed = 700  # pixels per second for dt-based movement
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 60, 60)
        self.bullets_allowed = 5

        # Alien
        # Base vertical speed in pixels/second and acceleration per second
        self.alien_speed = 20
        self.alien_acceleration = 0.5
        self.alien_drop = 30

        # Game play
        # Number of ships (lives) the player has
        self.ship_limit = 3

        # UI
        self.font_name = None
        self.font_size = 48
        self.text_color = (255, 255, 255)

        # Background (stars & planets)
        self.bg_star_count = 120
        # star speed in pixels per second (min, max)
        self.bg_star_speed = (10, 60)
        # planet count and speed range (slower than stars)
        self.bg_planet_count = 4
        self.bg_planet_speed = (8, 24)

        # Powerups / Laser (times in milliseconds)
        self.pickup_spawn_interval = 10000  # ms between spawn attempts
        self.laser_duration = 8000  # ms laser ability lasts after pickup
        self.laser_beam_duration = 600  # ms a fired beam lasts
        self.laser_cooldown = 500  # ms between laser fires

        # Music
        self.music_path = 'images/background_music.wav'
        self.music_volume = 1.0  # 100% volume (0.0 to 1.0) - MAXIMUM
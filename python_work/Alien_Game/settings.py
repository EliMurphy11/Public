class Settings:
    """A class to store all settings for Alien Invasion."""
class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings (sane defaults)
        self.screen_width = 1200
        self.screen_height = 800
        # Background color (dark navy)
        self.bg_color = (10, 15, 40)

        # Ship settings
        self.ship_speed = 5

        # Bullet settings
        self.bullet_speed = 7
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 60, 60)
        self.bullets_allowed = 5

        # Alien settings (simple)
        self.alien_speed = 1
        self.alien_drop = 30

import pygame.font
from pygame.sprite import Group

class Info():
    """A class to display information."""

    def __init__(self, settings, screen):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score images
        self.timer_count = 0
        self.collision_rate = 0

    def prep_kinetic_energy(self, kin_energy):
        """Turn the score into a rendered image."""
        rounded_energy = int(round(kin_energy, -1))
        energy_str = "Ec = " + "{:,}".format(rounded_energy) + ' u.e.'
        self.energy_image = self.font.render(energy_str, True, self.text_color,
            self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.energy_rect = self.energy_image.get_rect()
        self.energy_rect.right = self.screen_rect.right - 20
        self.energy_rect.top = 20

    def show_energy(self):
        """Draw score to the screen."""
        self.screen.blit(self.energy_image, self.energy_rect)

    def increase_time(self):
        self.timer_count += 1
        self.prep_collisions()
        self.collision_rate = 0

    def prep_time(self):
        """Turn the score into a rendered image."""
        rounded_time = int(round(self.timer_count, 0))
        time_str = "{:,}".format(rounded_time)
        self.time_image = self.font.render(time_str, True, self.text_color,
            self.settings.bg_color)

        # Display the score at the top left of the screen.
        self.time_rect = self.time_image.get_rect()
        self.time_rect.left = self.screen_rect.left + 20
        self.time_rect.top = 20

    def show_time(self):
        """Draw score to the screen."""
        self.screen.blit(self.time_image, self.time_rect)

    def prep_collisions(self):
        """Turn the score into a rendered image."""
        rounded_col = int(round(self.collision_rate, 0))
        col_str = "{:,}".format(rounded_col) + ' colisões/s'
        self.col_image = self.font.render(col_str, True, self.text_color,
            self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.col_rect = self.col_image.get_rect()
        self.col_rect.right = self.screen_rect.right - 20
        self.col_rect.top = 80

    def show_collisions(self):
        """Draw score to the screen."""
        self.screen.blit(self.col_image, self.col_rect)


import pygame.font
from pygame.sprite import Group

class Info():
    """A class to display information."""

    def __init__(self, settings, screen):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        # Font settings for information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial informations
        self.timer_count = 0
        self.collision_rate = 0
        self.volume = (settings.screen_height * settings.screen_width)/10000

    def prep_kinetic_energy(self, kin_energy):
        """Turn the kinetic energy into a rendered image."""
        rounded_energy = int(round(kin_energy, -1))
        energy_str = "Ec = " + "{:,}".format(rounded_energy) + ' u.e.'
        self.energy_image = self.font.render(energy_str, True, self.text_color,
            self.settings.bg_color)

        # Display the energy at the top right of the screen.
        self.energy_rect = self.energy_image.get_rect()
        self.energy_rect.right = self.screen_rect.right - 20
        self.energy_rect.top = 20

    def show_energy(self):
        """Draw energy image to the screen."""
        self.screen.blit(self.energy_image, self.energy_rect)

    def increase_time(self):
        #TODO fix collision rate
        self.timer_count += 1
        self.prep_collisions()
        self.collision_rate = 0

    def prep_time(self):
        """Turn the time into a rendered image."""
        rounded_time = int(round(self.timer_count, 0))
        time_str = "{:,}".format(rounded_time)
        self.time_image = self.font.render(time_str, True, self.text_color,
            self.settings.bg_color)

        # Display the time at the top left of the screen.
        self.time_rect = self.time_image.get_rect()
        self.time_rect.left = self.screen_rect.left + 20
        self.time_rect.top = 20

    def show_time(self):
        """Draw time image to the screen."""
        self.screen.blit(self.time_image, self.time_rect)

    def prep_collisions(self):
        """Turn the collision rate into a rendered image."""
        rounded_col = int(round(self.collision_rate, 0))
        col_str = "{:,}".format(rounded_col) + ' colisões/s'
        self.col_image = self.font.render(col_str, True, self.text_color,
            self.settings.bg_color)

        # Display the collision rate at the top right of the screen, bellow energy.
        self.col_rect = self.col_image.get_rect()
        self.col_rect.right = self.screen_rect.right - 20
        self.col_rect.top = 80

    def show_collisions(self):
        """Draw collision image to the screen."""
        self.screen.blit(self.col_image, self.col_rect)

    def prep_volume(self):
        """Turn the collision rate into a rendered image."""
        rounded_volume = int(round(self.volume, 0))
        vol_str = "V = " + "{:,}".format(rounded_volume) + ' u.v.'
        self.vol_image = self.font.render(vol_str, True, self.text_color,
            self.settings.bg_color)

        # Display the collision rate at the top right of the screen, bellow collisions.
        self.vol_rect = self.vol_image.get_rect()
        self.vol_rect.right = self.screen_rect.right - 20
        self.vol_rect.top = 140

    def show_volume(self):
        """Draw collision image to the screen."""
        self.screen.blit(self.vol_image, self.vol_rect)

    def prep_num_particles(self, n_par):
        """Turn the kinetic energy into a rendered image."""
        n_par_str = "{:,}".format(n_par) + ' partículas'
        self.n_par_image = self.font.render(n_par_str, True, self.text_color,
            self.settings.bg_color)

        # Display the energy at the top right of the screen.
        self.n_par_rect = self.n_par_image.get_rect()
        self.n_par_rect.right = self.screen_rect.right - 20
        self.n_par_rect.top = 200

    def show_num_particles(self):
        """Draw energy image to the screen."""
        self.screen.blit(self.n_par_image, self.n_par_rect)

    def prep(self, kin_energy, num_particles):
        """Prepares all images from info, besides collisions"""
        self.prep_time()
        self.prep_kinetic_energy(kin_energy)
        self.prep_volume()
        self.prep_num_particles(num_particles)

    def show(self):
        """Shows all info"""
        self.show_energy()
        self.show_collisions()
        self.show_time()
        self.show_volume()
        self.show_num_particles()

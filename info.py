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
        

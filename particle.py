import pygame
from pygame.sprite import Sprite
import random
import math

class Particle(Sprite):
    def __init__(self, settings, screen):
        """Initialize the alien, and set its starting position."""
        super(Particle, self).__init__()
        self.screen = screen
        self.vel_x = random.random() * 20.0
        self.vel_y = random.random() * 20.0
        self.mass = 1

        # Load the alien image, and set its rect attribute.
        self.image = pygame.Surface(settings.particle_size)
        self.image.fill(settings.bg_color)
        pygame.draw.circle(self.image, (0, 0, 255), settings.particle_size, 25, 0)
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = random.randint(0,settings.screen_width)
        self.rect.y = random.randint(0,settings.screen_height)

        # Store the alien's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges_hor(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            self.rect.right = screen_rect.right
            return True
        elif self.rect.left <= 0:
            self.rect.right = screen_rect.right
            return True
        else:
            return False

    def check_edges_ver(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.top <= screen_rect.top:
            self.rect.top = screen_rect.top
            return True
            
        elif self.rect.bottom > screen_rect.bottom:
            self.rect.bottom = screen_rect.bottom
            return True
        else:
            return False

    def update(self):
        if self.check_edges_ver():
            self.vel_y *= -1
        if self.check_edges_hor():
            self.vel_x *= -1

        self.x += self.vel_x
        self.y += self.vel_y

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def color_speed(self):
        self.image.fill((230, 230, 230))
        pygame.draw.circle(self.image, (0, 0, 255), (25, 25), 25, 0)
    
    def kinetic_energy(self):
        return 0.5*self.mass*(math.pow(self.vel_x,2) + math.pow(self.vel_y,2))

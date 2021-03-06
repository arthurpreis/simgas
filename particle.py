import pygame
from pygame.sprite import Sprite
import random
import math

class Particle(Sprite):
    def __init__(self, settings, screen, wall):
        """Initialize the particle, and set its starting position."""
        super(Particle, self).__init__()
        self.screen = screen
        self.vel_x = random.random() * settings.initial_speed
        self.vel_y = random.random() * settings.initial_speed
        self.mass = 1

        # Draw the circle
        self.image = pygame.Surface(settings.particle_size)
        self.image.fill(settings.bg_color)
        pygame.draw.circle(self.image, (0, 0, 255), settings.particle_pos, settings.particle_radius, 0) #TODO: fix circle
        self.rect = self.image.get_rect()

        # Start each new particle near the top left of the screen.
        self.rect.x = random.randint(wall.rect.right, settings.screen_width)
        self.rect.y = random.randint(0,settings.screen_height)

        # Store the particle's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Used by collision counter
        self.collision = False

    def check_edges_hor(self):
        """Return True if particle is at edge of screen (right or left)."""
        screen_rect = self.screen.get_rect()
        if self.rect.right > screen_rect.right:
            self.rect.right = screen_rect.right
            self.vel_x = (-1)*abs(self.vel_x) #bodge
            self.collision = True
            return True
        elif self.rect.left < screen_rect.left:
            self.rect.left = screen_rect.left
            self.vel_x = abs(self.vel_x)
            self.collision = True
            return True
        else:
            return False

    def check_edges_ver(self):
        """Return True if particle is at edge of screen (top or bottom)."""
        screen_rect = self.screen.get_rect()
        if self.rect.top < screen_rect.top:
            self.rect.top = screen_rect.top
            self.vel_y = abs(self.vel_y)
            self.collision = True
            return True

        elif self.rect.bottom > screen_rect.bottom:
            self.rect.bottom = screen_rect.bottom
            self.vel_y = (-1)*abs(self.vel_y)
            return True
            self.collision = True
        else:
            return False

    def check_wall(self, wall):
        if self.rect.left <= wall.rect.right:
            self.rect.x = wall.rect.right
            self.vel_x = abs(self.vel_x)
            self.collision = True
            return True
        else:
            return False

    def update(self, wall):
        if self.check_wall(wall):
            pass

        if self.check_edges_ver():
            pass

        if self.check_edges_hor():
            pass

        self.x += self.vel_x
        self.y += self.vel_y

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the particle at its current location."""
        self.screen.blit(self.image, self.rect)

    def kinetic_energy(self):
        return 0.5*self.mass*(math.pow(self.vel_x,2) + math.pow(self.vel_y,2))

import pygame
from pygame.sprite import Sprite
import random
import math

class Wall(Sprite):
    def __init__(self, settings, screen):
        """Initialize the particle, and set its starting position."""
        super(Wall, self).__init__()
        self.screen = screen
        screen_rect = self.screen.get_rect()


        self.image = pygame.Surface(settings.wall_size)
        self.image.fill(settings.bg_color)
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (50,50,50), self.rect, 0)


        self.rect.left = screen_rect.left
        self.rect.bottom = screen_rect.bottom


        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the particle at its current location."""
        self.screen.blit(self.image, self.rect)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

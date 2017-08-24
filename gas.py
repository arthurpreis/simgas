import pygame

from pygame.sprite import Sprite
from pygame.sprite import Group

class Particle(Sprite):
    def __init__(self, screen):
        """Initialize the alien, and set its starting position."""
        super(Particle, self).__init__()
        self.screen = screen
        self.vel_x = 1
        self.vel_y = 1

        # Load the alien image, and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)
        
    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    def update(self):
        """Move the alien right or left."""
        self.x += self.vel_x
        self.y += self.vel_y
        
        self.rect.x = self.x
        self.rect.y = self.y
        
    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

def create_gas():
    particle = Particle(screen)
    number_particles = 10
    # Create the fleet of aliens.
    for number in range(number_particles):
        create_particle(screen, particles, number)
                
def create_particle(screen, particles, number):
    """Create an alien, and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def __main__():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    particles = Group()
    
    while True:
        
        screen.fill((230,230,230))
        pygame.display.flip()

__main__()

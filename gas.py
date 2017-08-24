import pygame
import random
from pygame.sprite import Sprite
from pygame.sprite import Group
from particle import Particle


def create_gas(screen, particles, number_particles):
    particle = Particle(screen)
    for number in range(number_particles):
        create_particle(screen, particles, number)

def create_particle(screen, particles, number):
    """Create an alien, and place it in the row."""
    particle = Particle(screen)
    particles.add(particle)

def check_keydown_events(event, screen, particles):
    """Respond to keypresses."""
    if event.key == pygame.K_UP:
        change_speed(particles, increase = True)
    elif event.key == pygame.K_DOWN:
        change_speed(particles, increase = False)
    elif event.key == pygame.K_q:
        sys.exit()

def change_speed(particles, increase = True):
    for particle in particles:
        if increase:
            particle.vel_x *= (1.0 + random.random())
            particle.vel_y *= (1.0 + random.random())
        else:
            particle.vel_x *= (1.0 - random.random())
            particle.vel_y *= (1.0 - random.random())

def check_events(screen, particles):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen, particles)

def __main__():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1200,800))
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    particles = Group()
    create_gas(screen, particles, 10)
    speed_increment = False
    speed_decrement = False

    keepGoing = True
    while keepGoing:
        clock.tick(30)
        check_events(screen, particles)
        particles.clear(screen, background)
        particles.update()
        particles.draw(screen)
        pygame.display.flip()

__main__()

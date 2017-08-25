import pygame
import random
import sys
import math
from pygame.sprite import Sprite
from pygame.sprite import Group
from particle import Particle
from settings import Settings
from info import Info

def create_gas(settings, screen, particles, number_particles):
    for number in range(number_particles):
        create_particle(settings, screen, particles, number)

def create_particle(settings, screen, particles, number):
    particle = Particle(settings, screen)
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen, particles)

def avg_speed(particles):
    s = 0
    for particle in particles:
        s += math.abs(particle.vel_x) + math.abs(particle.vel_y)
    return s
    
def total_kinetic_energy(particles):
    s = 0
    for particle in particles:
        s += particle.kinetic_energy()
    return s
    
if __name__ == "__main__":
    settings = Settings()

    pygame.init()
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    
    info = Info(settings, screen)
    background = pygame.Surface(screen.get_size())
    background.fill(settings.bg_color)
    screen.blit(background, (0, 0))
    particles = Group()
    create_gas(settings, screen, particles, 10)
    
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        check_events(screen, particles)
        particles.clear(screen, background)
        particles.update()
        screen.fill(settings.bg_color)
        particles.draw(screen)
        info.prep_kinetic_energy(total_kinetic_energy(particles))
        info.show_energy()
        pygame.display.flip()
        
__main__()

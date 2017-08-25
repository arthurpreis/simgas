import pygame
import random
import sys
import math
from pygame.sprite import Sprite
from pygame.sprite import Group
from particle import Particle
from settings import Settings
from info import Info

def create_gas(settings, screen, particles):
    for number in range(settings.number_particles):
        create_particle(settings, screen, particles, number)

def create_particle(settings, screen, particles, number):
    particle = Particle(settings, screen)
    particles.add(particle)

def check_keydown_events(event, settings, screen, particles):
    """Respond to keypresses."""
    if event.key == pygame.K_UP:
        change_speed(particles, settings, increase = True)
    elif event.key == pygame.K_DOWN:
        change_speed(particles, settings, increase = False)
    elif event.key == pygame.K_q:
        sys.exit()

def change_speed(particles, settings, increase = True):
    for particle in particles:
        if increase:
            if abs(particle.vel_x) <= settings.max_speed:
                particle.vel_x *= (1.0 + random.random())
            if abs(particle.vel_y) <= settings.max_speed:
                particle.vel_y *= (1.0 + random.random())
        else:
            particle.vel_x *= (1.0 - random.random())
            particle.vel_y *= (1.0 - random.random())

def check_events(screen, settings, particles, info):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, particles)
        elif event.type == pygame.USEREVENT + 1:
            info.increase_time()
            pygame.time.set_timer(pygame.USEREVENT + 1, 1000)

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
    create_gas(settings, screen, particles)
    pygame.time.set_timer(pygame.USEREVENT + 1, 1000)
    info.prep_collisions()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        check_events(screen, settings, particles, info)
        particles.clear(screen, background)
        for particle in particles:
            particle.update()
            if particle.collision:
                info.collision_rate += 1
                particle.collsion = False

        screen.fill(settings.bg_color)
        particles.draw(screen)
        info.prep_time()
       # info.prep_collisions()
        info.prep_kinetic_energy(total_kinetic_energy(particles))
        info.show_energy()
        info.show_collisions()
        info.show_time()
        pygame.display.flip()

__main__()

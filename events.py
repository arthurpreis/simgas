import pygame
import random
import sys
from particle import Particle

def create_gas(settings, screen, particles):
    """Creates collections of particles"""
    for number in range(settings.number_particles):
        create_particle(settings, screen, particles, number)

def create_particle(settings, screen, particles, number):
    """Create particle and adds it to collection"""
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
    """Increases or decreases energy of all particles, depending on input"""
    for particle in particles:
        if increase:
            if abs(particle.vel_x) <= settings.max_speed:
                particle.vel_x *= (1.0 + random.random()) #TODO change distribution
            if abs(particle.vel_y) <= settings.max_speed:
                particle.vel_y *= (1.0 + random.random())
        else:
            particle.vel_x *= (1.0 - random.random())
            particle.vel_y *= (1.0 - random.random())

def check_events(screen, settings, particles, info):
    """check keystrokes and timer"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, particles)
        elif event.type == pygame.USEREVENT + 1:
            info.increase_time()
            pygame.time.set_timer(pygame.USEREVENT + 1, 1000)

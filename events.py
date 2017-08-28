import pygame
import random
import sys
from particle import Particle

def create_gas(settings, screen, particles, wall):
    """Creates collections of particles"""
    for number in range(settings.number_particles):
        create_particle(settings, screen, particles, wall)

def create_particle(settings, screen, particles, wall):
    """Create particle and adds it to collection"""
    particle = Particle(settings, screen, wall)
    particles.add(particle)

def check_keydown_events(event, settings, screen, particles, wall):
    """Respond to keypresses."""
    if event.key == pygame.K_UP:
        change_speed(particles, settings, increase = True)
    elif event.key == pygame.K_DOWN:
        change_speed(particles, settings, increase = False)
    elif event.key == pygame.K_RIGHT:
        move_wall(wall, screen, settings, particles, direction = 'right')
    elif event.key == pygame.K_LEFT:
        move_wall(wall, screen, settings, particles, direction = 'left')
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_m:
        create_particle(settings, screen, particles, wall)
    elif event.key == pygame.K_n:
        remove_particle(particles)

def change_speed(particles, settings, increase = True):
    """Increases or decreases energy of all particles, depending on input"""
    for particle in particles:
        if increase:
            if abs(particle.vel_x) <= settings.max_speed:
                particle.vel_x *= (1.5 + random.random())
            if abs(particle.vel_y) <= settings.max_speed:
                particle.vel_y *= (1.5 + random.random())
        else:
            particle.vel_x *= random.random()
            particle.vel_y *= random.random()

def check_events(screen, settings, particles, info, wall):
    """check keystrokes and timer"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, particles, wall)
        elif event.type == pygame.USEREVENT + 1:
            info.increase_time()
            pygame.time.set_timer(pygame.USEREVENT + 1, 1000)

def remove_particle(particles):
    for particle in particles:
        particles.remove(particle) #bodge
        break

def move_wall(wall, screen, settings, particles, direction = 'right'):
    screen_rect = screen.get_rect()
    if direction == 'right':
        if wall.rect.right < screen_rect.right:
            wall.rect.right += settings.wall_speed
    else:
        if wall.rect.left > screen_rect.left:
            wall.rect.right -= settings.wall_speed
    for particle in particles:
        particle.update(wall)

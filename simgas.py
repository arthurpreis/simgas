#  simgas.py
#
#MIT License

#Copyright (c) [2017] [Arthur Reis]

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import pygame
import random
import sys
import events
from pygame.sprite import Group
from pygame.sprite import Sprite
from info import Info
from particle import Particle
from settings import Settings

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
    #Init
    pygame.init()
    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    background = pygame.Surface(screen.get_size())

    particles = Group()
    events.create_gas(settings, screen, particles)

    #Sets clock (used for fixed FPS) and timer (used to count collision rate)
    clock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT + 1, 1000)

    info = Info(settings, screen)
    info.prep_collisions()

    keepGoing = True
    while keepGoing:
        clock.tick(30) #30 FPS

        events.check_events(screen, settings, particles, info)
        particles.clear(screen, background)

        for particle in particles:
            particle.update() #updates vel and pos
            if particle.collision:
                info.collision_rate += 1
                particle.collision = False

        screen.fill(settings.bg_color) #cleans screen
        particles.draw(screen)

        info.prep(total_kinetic_energy(particles))
        info.show()

        pygame.display.flip()

__main__()

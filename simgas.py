#  simgas.py
#
#  Copyright 2017 arthur <arthur@DESKTOP-E0CE8BM>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

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

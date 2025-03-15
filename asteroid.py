import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if ASTEROID_MIN_RADIUS >= self.radius:
            return
        else:
            random_angle = random.uniform(20, 50)
            chunk1_velocity = self.velocity.rotate(random_angle)
            chunk2_velocity = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            chunk1 = Asteroid(self.position.x, self.position.y, new_radius)
            chunk2 = Asteroid(self.position.x, self.position.y, new_radius)
            chunk1.velocity = chunk1_velocity * 1.2
            chunk2.velocity = chunk2_velocity * 1.2

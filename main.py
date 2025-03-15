# this allows us to use code from
# the open-source library
# throughout the file

import pygame
import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from constants import *
from shot import Shot

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(x, y)
    asteroid_field = AsteroidField()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    init_check = pygame.get_init()
    print(f"Pygame is currently initialized: {init_check}")

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        
        for member in drawable:
            member.draw(screen)
        
        dt = clock.tick(60) / 1000
        updatable.update(dt)

        for member in asteroids:
            if player.detect_collision(member):
                print("Game over!")
                sys.exit()


        pygame.display.flip()

if __name__ == "__main__":
    main()

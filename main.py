# this allows us to use code from
# the open-source library
# throughout the file

import pygame
from player import *
from constants import *

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x, y)

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
        player.draw(screen)
        dt = clock.tick(60) / 1000

        pygame.display.flip()

if __name__ == "__main__":
    main()

import pygame
from ship import Ship
import math

WIDTH = 800
HEIGHT = 600
TARGET_FPS = 60


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Asteroids")

    ship1 = Ship(screen, 300, 300, 0.8, 30)

    clock = pygame.time.Clock()
    running = True
    dt = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        ship1.update(dt)
        ship1.draw()

        pygame.display.flip()

        dt = clock.tick(60) / 1000.0

    pygame.quit()


if __name__ == "__main__":
    main()

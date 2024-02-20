import pygame
from ship import Ship
from asteroid import Asteroid

WIDTH = 800
HEIGHT = 600
TARGET_FPS = 60


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Asteroids")

    ship1 = Ship(screen, WIDTH / 2, HEIGHT / 2, 0.8, 30)
    astr = Asteroid(screen, 0, 0, 1, 120, 50)

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

        astr.update(dt)
        astr.draw()

        pygame.display.flip()

        dt = clock.tick(60) / 1000.0

    pygame.quit()


if __name__ == "__main__":
    main()

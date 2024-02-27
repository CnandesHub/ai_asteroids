import pygame
from ship import Ship
from asteroid import Asteroid
from collision_check import CollisionEntityCheck

WIDTH = 800
HEIGHT = 600
TARGET_FPS = 60


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Asteroids")

    # ship1 = Ship(screen, WIDTH / 2, HEIGHT / 2, 30, 1.5)
    ship1 = Ship(screen, WIDTH / 2, HEIGHT / 2, 30, 1.5, control_type="AI")
    ship2 = Ship(screen, WIDTH / 2, HEIGHT / 2, 30, 1.5, control_type="AI")

    astr = Asteroid(screen=screen, x=0, y=0, radius=80, speed=0.5, angle=1.35)
    astr2 = Asteroid(screen=screen, x=200, y=200, radius=45, speed=0, angle=1.35)

    clock = pygame.time.Clock()
    running = True
    dt = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        astr.update(dt)
        astr.draw()
        astr2.update(dt)
        astr2.draw()
        ship1.update([astr, astr2], dt)
        ship1.draw()
        ship2.update([astr, astr2], dt)
        ship2.draw()

        # if CollisionEntityCheck.check_collision(ship1, astr):
        #     print("Collision detected")

        pygame.display.flip()

        dt = clock.tick(60) / 1000.0

    pygame.quit()


if __name__ == "__main__":
    main()

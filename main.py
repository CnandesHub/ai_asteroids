import pygame
import random
from ship import Ship
from asteroid import Asteroid
from collision_check import CollisionEntityCheck

WIDTH = 1080
HEIGHT = 720
TARGET_FPS = 60

asteroid_stages = [
    {"speed": 2, "radius": 30},
    {"speed": 1.5, "radius": 50},
    {"speed": 1, "radius": 80},
    {"speed": 0.5, "radius": 100},
]


def main(num_asteroids, num_ships):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Asteroids")

    ships = [
        Ship(screen, WIDTH / 2, HEIGHT / 2, 30, 1.5, control_type="AI")
        for _ in range(num_ships)
    ]

    asteroids = []
    for _ in range(num_asteroids):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        stage = random.choice(asteroid_stages)
        speed = stage["speed"]
        radius = stage["radius"]
        angle = random.uniform(0, 2 * 3.14159)
        asteroids.append(
            Asteroid(screen=screen, x=x, y=y, radius=radius, speed=speed, angle=angle)
        )

    clock = pygame.time.Clock()
    running = True
    dt = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        for asteroid in asteroids:
            asteroid.update(dt)
            asteroid.draw()

        for ship in ships:
            ship.update(asteroids, dt)
            ship.draw()

        pygame.display.flip()

        dt = clock.tick(60) / 1000.0

    pygame.quit()


if __name__ == "__main__":
    num_asteroids = 6  # Specify number of asteroids
    num_ships = 10  # Specify number of ships
    main(num_asteroids, num_ships)

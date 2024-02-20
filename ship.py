from entity import Entity
import pygame
import math


class Ship(Entity):
    TURN_SPEED = 10

    def __init__(self, screen, x, y, radius, acceleration):
        super().__init__(screen, x, y, radius)
        self.acceleration = acceleration
        self.SCREEN_WIDTH = screen.get_width()
        self.SCREEN_HEIGHT = screen.get_height()
        self.max_speed = 10

    def update(self, dt):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.speed_x += math.cos(self.angle) * self.acceleration * dt
            self.speed_y += math.sin(self.angle) * self.acceleration * dt
        if keys[pygame.K_s]:
            self.speed_x -= math.cos(self.angle) * self.acceleration * dt
            self.speed_y -= math.sin(self.angle) * self.acceleration * dt
        if keys[pygame.K_d]:
            self.angle += self.TURN_SPEED * dt
        if keys[pygame.K_a]:
            self.angle -= self.TURN_SPEED * dt

        self.angle %= 2 * math.pi
        hipotenusa = math.sqrt(self.speed_x**2 + self.speed_y**2)
        if hipotenusa > self.max_speed:
            self.speed_x = self.speed_x / hipotenusa * self.max_speed
            self.speed_y = self.speed_y / hipotenusa * self.max_speed

        dx = self.speed_x * dt * self.TARGET_FPS
        dy = self.speed_y * dt * self.TARGET_FPS
        self.x += dx
        self.y += dy
        self.x %= self.SCREEN_WIDTH
        self.y %= self.SCREEN_HEIGHT

    def calculate_points(self):
        """
        Calculate the points of the ship's shape.

        Returns:
            A list of points defining the ship's shape.
        """
        return [
            (self.x, self.y - self.radius),
            (self.x - self.radius, self.y + self.radius),
            (self.x + self.radius, self.y + self.radius),
        ]

    def draw(self):
        # points = self.calculate_points()
        # pygame.draw.polygon(self.screen, (255, 255, 255), points)

        for y in range(-1, 2):
            for x in range(-1, 2):
                offset_x = x * self.SCREEN_WIDTH
                offset_y = y * self.SCREEN_HEIGHT

                circle_center = (self.x + offset_x, self.y + offset_y)
                pygame.draw.circle(self.screen, (255, 0, 0), circle_center, self.radius)

                ship_circle_distance = 20
                pygame.draw.circle(
                    self.screen,
                    (0, 255, 255),
                    (
                        self.x + offset_x + math.cos(self.angle) * ship_circle_distance,
                        self.y + offset_y + math.sin(self.angle) * ship_circle_distance,
                    ),
                    5,
                )

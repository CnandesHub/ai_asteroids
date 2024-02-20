from entity import Entity
import pygame
import math


class Ship(Entity):
    TURN_SPEED = 10

    def __init__(self, screen, x, y, acceleration, size=20):
        super().__init__(screen, x, y)
        self.acceleration = acceleration
        self.size = size
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
        if math.sqrt(self.speed_x**2 + self.speed_y**2) > self.max_speed:
            self.speed_x = (
                self.speed_x
                / math.sqrt(self.speed_x**2 + self.speed_y**2)
                * self.max_speed
            )
            self.speed_y = (
                self.speed_y
                / math.sqrt(self.speed_x**2 + self.speed_y**2)
                * self.max_speed
            )

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
            (self.x, self.y - self.size),
            (self.x - self.size, self.y + self.size),
            (self.x + self.size, self.y + self.size),
        ]

    def draw(self):
        # points = self.calculate_points()
        # pygame.draw.polygon(self.screen, (255, 255, 255), points)

        # Draw a circle
        circle_center = (self.x, self.y)
        circle_radius = self.size
        pygame.draw.circle(self.screen, (255, 0, 0), circle_center, circle_radius)

        ship_circle_distance = 20
        pygame.draw.circle(
            self.screen,
            (0, 255, 255),
            (
                self.x + math.cos(self.angle) * ship_circle_distance,
                self.y + math.sin(self.angle) * ship_circle_distance,
            ),
            5,
        )

        font = pygame.font.Font(None, 36)
        text = f"Vel_x:{self.speed_x:.2f} Vel_y:{self.speed_y:.2f} Acc:{self.acceleration} Angle:{self.angle:.2f}"
        text_surface = font.render(text, True, (255, 255, 255))
        self.screen.blit(text_surface, (0, 0))

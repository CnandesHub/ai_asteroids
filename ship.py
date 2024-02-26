from entity import Entity
import pygame
import math
from sensor import Sensor
from neural_net import NeuralNetwork
from controls import Controls


class Ship(Entity):
    TURN_SPEED = 10

    def __init__(self, screen, x, y, radius, acceleration, control_type="Player"):
        super().__init__(screen, x, y, radius)
        self.acceleration = acceleration
        self.SCREEN_WIDTH = screen.get_width()
        self.SCREEN_HEIGHT = screen.get_height()
        self.max_speed = 10
        self.sensor = Sensor(self)
        self.use_brain = control_type == "AI"

        if self.use_brain:
            self.brain = NeuralNetwork(self.sensor.ray_count)

        self.controls = Controls()

    def _move_ship(self, dt, pressed_keys):
        if "forward" in pressed_keys:
            self.speed_x += math.cos(self.angle) * self.acceleration * dt
            self.speed_y += math.sin(self.angle) * self.acceleration * dt
        if "backward" in pressed_keys:
            self.speed_x -= math.cos(self.angle) * self.acceleration * dt
            self.speed_y -= math.sin(self.angle) * self.acceleration * dt
        if "right" in pressed_keys:
            self.angle += self.TURN_SPEED * dt
        if "left" in pressed_keys:
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

    def update(self, asteroids, dt):
        pressed_keys = self.controls.handle_keys()
        self._move_ship(dt, pressed_keys)
        self.sensor.update(asteroids)

    def draw(self):
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
        self.sensor.draw()

from entity import Entity
import pygame
import math
from sensor import Sensor
from neural_net import NeuralNetwork
from controls import Controls
from genetic_algorithm import DNA

# def dna_to_weights(dna, nn_shape):
#     weights = []

pesos = []


def random_weights(nn_shape):
    weights_arr = []


class Ship(Entity):
    TURN_SPEED = 10

    def __init__(self, screen, x, y, radius, acceleration, control_type="Player"):
        super().__init__(screen, x, y, radius)
        self.acceleration = acceleration
        self.SCREEN_WIDTH = screen.get_width()
        self.SCREEN_HEIGHT = screen.get_height()
        self.max_speed = 10
        self.alive = True
        self.time_alive = 0
        self.sensor = Sensor(self)
        self.controls = Controls(control_type)
        self.use_brain = control_type == "AI"
        self.brain = None
        # self.dna = None
        self.nn_shape = [self.sensor.ray_count, 10, 10, 4]

        if self.use_brain:
            # self.dna = DNA()
            self.brain = NeuralNetwork(self.nn_shape)

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
        brain_output = None
        if self.use_brain:
            brain_output = self.brain.feed_forward(self.sensor.sensor())
        pressed_keys = self.controls.handle_keys(brain_output)
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

    # def update_brain_with_dna(self, genes):
    #     if self.use_brain:
    #         self.brain.update_dna(genes)

import math
import pygame


class Sensor:
    def __init__(self, ship):
        self.ship = ship
        self.ray_count = 16
        self.ray_length = 200
        self.ray_angle = 2 * math.pi / self.ray_count
        self.rays = []

    def update(self):
        self.rays = []
        ship_x, ship_y = self.ship.get_position()
        start = (ship_x, ship_y)
        for i in range(self.ray_count):
            angle = self.ray_angle * i
            end = (
                ship_x + self.ray_length * math.cos(angle),
                ship_y + self.ray_length * math.sin(angle),
            )

            self.rays.append({"start": start, "end": end})

    def draw(self):
        for ray in self.rays:
            pygame.draw.line(
                self.ship.screen, (255, 255, 255), ray["start"], ray["end"], 1
            )

import math
import pygame
from utils import distance_point_line


class Sensor:
    def __init__(self, ship):
        self.ship = ship
        self.ray_count = 16
        self.ray_length = 150
        self.ray_angle = 2 * math.pi / self.ray_count
        self.rays = []
        self.readings = []

    def _cast_rays(self):
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

    def _get_readings(self, ray, asteroids):
        for asteroid in asteroids:
            touch = self._get_intersection(ray, asteroid)
            if touch:
                return True
        return False

    @staticmethod
    def _get_intersection(ray, asteroid):
        x1, y1 = ray["start"]
        x2, y2 = ray["end"]
        radius = asteroid.get_radius()
        x0, y0 = asteroid.get_position()
        distance = distance_point_line(x0, y0, x1, y1, x2, y2)
        if distance > radius:
            return False
        return True

    def update(self, asteroids):
        self._cast_rays()
        self.readings = []
        for ray in self.rays:
            self.readings.append(self._get_readings(ray, asteroids))

    def draw(self):
        for i, ray in enumerate(self.rays):
            color = (255, 255, 255)
            if self.readings[i]:
                color = (0, 128, 128)
            pygame.draw.line(self.ship.screen, color, ray["start"], ray["end"], 1)

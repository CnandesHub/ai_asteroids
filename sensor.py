import math
import pygame
from utils import distance_point_line, lerp


class Sensor:
    def __init__(self, ship):
        self.ship = ship
        self.ray_count = 8
        self.ray_length = 150
        self.ray_angle = 2 * math.pi / self.ray_count
        self.rays = []
        self.readings = [0] * self.ray_count

    def _cast_rays(self):
        self.rays = []
        ship_x, ship_y = self.ship.get_position()
        start = (ship_x, ship_y)
        for i in range(self.ray_count):
            angle = self.ray_angle * i + self.ship.angle
            end = (
                ship_x + self.ray_length * math.cos(angle),
                ship_y + self.ray_length * math.sin(angle),
            )

            self.rays.append({"start": start, "end": end, "angle": angle})

    def _get_readings(self, ray, asteroids):
        touches = []
        for asteroid in asteroids:
            touches.append(self.find_distance_line_circle(ray, asteroid))
        touches = list(filter(None, touches))

        if not touches:
            return 0

        minimun_distance = min(touches)
        if minimun_distance > self.ray_length:
            return 0

        return minimun_distance / self.ray_length

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

    @staticmethod
    def find_distance_line_circle(ray, asteroid):
        # x1, y1, x3, y3, x2, y2, r
        x1, y1 = ray["start"]
        x3, y3 = ray["end"]
        r = asteroid.get_radius()
        x2, y2 = asteroid.get_position()

        # Direction vector of the line segment
        dx = x3 - x1
        dy = y3 - y1

        # Coefficients of the quadratic equation
        A = dx**2 + dy**2
        B = 2 * (dx * (x1 - x2) + dy * (y1 - y2))
        C = (x1 - x2) ** 2 + (y1 - y2) ** 2 - r**2

        # Discriminant
        D = B**2 - 4 * A * C

        if D < 0:
            return None  # No intersection
        else:
            sqrt_D = math.sqrt(D)
            t1 = (-B + sqrt_D) / (2 * A)
            t2 = (-B - sqrt_D) / (2 * A)

            # Calculate intersection points
            intersections = []
            if 0 <= t1 <= 1:
                x_int1 = x1 + t1 * dx
                y_int1 = y1 + t1 * dy
                intersections.append((x_int1, y_int1))

            if 0 <= t2 <= 1:
                x_int2 = x1 + t2 * dx
                y_int2 = y1 + t2 * dy
                intersections.append((x_int2, y_int2))

            if not intersections:
                return None  # Intersections are outside the line segment

            # Calculate distances
            distances = [
                math.sqrt((x - x1) ** 2 + (y - y1) ** 2) for x, y in intersections
            ]
            return min(distances)

    def update(self, asteroids):
        self._cast_rays()
        self.readings = []
        for ray in self.rays:
            self.readings.append(self._get_readings(ray, asteroids))

    def draw(self):
        for i, ray in enumerate(self.rays):
            color = (255, 255, 153)
            pygame.draw.line(self.ship.screen, color, ray["start"], ray["end"], 2)

            if self.readings[i]:
                xi, yi = ray["start"]
                xf, yf = ray["end"]

                x = lerp(xi, xf, self.readings[i])
                y = lerp(yi, yf, self.readings[i])

                pygame.draw.line(
                    self.ship.screen, (255, 255, 255), ray["start"], (x, y), 2
                )

    def sensor(self):
        return self.readings

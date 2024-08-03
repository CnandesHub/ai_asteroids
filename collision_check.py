import math


class CollisionEntityCheck:

    @staticmethod
    def check_intersection(a_x, a_y, a_radius, b_x, b_y, b_radius):
        return (a_x - b_x) ** 2 + (a_y - b_y) ** 2 <= (a_radius + b_radius) ** 2

    @staticmethod
    def check_collision(entity1, entity2):
        a_x, a_y = entity1.get_position()
        a_radius = entity1.get_radius()
        b_x, b_y = entity2.get_position()
        b_radius = entity2.get_radius()
        collision = CollisionEntityCheck.check_intersection(
            a_x, a_y, a_radius, b_x, b_y, b_radius
        )
        distance = math.sqrt((a_x - b_x) ** 2 + (a_y - b_y) ** 2) - b_radius
        distance = distance if distance >= 0 else 0
        return collision


def find_intersection(x1, y1, x3, y3, x2, y2, r):
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
        distances = [math.sqrt((x - x1) ** 2 + (y - y1) ** 2) for x, y in intersections]
        return min(distances)


def find_intersection_and_distance(x1, y1, x2, y2, r2, theta):
    # Convert angle to radians
    # theta = math.radians(angle)

    # Calculate A, B, and C for the quadratic equation
    B = 2 * ((x1 - x2) * math.cos(theta) + (y1 - y2) * math.sin(theta))
    C = (x1 - x2) ** 2 + (y1 - y2) ** 2 - r2**2

    # Calculate the discriminant
    discriminant = B**2 - 4 * C

    if discriminant < 0:
        # No intersection
        return 0
    elif discriminant == 0:
        # One intersection
        t = -B / 2
    else:
        # Two intersections, we want the smallest positive t
        t1 = (-B + math.sqrt(discriminant)) / 2
        t2 = (-B - math.sqrt(discriminant)) / 2
        t = min(t for t in (t1, t2) if t > 0)

    if t < 0:
        # Intersection point is behind the start of the line
        return 0

    # # Calculate the intersection point
    # x_intersect = x1 + t * math.cos(theta)
    # y_intersect = y1 + t * math.sin(theta)

    # Calculate the distance from the first circle to the intersection point
    distance = t
    return distance
    # return (x_intersect, y_intersect), distance


def calculate_angle(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    angle_rad = math.atan2(dy, dx)
    # angle_deg = math.degrees(angle_rad)
    return angle_rad

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
        return collision

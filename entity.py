class Entity:

    def __init__(self, screen, x, y, acceleration):
        self.x = x
        self.y = y
        self.acceleration = acceleration
        self.angle = 0
        self.screen = screen
        self.speed_x = 0
        self.speed_y = 0
        self.TARGET_FPS = 60

    def update(self, dt):
        pass

    def draw(self):
        pass

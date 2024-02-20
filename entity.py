class Entity:

    def __init__(self, screen, x, y, size=20):
        self.x = x
        self.y = y
        self.size = size
        self.angle = 0
        self.screen = screen
        self.speed_x = 0
        self.speed_y = 0
        self.TARGET_FPS = 60

    def update(self, dt):
        pass

    def draw(self):
        pass

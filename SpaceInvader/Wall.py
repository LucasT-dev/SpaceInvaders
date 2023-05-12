import core


class Wall:

    def __init__(self, position):
        self.position = position
        self.color = (255, 255, 255)
        self.height = 10

    def draw(self):
        core.Draw.rect(self.color, (self.position.x, self.position.y, self.height, self.height))
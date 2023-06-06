import core


class Wall:

    def __init__(self, position, texture):
        self.position = position
        self.color = (255, 255, 255,127)
        self.height = 10
        self.modele = texture

    def draw(self):
        self.modele.pos.x = self.position.x
        self.modele.pos.y = self.position.y
        self.modele.show()

    def remove(self):
        core.memory("wall").remove(self)
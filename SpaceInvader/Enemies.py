import core


class Enemies:

    def __init__(self, position, texture, score):
        self.lifePoint = score
        self.modele = texture
        self.shield = False
        self.position = position
        self.color = (155, 255, 255)
        self.height = 10

    def draw(self):

        self.modele.pos.x = self.position.x
        self.modele.pos.y = self.position.y
        self.modele.show()
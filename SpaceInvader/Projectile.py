from pygame import Vector2

import core


class Projectile:

    def __init__(self, position, speed,texture):
        self.speed = speed
        self.length = 3
        self.position = position
        self.modele = texture
        self.color=(255,0,0,127)

    def movePlayerProjectile(self):

        self.position = Vector2(self.position.x, self.position.y - self.speed)

    def moveEnemiesProjectile(self):

        self.position = Vector2(self.position.x, self.position.y + (self.speed * core.memory("partie").speedCoef))

    def draw(self):
        self.modele.pos.x = self.position.x
        self.modele.pos.y = self.position.y
        self.modele.show()
        #core.Draw.rect(self.color,(self.position.x+2, self.position.y, 17,27))
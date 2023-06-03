from pygame import Vector2

import core


class Projectile:

    def __init__(self, position, speed, color):
        self.speed = speed
        self.length = 3
        self.position = position
        self.color = color

    def movePlayerProjectile(self):

        self.position = Vector2(self.position.x, self.position.y - self.speed)

    def moveEnemiesProjectile(self):

        self.position = Vector2(self.position.x, self.position.y + (self.speed * core.memory("partie").speedCoef))

    def draw(self):
        core.Draw.rect(self.color,(self.position.x, self.position.y, 10, 20))
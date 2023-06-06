from pygame import Vector2

import core
from SpaceInvader.Projectile import Projectile


class Vaisseau:

    def __init__(self):
        self.score = 0
        self.speed = 7
        self.speedProjectile = 8
        self.maxProjectile = 6
        self.lifePoint = 3
        self.position = Vector2(500, 700)
        self.projectile = []
        core.memory("textureV").pos = self.position

    def moveRight(self):
        self.position.x = self.position.x + self.speed
        core.memory("textureV").pos = self.position

    def moveLeft(self):
        self.position.x = self.position.x - self.speed
        core.memory("textureV").pos = self.position

    def addPoint(self, point):
        self.score += point

    def removelife(self):

        self.lifePoint -= 1

        if self.lifePoint.__eq__(0):
            core.memory("partie").end()

    def addProjectile(self):

        if len(self.projectile) < self.maxProjectile:

            self.projectile.append(
                Projectile(Vector2(core.memory("vaisseau").position.x + 27, core.memory("vaisseau").position.y), self.speedProjectile,
                           core.memory("missileV")))

    def removeProjectile(self, element):

        if (self.projectile.__contains__(element)):
            self.projectile.remove(element)

    def updateProjectile(self):

        for i in self.projectile:
            i.movePlayerProjectile()
            i.draw()

            if i.position.y < 0:
                self.removeProjectile(i)

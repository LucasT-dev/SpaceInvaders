from pygame import Vector2

import core
from SpaceInvader.Projectile import Projectile


class Vaisseau:

    def __init__(self):
        self.score = 0
        self.modele = 0  # !!!
        self.speed = 2
        self.maxSpeed = 5
        self.acc = 2
        self.maxAcc = 3
        self.lifePoint = 3
        self.shottingSpeed = 2
        self.shield = False
        self.position = Vector2(500, 700)
        self.projectile = []

    def moveRight(self):
        self.position.x = self.position.x + 7
        core.memory("textureV").pos = self.position

    def moveLeft(self):
        self.position.x = self.position.x - 7
        core.memory("textureV").pos = self.position

    def addPoint(self, point):
        self.score += point

    def removelife(self):
        self.lifePoint -= 1

        if self.lifePoint.__eq__(0):
            core.memory("partie").end()

    def addProjectile(self):

        print("projectile")

        if len(self.projectile) < 5:
            print("inf 5")
            self.projectile.append(
                Projectile(Vector2(core.memory("vaisseau").position.x + 32, core.memory("vaisseau").position.y), 5,
                           (0, 0, 255)))

    def removeProjectile(self, element):
        if (self.projectile.__contains__(element)):
            self.projectile.remove(element)

    def updateProjectile(self):

        for i in self.projectile:
            i.position = Vector2(i.position.x + 0, i.position.y - self.speed)
            i.draw()
            if i.position.y < 0:
                print("y inf 0 ")
                self.removeProjectile(i)

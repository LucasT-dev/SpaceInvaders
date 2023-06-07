from random import randrange

from pygame import Vector2

import core
from SpaceInvader.Projectile import Projectile


class Enemies:

    def __init__(self, position, texture, score, speedProjectile):
        self.score = score
        self.speedProjectile = speedProjectile
        self.modele = texture
        self.position = position
        self.color = (155, 255, 255)
        self.projectile = []
        self.speed = 2.5
        self.tempsExplosion = 6

    def draw(self):
        self.modele.pos.x = self.position.x
        self.modele.pos.y = self.position.y
        self.modele.show()

    def remove(self):
        self.remove()



    def launchProjectile(self):

        i = randrange(100)

        if i > (98 - core.memory("partie").coefLaunchProjectile):

            if Vector2.distance_to(self.position, core.memory("vaisseau").position) < 600:

                j = randrange(100)
                if j > 65:
                    self.addProjectile()

    def addProjectile(self):
        if (str(self.modele.url).__eq__("./SpaceInvader/ressource/Red_En.png")):
            self.projectile.append(
                Projectile(Vector2(self.position.x + 5, self.position.y), 5,core.memory("projectileR")))
        if (str(self.modele.url).__eq__("./SpaceInvader/ressource/Green_En.png")):
            self.projectile.append(
                Projectile(Vector2(self.position.x + 5, self.position.y), 5,core.memory("projectileG")))

    def removeProjectile(self, element):
        if (self.projectile.__contains__(element)):
            self.projectile.remove(element)

    def update(self):
        self.draw()
        self.launchProjectile()
        self.updateProjectile()

    def updateProjectile(self):

        for i in self.projectile:

            i.moveEnemiesProjectile()
            i.draw()

            if i.position.y > 800:
                self.removeProjectile(i)

    def moveRight(self):
        self.position.x = self.position.x + self.speed
        self.modele.pos = self.position

    def moveLeft(self):
        self.position.x = self.position.x - self.speed
        self.modele.pos.x = self.position.x

    def moveDown(self):
        self.position.y = self.position.y + self.speed-2.25
        self.modele.pos.y = self.position.y

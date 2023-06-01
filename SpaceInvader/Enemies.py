from random import randrange

from pygame import Vector2

import core
from SpaceInvader.Projectile import Projectile


class Enemies:

    def __init__(self, position, texture, score, speedProjectile):
        self.score = score
        self.speedProjectile = speedProjectile
        self.modele = texture
        self.shield = False
        self.position = position
        self.color = (155, 255, 255)
        self.height = 10
        self.projectile = []

    def draw(self):

        self.modele.pos.x = self.position.x
        self.modele.pos.y = self.position.y
        self.modele.show()

    def remove(self):
        self.remove()


    def launchProjectile(self):

        i = randrange(100)

        if i > 98:

            if Vector2.distance_to(self.position, core.memory("vaisseau").position) < 600:

                j = randrange(100)
                if j > 65:
                    self.addProjectile()

    def addProjectile(self):

        self.projectile.append(
            Projectile(Vector2(self.position.x + 32, self.position.y), 5,
                       (0, 0, 255)))

    def removeProjectile(self, element):
        self.projectile.remove(element)

    def update(self):

        self.draw()
        self.launchProjectile()

        self.updateProjectile()

    def updateProjectile(self):

        for i in self.projectile:
            i.position = Vector2(i.position.x, i.position.y + self.speedProjectile)
            i.draw()

            if i.position.y > 800:
                self.removeProjectile(i)

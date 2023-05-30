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

    def launchProjectile(self):

        i = randrange(100)

        if i > 98:

            if Vector2.distance_to(self.position, core.memory("vaisseau").position) < 600:

                j = randrange(100)

                if self.speedProjectile == 5:
                    if j > 65:
                        core.memory("Eprojectile").append(
                            Projectile(Vector2(self.position.x, self.position.y), self.speedProjectile, (0, 255, 0)))

                if self.speedProjectile == 3:
                    if j > 35:
                        core.memory("Eprojectile").append(
                            Projectile(Vector2(self.position.x, self.position.y), self.speedProjectile, (255, 0, 0)))

    def addProjectile(self):
        if len(self.projectile) < 5:
            self.projectile.append(
                Projectile(Vector2(core.memory("vaisseau").position.x + 32, core.memory("vaisseau").position.y), 5,
                           (0, 0, 255)))


    def updateProjectile(self):

        if len(self.projectile) < 1:
            for i in self.projectile:
                i.position = Vector2(i.position.x + self.speed, i.position.y + self.speed)
                i.draw()
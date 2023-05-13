from pygame import Vector2

import core


class Vaisseau:

    def __init__(self):
        self.score = 0
        self.modele = 0  # !!!
        self.speed = 2
        self.maxSpeed = 5
        self.acc = 2
        self.maxAcc = 3
        self.lifePoint = 100
        self.shottingSpeed = 2
        self.shield = False
        self.position = Vector2(500, 700)

    def moveRight(self):
        self.position.x = self.position.x + 7
        core.memory("textureV").pos = self.position

    def moveLeft(self):
        self.position.x = self.position.x - 7
        core.memory("textureV").pos = self.position

    def addPoint(self, point):
        self.score += point

    def removePoint(self, point):
        self.score -= point
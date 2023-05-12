from pygame import Vector2

import core
class Projectile:

    def __init__(self, position, speed):
        self.speed = speed
        self.length = 3
        self.position = position
        self.color = (255, 255, 255)

    def update(self):

        self.position = Vector2(self.position.x, self.position.y - self.speed)


    def draw(self):

        core.Draw.rect(self.color,
                           (self.position.x, self.position.y, 10, 20))
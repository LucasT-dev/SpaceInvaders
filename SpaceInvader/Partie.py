from datetime import datetime
from random import randrange

from pygame import Vector2, time

import core
from SpaceInvader import Screen
from SpaceInvader.Enemies import Enemies
from SpaceInvader.Wall import Wall


class Partie:

    def __init__(self):
        self.backgroundColor = (0, 0, 0)
        self.timer = 0

    def start(self):

        # Wall
        n = 10
        l = 1000
        d = (l / n)
        d1 = (l / n) - (l / n) / 2

        for i in range(n):
            core.memory("wall").append(Wall(Vector2((((i + 1) * d) - d1, 600))))

        # Enemies
        n = randrange(1, 15)
        l = 1000
        d = (l / n)
        d1 = d - (d / 2)

        for i in range(n):
            core.memory("enemies").append(
                Enemies(Vector2((((i + 1) * d) - d1, 200)), core.memory("textureRed_En"), 10, 3))

        n = randrange(12)
        l = 1000
        d = (l / n)
        d1 = (l / n) - (l / n) / 2

        for i in range(n):
            core.memory("enemies").append(
                Enemies(Vector2((((i + 1) * d) - d1, 300)), core.memory("textureGreen_En"), 5, 5))


    def end(self):

        pass

    def update(self):

        core.setBgColor((0, 0, 0))

        if core.memory("screen").__eq__(Screen.Screen.MENU.value):
            if not core.memory("textureL").ready:
                core.memory("textureL").load()
            core.memory("textureL").show()

            if not core.memory("textureP").ready:
                core.memory("textureP").load()
            core.memory("textureP").show()

            if not core.memory("textureS").ready:
                core.memory("textureS").load()
            core.memory("textureS").show()

            if not core.memory("textureE").ready:
                core.memory("textureE").load()
            core.memory("textureE").show()

        if core.memory("screen").__eq__(Screen.Screen.INGAME.value):

            if not core.memory("textureV").ready:
                core.memory("textureV").load()
            core.memory("textureV").show()

            if not core.memory("textureRed_En").ready:
                core.memory("textureRed_En").load()

            if not core.memory("textureGreen_En").ready:
                core.memory("textureGreen_En").load()

        if core.memory("screen").__eq__(Screen.Screen.SETTING.value):

            if not core.memory("textureE").ready:
                core.memory("textureE").load()
            core.memory("textureE").show()

        if core.memory("screen").__eq__(Screen.Screen.GAMEOVER.value):

            core.Draw.text((255, 137, 0), "GAME OVER : ", Vector2(350, 100), 70, "Script MT Bold")
            core.Draw.text((255, 255, 255), "SCORE : " + str(core.memory("vaisseau").score), Vector2(450, 200), 30,
                           "Arial")

            if not core.memory("textureE").ready:
                core.memory("textureE").load()
            core.memory("textureE").show()

        self.timer = datetime.second
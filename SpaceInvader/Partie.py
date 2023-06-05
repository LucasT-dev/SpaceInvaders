import time
from datetime import datetime
from random import randrange

import pygame
from pygame import Vector2
from pygame.rect import Rect

import core
from SpaceInvader import Screen
from SpaceInvader.Enemies import Enemies
from SpaceInvader.Wall import Wall


class Partie:

    def __init__(self):
        self.backgroundColor = (0, 0, 0)
        self.timer = 0
        self.speedCoef = 1
        self.coefLaunchProjectile = 0
        self.startTime = time.time()
        self.endTime = 0
        self.enemiesKill = 0
        self.name = " "
        self.totalScore = 0

    def start(self):

        # Wall
        n = 10
        l = 1000
        d = (l / n)
        d1 = (l / n) - (l / n) / 2

        for i in range(n):
            core.memory("wall").append(Wall(Vector2((((i + 1) * d) - d1, 600))))

        # Enemies
        n = randrange(1, 15) #15
        l = 1000
        d = (l / n)
        d1 = d - (d / 2)

        for i in range(n):
            core.memory("enemies").append(
                Enemies(Vector2((((i + 1) * d) - d1, 200)), core.memory("textureRed_En"), 20, 3))

        n = randrange(1, 12) #12
        l = 1000
        d = (l / n)
        d1 = (l / n) - (l / n) / 2

        for i in range(n):
            core.memory("enemies").append(
                Enemies(Vector2((((i + 1) * d) - d1, 300)), core.memory("textureGreen_En"), 10, 5))

    def end(self):
        print("END")
        core.memory("screen", Screen.Screen.GAMEOVER.value)
        self.endTime = time.time() - self.startTime

    def collide(self):

        for i in core.memory("vaisseau").projectile:

            vaisseauRectProjectile = Rect(i.position.x, i.position.y, 10, 20)
            #core.Draw.rect((255, 255, 255, 150), vaisseauRectProjectile)

            for j in core.memory("wall"):

                wallRect = Rect(j.position.x, j.position.y, 10, 10)
                #core.Draw.rect(j.color, wallRect)

                if (vaisseauRectProjectile.colliderect(wallRect)):

                    core.memory("vaisseau").removeProjectile(i)
                    j.remove()

            for k in core.memory("enemies"):

                enemiesRect = Rect(k.position.x, k.position.y, 20, 10)
                #core.Draw.rect((0, 0, 255, 150), enemiesRect)

                if (vaisseauRectProjectile.colliderect(enemiesRect)):
                    core.memory("vaisseau").removeProjectile(i)
                    core.memory("enemies").remove(k)

                    core.memory("vaisseau").addPoint(k.score)
                    core.memory("partie").enemiesKill += 1

                for o in k.projectile:
                    enemiesProjectileRect = Rect(o.position.x, o.position.y, 10, 20)
                    #core.Draw.rect((0, 255, 255, 150), enemiesProjectileRect)

                    if vaisseauRectProjectile.colliderect(enemiesProjectileRect):
                        core.memory("vaisseau").removeProjectile(i)
                        k.removeProjectile(o)


        for l in core.memory("enemies"):

            for m in l.projectile:

                enemiesProjectileRect = Rect(m.position.x, m.position.y, 10, 20)
                core.Draw.rect(m.color, enemiesProjectileRect)

                for n in core.memory("wall"):

                    wallRect = Rect(n.position.x, n.position.y, 10, 10)
                    core.Draw.rect(n.color, wallRect)

                    if wallRect.colliderect(enemiesProjectileRect):
                        l.removeProjectile(m)
                        n.remove()

                vaisseauRect = Rect(core.memory("vaisseau").position.x + 15, core.memory("vaisseau").position.y + 10, 40, 60)
                #core.Draw.rect((255, 255, 255, 150), vaisseauRect)

                if vaisseauRect.colliderect(enemiesProjectileRect):
                     l.removeProjectile(m)
                     core.memory("vaisseau").removelife()

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


            j = 0
            for i in core.memory("score"):
                core.Draw.text((255, 255, 255), i.pseudo + " : " + str(i.score), (100, 200 + 25*j), 35, "Arial")
                j +=1

        if core.memory("screen").__eq__(Screen.Screen.INGAME.value):

            if not core.memory("textureV").ready:
                core.memory("textureV").load()
            core.memory("textureV").show()

            if not core.memory("textureRed_En").ready:
                core.memory("textureRed_En").load()

            if not core.memory("textureGreen_En").ready:
                core.memory("textureGreen_En").load()


            core.Draw.text((255, 255, 255), "Score : " + str(core.memory("vaisseau").score), Vector2(800, 20), 25,
                           "Arial")
            core.Draw.text((255, 255, 255), "LifePoint : " + str(core.memory("vaisseau").lifePoint), Vector2(800, 45),
                           25, "Arial")
            core.Draw.text((255, 255, 255), "Kill : " + str(self.enemiesKill), Vector2(800, 70), 25,
                           "Arial")
            core.Draw.text((255, 255, 255), "Time : " + str(time.time() - self.startTime), Vector2(800, 95), 25,
                           "Arial")

        if core.memory("screen").__eq__(Screen.Screen.SETTING.value):

            if not core.memory("textureE").ready:
                core.memory("textureE").load()
            core.memory("textureE").show()

        if core.memory("screen").__eq__(Screen.Screen.GAMEOVER.value):

            self.totalScore = core.memory("vaisseau").score * self.enemiesKill - self.endTime.__int__()

            core.Draw.text((255, 137, 0), "GAME OVER : ", Vector2(350, 100), 70, "Script MT Bold")
            core.Draw.text((255, 255, 255), "SCORE : " + str(core.memory("vaisseau").score), Vector2(450, 200), 30,
                           "Arial")
            core.Draw.text((255, 255, 255), "Kill : " + str(self.enemiesKill), Vector2(450, 250), 25,
                           "Arial")
            core.Draw.text((255, 255, 255), "Time : " + str(self.endTime), Vector2(450, 300), 25,
                           "Arial")

            core.Draw.text((255, 255, 255), "TOTAL : " + str(core.memory("vaisseau").score), Vector2(450, 450), 25,
                           "Arial")
            core.Draw.text((255, 255, 255), " * " + str(self.enemiesKill), Vector2(490, 475), 25,
                           "Arial")
            core.Draw.text((255, 255, 255), " - " + str(self.endTime.__int__()), Vector2(490, 500), 25,
                           "Arial")
            core.Draw.text((255, 255, 255), " ------------------- ", Vector2(450, 525), 25,
                           "Arial")
            core.Draw.text((255, 255, 255), " = " + str(self.totalScore), Vector2(450, 550), 25,
                           "Arial")

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    print(pygame.key.name(event.key))
                    self.name += str(pygame.key.name(event.key))

            core.Draw.text((255, 255, 255), " Name : " + self.name, Vector2(450, 600), 25), "Arial"

            if not core.memory("textureE").ready:
                core.memory("textureE").load()
            core.memory("textureE").show()
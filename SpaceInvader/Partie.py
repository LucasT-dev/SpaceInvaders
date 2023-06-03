from datetime import datetime
from random import randrange

from pygame import Vector2, time
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

    def start(self):

        # Wall
        n = 10
        l = 1000
        d = (l / n)
        d1 = (l / n) - (l / n) / 2

        for i in range(n):
            core.memory("wall").append(Wall(Vector2((((i + 1) * d) - d1, 600))))

        # Enemies
        n = randrange(1, 5) #15
        l = 1000
        d = (l / n)
        d1 = d - (d / 2)

        for i in range(n):
            core.memory("enemies").append(
                Enemies(Vector2((((i + 1) * d) - d1, 200)), core.memory("textureRed_En"), 10, 3))

        n = randrange(1, 3) #12
        l = 1000
        d = (l / n)
        d1 = (l / n) - (l / n) / 2

        for i in range(n):
            core.memory("enemies").append(
                Enemies(Vector2((((i + 1) * d) - d1, 300)), core.memory("textureGreen_En"), 5, 5))

    def end(self):
        print("END")
        core.memory("screen", Screen.Screen.GAMEOVER.value)

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
                core.Draw.rect((0, 0, 255, 150), enemiesRect)

                if (vaisseauRectProjectile.colliderect(enemiesRect)):
                    core.memory("vaisseau").removeProjectile(i)
                    core.memory("vaisseau").addPoint(10)
                    core.memory("enemies").remove(k)

                for o in k.projectile:
                    enemiesProjectileRect = Rect(o.position.x, o.position.y, 10, 20)
                    core.Draw.rect((0, 255, 255, 150), enemiesProjectileRect)

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

        if core.memory("screen").__eq__(Screen.Screen.INGAME.value):

            if not core.memory("textureV").ready:
                core.memory("textureV").load()
            core.memory("textureV").show()

            if not core.memory("textureRed_En").ready:
                core.memory("textureRed_En").load()

            if not core.memory("textureGreen_En").ready:
                core.memory("textureGreen_En").load()


            core.Draw.text((255, 255, 255), "Score :" + str(core.memory("vaisseau").score), Vector2(800, 20), 25,
                           "Arial")
            core.Draw.text((255, 255, 255), "LifePoint :" + str(core.memory("vaisseau").lifePoint), Vector2(800, 45),
                           25, "Arial")
            core.Draw.text((255, 255, 255), "Position :" + str(core.memory("vaisseau").position), Vector2(800, 70), 25,
                           "Arial")

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

        #self.timer = datetime.second
import time
from datetime import datetime
from random import randrange

import pygame
from pygame import Vector2
from pygame.rect import Rect

import core
from SpaceInvader.Enemies import Enemies
from SpaceInvader.Screen import Screen
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
        self.pygameFont = pygame.font.SysFont("./SpaceInvader/ressource/Police/Police.TTF",35)


    def start(self):

        # Wall
        n = randrange(3,10)
        l = 1000
        d = (l / n)
        d1 = (l / n) - (l / n) / 2

        for i in range(n):
            core.memory("wall").append(Wall(Vector2((((i + 1) * d) - d1, 600)), core.memory("textureWall")))

        # Enemies
        n = randrange(3, 10)
        l = 1000
        d = (l / n)
        d1 = d - (d / 2)

        for i in range(n):
            core.memory("enemies").append(
                Enemies(Vector2((((i + 1) * d) - d1, 100)), core.memory("textureRed_En"), 20, 3))

        n = randrange(2, 8)
        l = 1000
        d = (l / n)
        d1 = (l / n) - (l / n) / 2

        for i in range(n):
            core.memory("enemies").append(
                Enemies(Vector2((((i + 1) * d) - d1, 200)), core.memory("textureGreen_En"), 10, 5))

    def end(self):
        print("END")
        core.memory("screen", Screen.GAMEOVER)
        self.endTime = time.time() - self.startTime
        self.timer = 0

    def collide(self):

        for i in core.memory("vaisseau").projectile:

            vaisseauRectProjectile = Rect(i.position.x, i.position.y, 10, 20)
            #core.Draw.rect((255, 255, 255, 150), vaisseauRectProjectile)

            for j in core.memory("wall"):

                wallRect = Rect(j.position.x + 15, j.position.y + 15, 30, 28)
                #core.Draw.rect(j.color, wallRect)

                if (vaisseauRectProjectile.colliderect(wallRect)):

                    core.memory("vaisseau").removeProjectile(i)
                    j.remove()

            for k in core.memory("enemies"):

                enemiesRect = None

                if (str(k.modele.url) == ("./SpaceInvader/ressource/Red_En.png")):
                    enemiesRect = Rect(k.position.x, k.position.y, 38, 22)

                if (str(k.modele.url) == ("./SpaceInvader/ressource/Green_En.png")):
                    enemiesRect = Rect(k.position.x, k.position.y, 20, 17)
                #core.Draw.rect((0, 0, 255, 150), enemiesRect)

                if (vaisseauRectProjectile.colliderect(enemiesRect)):

                    core.memory("vaisseau").removeProjectile(i)
                    core.memory("explosion").pos = k.position
                    core.memory("explosion").show()
                    core.memory("enemies").remove(k)
                    core.memory("vaisseau").addPoint(k.score)
                    core.memory("partie").enemiesKill += 1
                    '''core.memory("explosion").pos = k.position
                    if k.tempsExplosion > 0:
                        core.memory("explosion").show()
                        k.tempsExplosion -= 0.1
                    else:
                        core.memory("enemies").remove(k)
                        core.memory("vaisseau").addPoint(k.score)
                        core.memory("partie").enemiesKill += 1'''

                for o in k.projectile:
                    enemiesProjectileRect = Rect(o.position.x, o.position.y, 10, 20)
                    #core.Draw.rect((0, 255, 255, 150), enemiesProjectileRect)

                    if vaisseauRectProjectile.colliderect(enemiesProjectileRect):
                        core.memory("vaisseau").removeProjectile(i)
                        k.removeProjectile(o)


        for l in core.memory("enemies"):

            for m in l.projectile:

                enemiesProjectileRect = Rect(m.position.x + 4, m.position.y, 15, 25)
                # core.Draw.rect(m.color, enemiesProjectileRect)

                for n in core.memory("wall"):

                    wallRect = Rect(n.position.x + 15, n.position.y + 15, 30, 28)
                    # core.Draw.rect(n.color, wallRect)

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

        if core.memory("screen") == Screen.MENU:

            if not core.memory("bgMenu").ready:
                core.memory("bgMenu").load()
            core.memory("bgMenu").show()

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

        if core.memory("screen") == Screen.PAUSE:
            if not core.memory("texturePa").ready:
                core.memory("texturePa").load()
            core.memory("texturePa").show()
            core.memory("textureP").load()
            core.memory("textureP").show()
            core.memory("textureE").load()
            core.memory("textureE").show()

        if core.memory("screen") == Screen.INGAME:
            if not core.memory("bgJeu").ready:
                core.memory("bgJeu").load()
            core.memory("bgJeu").show()

            if not core.memory("textureV").ready:
                core.memory("textureV").load()
            core.memory("textureV").show()

            if not core.memory("textureRed_En").ready:
                core.memory("textureRed_En").load()

            if not core.memory("textureGreen_En").ready:
                core.memory("textureGreen_En").load()
            if not core.memory("textureWall").ready:
                core.memory("textureWall").load()

            if not core.memory("missileV").ready:
                core.memory("missileV").load()

            if not core.memory("projectileG").ready:
                core.memory("projectileG").load()

            if not core.memory("projectileR").ready:
                core.memory("projectileR").load()

            if not core.memory("explosion").ready:
                core.memory("explosion").load()

            n = int(time.time() - self.startTime)


            core.Draw.text((255, 255, 255), "Score : " + str(core.memory("vaisseau").score), Vector2(800, 20), 25,
                           self.pygameFont)
            core.Draw.text((255, 255, 255), "LifePoint : " + str(core.memory("vaisseau").lifePoint), Vector2(800, 45),
                           25, self.pygameFont)
            core.Draw.text((255, 255, 255), "Kill : " + str(self.enemiesKill), Vector2(800, 70), 25,
                           self.pygameFont)
            core.Draw.text((255, 255, 255), "Time : " + str(int(time.time() - self.startTime)), Vector2(800, 95), 25,
                           self.pygameFont)
            # mouvements ennemis
            for w in core.memory("enemies"):
                if n % 2 == 0:
                    w.moveRight()
                elif n % 2 != 0:
                    w.moveLeft()
                if (str(w.modele.url).__eq__("./SpaceInvader/ressource/Red_En.png")) and w.position.y <= 400:
                    w.moveDown()
                if (str(w.modele.url).__eq__("./SpaceInvader/ressource/Green_En.png")) and w.position.y <= 500:
                    w.moveDown()

        if core.memory("screen") == Screen.SCOREBOARD:

            if not core.memory("textureE").ready:
                core.memory("textureE").load()
            core.memory("textureE").show()
            j = 0
            for i in core.memory("score"):
                self.pygameFont = pygame.font.SysFont("./SpaceInvader/ressource/Police/Police.TTF", 80)
                core.Draw.text((255,255,255),"Scoreboard",(350,100),80,self.pygameFont)
                self.pygameFont = pygame.font.SysFont("./SpaceInvader/ressource/Police/Police.TTF", 35)
                core.Draw.text((255, 255, 255), str(j+1) + " : " + i.pseudo + " : " + str(i.score).replace("\n",""), (400, 200 + 25*j), 45, self.pygameFont)
                j +=1
        if core.memory("screen") == Screen.GAMEOVER:

            self.totalScore = core.memory("vaisseau").score * self.enemiesKill - self.endTime.__int__()

            core.Draw.text((255, 137, 0), "GAME OVER : ", Vector2(350, 100), 70, "Script MT Bold")
            core.Draw.text((255, 255, 255), "SCORE : " + str(core.memory("vaisseau").score), Vector2(450, 200), 30,
                           self.pygameFont)
            core.Draw.text((255, 255, 255), "Kill : " + str(self.enemiesKill), Vector2(450, 250), 25,
                           self.pygameFont)
            core.Draw.text((255, 255, 255), "Time : " + str(self.endTime), Vector2(450, 300), 25,
                           self.pygameFont)

            core.Draw.text((255, 255, 255), "TOTAL : " + str(core.memory("vaisseau").score), Vector2(450, 450), 25,
                           self.pygameFont)
            core.Draw.text((255, 255, 255), " * " + str(self.enemiesKill), Vector2(490, 475), 25,
                           self.pygameFont)
            core.Draw.text((255, 255, 255), " - " + str(self.endTime.__int__()), Vector2(490, 500), 25,
                           self.pygameFont)
            core.Draw.text((255, 255, 255), " ------------------- ", Vector2(450, 525), 25,
                           self.pygameFont)
            core.Draw.text((255, 255, 255), " = " + str(self.totalScore), Vector2(450, 550), 25,
                           self.pygameFont)

            if core.getkeyPressValue():

                s = pygame.key.name((core.getkeyPressValue()))
                if s != "space" and s != "return" and s != "backspace" and s != "right_shift" and s != "left_shift" and s != "right" and s != "left" and s != "up" and s != "down" and len(self.name)<10:

                    self.name += pygame.key.name((core.getkeyPressValue()))
                    core.keyPressValue = None
                if s.__eq__("backspace") and len(self.name) > 1:
                    print(len(self.name))
                    self.name = self.name.replace(self.name[len(self.name)-1], "")
                    core.keyPressValue = None
            core.Draw.text((255, 255, 255), " Name : " + self.name, Vector2(450, 600), 25), self.pygameFont

            if not core.memory("textureE").ready:
                core.memory("textureE").load()
            core.memory("textureE").show()

    def pause(self):
        core.memory("screen", Screen.PAUSE)
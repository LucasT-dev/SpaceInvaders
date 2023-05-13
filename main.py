# This is a sample Python script.
import sys

import pygame
from pygame import Vector2, mixer

import core
from SpaceInvader import Screen
from SpaceInvader.Enemies import Enemies
from SpaceInvader.Projectile import Projectile
from SpaceInvader.Vaisseau import Vaisseau
from SpaceInvader.Wall import Wall


#https://www.crazygames.fr/jeu/space-invaders

def setup():
    print("Setup START---------")
    core.WINDOW_SIZE = [1000, 800]
    core.fps = 60
    core.memory("screen", Screen.Screen.MAIN.value)
    core.setBgColor((0, 0, 0))
    core.setTitle("Space Invaders")

    core.memory("vaisseau", Vaisseau())

    core.memory("projectile", [])
    core.memory("Eprojectile", [])

    core.memory("wall", [])
    core.memory("enemies", [])

    mixer.init()
    # Loading the song
    mixer.music.load("./SpaceInvader/ressource/song.mp3")
    # Setting the volume
    mixer.music.set_volume(0.7)
    # Start playing the song
    mixer.music.play(-1)


    # core.memory("texture", core.Texture("./ressource/img.png", Vector2(-200, -200), 0, (1000, 1000)))
    core.memory("textureP", core.Texture("./SpaceInvader/ressource/Play.png", Vector2(320, 100), 0, (1500, 1000)))
    core.memory("textureS", core.Texture("./SpaceInvader/ressource/Setting.png", Vector2(280, 200), 0, (1500, 1000)))
    core.memory("textureE", core.Texture("./SpaceInvader/ressource/Exit.png", Vector2(340, 300), 0, (1500, 1000)))
    core.memory("textureV", core.Texture("./SpaceInvader/ressource/PlayerVaisseau.png", Vector2(500, 700), 0, (70, 70)))
    core.memory("textureRed_En", core.Texture("./SpaceInvader/ressource/Red_En.png", Vector2(0, 0), 10, (70, 70)))
    core.memory("textureGreen_En", core.Texture("./SpaceInvader/ressource/Green_En.png", Vector2(0, 0), 10, (70, 70)))

def edge(j):
    if j.position.x < 0:
        j.position.x = 0
    if j.position.x > core.WINDOW_SIZE[0]-30:
        j.position.x = core.WINDOW_SIZE[0]-30

def run():
    core.cleanScreen()

    if core.memory("screen").__eq__(Screen.Screen.MAIN.value):

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

        core.setBgColor((0, 0, 0))

        core.Draw.text((255, 255, 255), "Score :" + str(core.memory("vaisseau").score), Vector2(800, 20), 25, "Arial")
        core.Draw.text((255, 255, 255), "LifePoint :" + str(core.memory("vaisseau").lifePoint), Vector2(800, 45), 25, "Arial")
        core.Draw.text((255, 255, 255), "Position :" + str(core.memory("vaisseau").position), Vector2(800, 70), 25, "Arial")

        for i in core.memory("wall"):
            i.draw()

        for i in core.memory("enemies"):
            i.draw()
            #enemies launch projectile

        for i in core.memory("Eprojectile"):
            i.moveEnemiesProjectile()

        for i in core.memory("projectile"):

            if (i.position.y < 10):
                core.memory("projectile").remove(i)

            i.movePlayerProjectile()

            # player projectil shut walls
            for j in core.memory("wall"):

                d = Vector2.distance_to(i.position, j.position)

                if (d < 10):

                    core.memory("projectile").remove(i)
                    core.memory("wall").remove(j)

            #player projectil shut enemies
            for k in core.memory("enemies"):

                d = Vector2.distance_to(i.position, k.position)

                if (d < 10):

                    core.memory("projectile").remove(i)
                    core.memory("enemies").remove(k)

                    core.memory("vaisseau").addPoint(k.lifePoint)

            for l in core.memory("Eprojectile"):

                d = Vector2.distance_to(i.position, l.position)

                if (d < 10):
                    core.memory("projectile").remove(i)
                    core.memory("Eprojectile").remove(j)

            i.draw()

        keys = pygame.key.get_pressed()
        keys1 = core.getkeyPress()

        print(keys1)

        #Control
        if keys[pygame.K_LEFT]:
            core.memory("vaisseau").moveLeft()
        if keys[pygame.K_RIGHT]:
            core.memory("vaisseau").moveRight()

        if keys1 and keys[pygame.K_SPACE]:
            print("LAUNCH projectile")
            core.keyPress = False

            if (len(core.memory("projectile")) < 5 ):
                core.memory("projectile").append(Projectile(Vector2(core.memory("vaisseau").position.x+32, core.memory("vaisseau").position.y), 5))

        edge(core.memory("vaisseau"))


    if core.memory("screen").__eq__(Screen.Screen.SETTING.value):

        if not core.memory("textureE").ready:
            core.memory("textureE").load()
        core.memory("textureE").show()

    if core.memory("screen").__eq__(Screen.Screen.GAMEOVER.value):
        core.Draw.circle((155, 0, 155), Vector2(0, 0), 200)

    # if not core.memory("texture").ready:
    #     core.memory("texture").load()
    # core.memory("texture").show()

    # MAIN
    if core.getMouseLeftClick() and core.memory("screen").__eq__(Screen.Screen.MAIN.value):
        core.getMouseLeftClick()
        print(pygame.mouse.get_pos())

        # Bottom START
        if 330 < pygame.mouse.get_pos()[0] < 650 and 110 < pygame.mouse.get_pos()[1] < 200:
            print("START")
            core.memory("screen", Screen.Screen.INGAME.value)
            core.mouseclickL = False

            #Wall
            n = 10
            l = 1000
            d = (l/n)
            d1 = (l/n) - (l/n)/2

            for i in range(n):
                core.memory("wall").append(Wall(Vector2((((i+1)*d)-d1, 600))))

            #Enemies
            n = 13
            l = 1000
            d = (l / n)
            d1 = (l / n) - (l / n) / 2

            for i in range(n):
                core.memory("enemies").append(Enemies(Vector2((((i + 1) * d) - d1, 200)), core.memory("textureRed_En"), 10))

            n = 10
            l = 1000
            d = (l / n)
            d1 = (l / n) - (l / n) / 2

            for i in range(n):
                core.memory("enemies").append(Enemies(Vector2((((i + 1) * d) - d1, 300)), core.memory("textureGreen_En"), 20))



        # Bottom SETTING
        if 290 < pygame.mouse.get_pos()[0] < 700 and 200 < pygame.mouse.get_pos()[1] < 290:
            print("SETTING")
            core.memory("screen", Screen.Screen.SETTING.value)
            core.mouseclickL = False

        # Bottom EXIT
        if 350 < pygame.mouse.get_pos()[0] < 650 and 300 < pygame.mouse.get_pos()[1] < 390:
            print("EXIT")
            sys.exit()

    # SETTING
    if core.getMouseLeftClick() and core.memory("screen").__eq__(Screen.Screen.SETTING.value):

        if 350 < pygame.mouse.get_pos()[0] < 650 and 300 < pygame.mouse.get_pos()[1] < 390:
            print("EXIT2")
            core.memory("screen", Screen.Screen.MAIN.value)
            core.mouseclickL = False


core.main(setup, run)

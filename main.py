# This is a sample Python script.
import sys
import time
from random import randrange

import pygame
from pygame import Vector2, mixer
from pygame.rect import Rect

import core
from SpaceInvader import Screen
from SpaceInvader.Enemies import Enemies
from SpaceInvader.Partie import Partie
from SpaceInvader.Projectile import Projectile
from SpaceInvader.Vaisseau import Vaisseau
from SpaceInvader.Wall import Wall


# https://www.crazygames.fr/jeu/space-invaders

def setup():
    print("Setup START---------")

    core.memory("partie", Partie())

    core.WINDOW_SIZE = [1000, 800]
    core.fps = 60
    core.setTitle("Space Invaders")

    core.memory("screen", Screen.Screen.MENU.value)
    core.memory("vaisseau", Vaisseau())

    core.memory("projectile", [])
    core.memory("Eprojectile", [])

    core.memory("wall", [])
    core.memory("enemies", [])

    #mixer.init()
    # Loading the song
    #mixer.music.load("./SpaceInvader/ressource/song.mp3")
    # Setting the volume
    #mixer.music.set_volume(0.7)
    # Start playing the song
    #mixer.music.play(-1)

    # core.memory("texture", core.Texture("./ressource/img.png", Vector2(-200, -200), 0, (1000, 1000)))
    core.memory("textureL", core.Texture("./SpaceInvader/ressource/Logo.png", Vector2(260, 25), 0, (500, 350)))
    core.memory("textureP", core.Texture("./SpaceInvader/ressource/Play.png", Vector2(330, 450), 0, (1500, 1000)))
    core.memory("textureS", core.Texture("./SpaceInvader/ressource/Setting.png", Vector2(280, 575), 0, (1500, 1000)))
    core.memory("textureE", core.Texture("./SpaceInvader/ressource/Exit.png", Vector2(340, 700), 0, (1500, 1000)))
    core.memory("textureV", core.Texture("./SpaceInvader/ressource/PlayerVaisseau.png", Vector2(500, 700), 0, (70, 70)))
    core.memory("textureRed_En", core.Texture("./SpaceInvader/ressource/Red_En.png", Vector2(0, 0), 10, (70, 70)))
    core.memory("textureGreen_En", core.Texture("./SpaceInvader/ressource/Green_En.png", Vector2(0, 0), 10, (70, 70)))


def edge(j):
    if j.position.x < 0:
        j.position.x = 0
    if j.position.x > core.WINDOW_SIZE[0] - 30:
        j.position.x = core.WINDOW_SIZE[0] - 30

def run():
    core.cleanScreen()

    core.memory("partie").update()

    ##lorsque tout les ennemies ont été tué on n'en remet
    if len(core.memory("enemies")) == 0:
          core.memory("partie").end()

    for i in core.memory("wall"):
        i.draw()

    for i in core.memory("enemies"):

        i.draw()
        i.launchProjectile()
        # enemies launch projectile

    for i in core.memory("Eprojectile"):
        i.draw()
        i.moveEnemiesProjectile()

        for j in core.memory("wall"):

            d = Vector2.distance_to(i.position, j.position)

            if (d < 10):
                core.memory("Eprojectile").remove(i)
                core.memory("wall").remove(j)

        d = Vector2.distance_to(i.position, core.memory("vaisseau").position)

        if (d < 20):
            core.memory("screen", Screen.Screen.GAMEOVER.value)

        if i.position.y > 800:
            core.memory("Eprojectile").remove(i)

    for i in core.memory("projectile"):

        i.movePlayerProjectile()

        if i.position.y < 10:
            core.memory("projectile").remove(i)

        # player projectil shot walls
        for j in core.memory("wall"):

            d = Vector2.distance_to(i.position, j.position)

            if d < 10:
                core.memory("projectile").remove(i)
                core.memory("wall").remove(j)

        # player projectile shot enemies
        for k in core.memory("enemies"):

            d = Vector2.distance_to(i.position, k.position)

            if d < 10:
                core.memory("projectile").remove(i)
                core.memory("enemies").remove(k)

                core.memory("vaisseau").addPoint(k.lifePoint)

        # player projectile shot enemies projectile
        for l in core.memory("Eprojectile"):

            d = Vector2.distance_to(i.position, l.position)

            if d < 7:
                core.memory("projectile").remove(i)
                core.memory("Eprojectile").remove(l)

        i.draw()

    keys = pygame.key.get_pressed()
    keys1 = core.getkeyPress()

    # Control
    if keys[pygame.K_LEFT]:
        core.memory("vaisseau").moveLeft()
    if keys[pygame.K_RIGHT]:
        core.memory("vaisseau").moveRight()

    if keys1 and keys[pygame.K_SPACE]:
        core.keyPress = False

    edge(core.memory("vaisseau"))

    startButton = Rect(330, 450, 335, 100)
    core.Draw.rect((0, 0, 255,0), startButton)

    settingButton = Rect(280, 575, 430, 90)
    core.Draw.rect((255, 0, 0,0), settingButton)

    exitButton = Rect(350, 700, 300, 90)
    core.Draw.rect((0, 255, 0,0), exitButton)

    # MAIN
    if core.getMouseLeftClick() and core.memory("screen").__eq__(Screen.Screen.MENU.value):
        core.getMouseLeftClick()
        print(pygame.mouse.get_pos())

        if startButton.collidepoint(core.getMouseLeftClick()):
            print("START")
            core.memory("screen", Screen.Screen.INGAME.value)
            core.mouseclickL = False

        if settingButton.collidepoint(core.getMouseLeftClick()):
            print("SETTING")
            core.memory("screen", Screen.Screen.SETTING.value)
            core.mouseclickL = False

        if exitButton.collidepoint(core.getMouseLeftClick()):
            print("EXIT")
            sys.exit()
        # Bottom START



        if 330 < pygame.mouse.get_pos()[0] < 650 and 110 < pygame.mouse.get_pos()[1] < 200:
            print("START")
            core.memory("screen", Screen.Screen.INGAME.value)
            core.mouseclickL = False

            core.memory("partie").start
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
            core.memory("screen", Screen.Screen.MENU.value)
            core.mouseclickL = False

    # GAME OVER
    if core.getMouseLeftClick() and core.memory("screen").__eq__(Screen.Screen.GAMEOVER.value):

        if 350 < pygame.mouse.get_pos()[0] < 650 and 300 < pygame.mouse.get_pos()[1] < 390:
            print("EXIT2")
            core.memory("screen", Screen.Screen.MENU.value)
            core.memory("vaisseau").score = 0
            core.memory("projectile").clear()
            core.memory("Eprojectile").clear()
            core.memory("enemies").clear()
            core.mouseclickL = False


core.main(setup, run)

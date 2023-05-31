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

    core.memory("wall", [])
    core.memory("enemies", [])

    # mixer.init()
    # Loading the song
    # mixer.music.load("./SpaceInvader/ressource/song.mp3")
    # Setting the volume
    # mixer.music.set_volume(0.7)
    # Start playing the song
    # mixer.music.play(-1)

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

    core.memory("vaisseau").updateProjectile()

    ##lorsque tout les ennemies ont été tué on n'en remet
    if len(core.memory("enemies")) == 0:
        pass
        #core.memory("partie").end()

    for i in core.memory("wall"):

        i.draw()

    for i in core.memory("enemies"):

        enemiesRect = Rect(i.position.x, i.position.y, 20, 12)
        core.Draw.rect((255, 255, 255, 150), enemiesRect)

        i.update()

    vaisseauRect = Rect(core.memory("vaisseau").position.x + 15, core.memory("vaisseau").position.y + 10, 40, 60)
    core.Draw.rect((255, 255, 255, 150), vaisseauRect)

    ##Collision

    exitButton = Rect(350, 700, 300, 90)
    core.Draw.rect((0, 255, 0, 0), exitButton)


    keys = pygame.key.get_pressed()
    keys1 = core.getkeyPress()

    # Control
    if keys[pygame.K_LEFT]:
        core.memory("vaisseau").moveLeft()
    if keys[pygame.K_RIGHT]:
        core.memory("vaisseau").moveRight()

    if keys1 and keys[pygame.K_SPACE]:
        core.keyPress = False
        print("SPACE")
        core.memory("vaisseau").addProjectile()

    edge(core.memory("vaisseau"))

    startButton = Rect(330, 450, 335, 100)
    core.Draw.rect((0, 0, 255, 0), startButton)

    settingButton = Rect(280, 575, 430, 90)
    core.Draw.rect((255, 0, 0, 0), settingButton)

    exitButton = Rect(350, 700, 300, 90)
    core.Draw.rect((0, 255, 0, 0), exitButton)

    # MAIN
    if core.getMouseLeftClick() and core.memory("screen").__eq__(Screen.Screen.MENU.value):
        core.getMouseLeftClick()
        print(pygame.mouse.get_pos())

        if startButton.collidepoint(core.getMouseLeftClick()):
            print("START")
            core.memory("screen", Screen.Screen.INGAME.value)
            core.memory("partie").start()
            core.mouseclickL = False

        elif settingButton.collidepoint(core.getMouseLeftClick()):
            print("SETTING")
            core.memory("screen", Screen.Screen.SETTING.value)
            core.mouseclickL = False

        elif exitButton.collidepoint(core.getMouseLeftClick()):
            print("EXIT")
            sys.exit()
        # Bottom START

    # SETTING
    if core.getMouseLeftClick() and core.memory("screen").__eq__(Screen.Screen.SETTING.value):

        if exitButton.collidepoint(core.getMouseLeftClick()):
            print("EXIT2")
            core.memory("screen", Screen.Screen.MENU.value)
            core.mouseclickL = False

    # GAME OVER
    if core.getMouseLeftClick() and core.memory("screen").__eq__(Screen.Screen.GAMEOVER.value):

        if 350 < pygame.mouse.get_pos()[0] < 650 and 300 < pygame.mouse.get_pos()[1] < 390:
            print("EXIT2")
            core.memory("screen", Screen.Screen.MENU.value)
            core.memory("vaisseau").score = 0
            core.memory("enemies").clear()
            core.mouseclickL = False


core.main(setup, run)

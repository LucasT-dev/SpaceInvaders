# This is a sample Python script.
import os.path
import sys

import pygame
from pygame import Vector2, mixer
from pygame.rect import Rect

import core
from SpaceInvader.Partie import Partie
from SpaceInvader.ScoreManager import ScoreManager
from SpaceInvader.Screen import Screen
from SpaceInvader.Vaisseau import Vaisseau


# https://www.crazygames.fr/jeu/space-invaders

def setup():
    print("Setup START---------")

    core.memory("partie", Partie())

    core.WINDOW_SIZE = [1000, 800]
    core.fps = 60
    core.setTitle("Space Invaders")

    core.memory("music", core.Sound("./SpaceInvader/ressource/Sons/Fond.mp3"))
    #core.memory("sonTir", pygame.mixer_music.load("./SpaceInvader/ressource/Sons/sonTir.wav"))
    core.memory("screen", Screen.MENU)
    core.memory("wall", [])
    core.memory("enemies", [])
    core.memory("score", [])

    ScoreManager.load( ScoreManager,"score.txt" )

    core.memory("bgJeu", core.Texture("./SpaceInvader/ressource/BackgroundJeu.png", Vector2(0, 0), 0, (1000, 800)))
    core.memory("bgMenu", core.Texture("./SpaceInvader/ressource/BackgroundMenu.png", Vector2(0, 0), 0, (1000, 800)))

    core.memory("texturePa", core.Texture("./SpaceInvader/ressource/Pause.png", Vector2(300, 100), 0, (400, 100)))
    core.memory("textureL", core.Texture("./SpaceInvader/ressource/Logo.png", Vector2(260, 25), 0, (500, 350)))
    core.memory("textureP", core.Texture("./SpaceInvader/ressource/Play.png", Vector2(330, 450), 0, (1500, 1000)))
    core.memory("textureS", core.Texture("./SpaceInvader/ressource/Score.png", Vector2(335, 590), 0, (330, 80)))
    core.memory("textureE", core.Texture("./SpaceInvader/ressource/Exit.png", Vector2(340, 700), 0, (1500, 1100)))

    core.memory("textureV", core.Texture("./SpaceInvader/ressource/PlayerVaisseau.png", Vector2(500, 700), 0, (70, 70)))
    core.memory("textureRed_En", core.Texture("./SpaceInvader/ressource/Red_En.png", Vector2(0, 0), 10, (140, 140)))
    core.memory("textureGreen_En", core.Texture("./SpaceInvader/ressource/Green_En.png", Vector2(0, 0), 10, (100, 100)))
    core.memory("textureWall", core.Texture("./SpaceInvader/ressource/Wall.png", Vector2(0, 0), 0, (60, 60)))

    core.memory("missileV", core.Texture("./SpaceInvader/ressource/MissileV.png", Vector2(0, 0), 0, (20, 27)))
    core.memory("projectileG", core.Texture("./SpaceInvader/ressource/ProjectileG.png", Vector2(0, 0), 0, (20, 27)))
    core.memory("projectileR", core.Texture("./SpaceInvader/ressource/ProjectileR.png", Vector2(0, 0), 0, (20, 27)))
    core.memory("explosion", core.Texture("./SpaceInvader/ressource/Explosion.png", Vector2(0, 0), 0, (100, 100)))


def edge(j):
    if j.position.x < 0 - 30:
        j.position.x = 1000 - 31
    if j.position.x > core.WINDOW_SIZE[0] - 30:
        j.position.x = 0 + 31
def edgeEnnemis(t):
    for i in t:
        if i.position.x<0:
            i.position.x = 0
        if i.position.x>core.WINDOW_SIZE[0]:
            i.position.x = core.WINDOW_SIZE[0]
    pass

def run():

    core.cleanScreen()

    core.memory("partie").update()
    edgeEnnemis(core.memory("enemies"))

    if core.memory("screen") == Screen.INGAME:

        core.memory("vaisseau").updateProjectile()

        # Control
        keys = pygame.key.get_pressed()
        keys1 = core.getkeyPress()

        #print(core.getkeyPressValue())

        if core.getKeyPressList("SPACE") and keys1:
            core.keyPress = False
            core.memory("vaisseau").addProjectile()
            #core.memory("sonTir").play()

        if keys[pygame.K_LEFT]:
            core.memory("vaisseau").moveLeft()
        if keys[pygame.K_RIGHT]:
            core.memory("vaisseau").moveRight()
        if keys[pygame.K_ESCAPE]:
            core.memory("partie").pause()

        ##lorsque tout les ennemies ont été tué on n'en remet
        if len(core.memory("enemies")) == 0:
            core.memory("partie").start()
            core.memory("partie").speedCoef += 0.5
            core.memory("partie").coefLaunchProjectile += 2


        for i in core.memory("wall"):
            i.draw()

        for i in core.memory("enemies"):
            i.update()

        core.memory("partie").collide()

        edge(core.memory("vaisseau"))


    # MENU
    if core.memory("screen") == Screen.MENU:

        if core.getMouseLeftClick():

            startButton = Rect(330, 450, 335, 100)
            core.Draw.rect((0, 0, 255, 0), startButton)

            scoreButton = Rect(330, 585, 335, 100)
            core.Draw.rect((255, 0, 0, 0), scoreButton)

            exitButton = Rect(350, 700, 300, 90)
            core.Draw.rect((0, 255, 0, 0), exitButton)

            if startButton.collidepoint(core.getMouseLeftClick()):
                core.memory("vaisseau", Vaisseau())
                core.memory("screen", Screen.INGAME)
                core.memory("partie").start()
                core.memory("music").start()
                core.mouseclickL = False

            elif scoreButton.collidepoint(core.getMouseLeftClick()):
                core.memory("screen", Screen.SCOREBOARD)
                core.mouseclickL = False

            elif exitButton.collidepoint(core.getMouseLeftClick()):
                ScoreManager.write(ScoreManager,"score.txt")
                sys.exit()
            # Bottom START

    # SCOREBOARD
    if core.memory("screen")==Screen.SCOREBOARD:
        if core.getMouseLeftClick():

            exitButton = Rect(350, 700, 300, 90)
            core.Draw.rect((0, 255, 0, 0), exitButton)


            if exitButton.collidepoint(core.getMouseLeftClick()):
                core.memory("screen", Screen.MENU)
                core.mouseclickL = False

    # GAME OVER
    if core.memory("screen") == Screen.GAMEOVER:
        core.memory("music").pause()
        core.memory("music").rewind()
        if core.getMouseLeftClick():

            exitButton = Rect(350, 700, 300, 90)
            core.Draw.rect((0, 255, 0, 0), exitButton)

            if exitButton.collidepoint(core.getMouseLeftClick()):

                ScoreManager.insert(ScoreManager((core.memory("partie").name), core.memory("partie").totalScore))
                core.memory("enemies").clear()
                core.memory("wall").clear()
                core.memory("partie", Partie())
                core.memory("screen", Screen.MENU)
                core.mouseclickL = False
    # PAUSE
    if core.memory("screen") == Screen.PAUSE:
        core.memory("music").pause()
        if core.getMouseLeftClick():
            startButton = Rect(330, 450, 335, 100)
            core.Draw.rect((0, 0, 255, 0), startButton)

            exitButton = Rect(350, 700, 300, 90)
            core.Draw.rect((0, 255, 0, 0), exitButton)

            if startButton.collidepoint(core.getMouseLeftClick()):
                core.memory("vaisseau", Vaisseau())
                core.memory("screen", Screen.INGAME)
                core.memory("son").start()
                core.mouseclickL = False
            elif exitButton.collidepoint(core.getMouseLeftClick()):
                core.memory("screen", Screen.GAMEOVER )
                core.mouseclickL = False



core.main(setup, run)

# This is a sample Python script.
import pygame
from pygame import Vector2

import core
from SpaceInvader import Screen


# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def setup():

    print("Setup START---------")
    core.WINDOW_SIZE = [1000, 800]
    core.fps = 60
    core.memory("screen", Screen.Screen.MAIN)
    core.setBgColor((255, 255, 255))
    core.setTitle("Space Invaders")

    #core.memory("texture", core.Texture("./ressource/img.png", Vector2(-200, -200), 0, (1000, 1000)))
    core.memory("textureP", core.Texture("./SpaceInvader/ressource/Play.png", Vector2(320, 100), 0, (1500, 1000)))
    core.memory("textureS", core.Texture("./SpaceInvader/ressource/Setting.png", Vector2(280, 200), 0, (1500, 1000)))
    core.memory("textureE", core.Texture("./SpaceInvader/ressource/Exit.png", Vector2(340, 300), 0, (1500, 1000)))

def run():

    core.cleanScreen()

    if core.memory("screen").__eq__(Screen.Screen.MAIN):

        buttomHeight = 50 #Largeur du bouton
        buttomWidth = 500 #Longueur du bouton

        #PLAYING

        if not core.memory("textureP").ready:
            core.memory("textureP").load()
        core.memory("textureP").show()

        if not core.memory("textureS").ready:
            core.memory("textureS").load()
        core.memory("textureS").show()

        if not core.memory("textureE").ready:
            core.memory("textureE").load()
        core.memory("textureE").show()

    if core.memory("screen").__eq__(Screen.Screen.INGAME):
        pass

    if core.memory("screen").__eq__(Screen.Screen.SETTING):
        pass

    if core.memory("screen").__eq__(Screen.Screen.GAMEOVER):
        pass

   # if not core.memory("texture").ready:
   #     core.memory("texture").load()
   # core.memory("texture").show()

    if core.getMouseLeftClick() and core.memory("screen").__eq__(Screen.Screen.MAIN):
        core.getMouseLeftClick()
        print(pygame.mouse.get_pos())

        # Bottom START
        if 330 < pygame.mouse.get_pos()[0] < 650 and 110 < pygame.mouse.get_pos()[1] < 200:
            print("START")
            core.memory("screen", Screen.Screen.INGAME)
            core.mouseclickL = False

        # Bottom SETTING
        if 290 < pygame.mouse.get_pos()[0] < 700 and 200 < pygame.mouse.get_pos()[1] < 290:
            print("SETTING")
            core.memory("screen", Screen.Screen.SETTING)
            core.mouseclickL = False

        # Bottom EXIT
        if 350 < pygame.mouse.get_pos()[0] < 650 and 300 < pygame.mouse.get_pos()[1] < 390:
            print("EXIT")
            sys.exit()
        pass


core.main(setup, run)
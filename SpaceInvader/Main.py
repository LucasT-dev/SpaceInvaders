from pygame import Vector2

import core
from SpaceInvader import Screen


def setup():

    print("Setup START---------")
    core.WINDOW_SIZE = [1000, 800]
    core.fps = 60
    core.memory("screen", Screen.Screen.MAIN)
    core.setBgColor((255, 255, 255))


    #core.memory("texture", core.Texture("./ressource/img.png", Vector2(-200, -200), 0, (1000, 1000)))
    core.memory("textureP", core.Texture("./ressource/Play.png", Vector2(320, 100), 0, (1500, 1000)))
    core.memory("textureS", core.Texture("./ressource/Setting.png", Vector2(280, 200), 0, (1500, 1000)))
    core.memory("textureE", core.Texture("./ressource/Exit.png", Vector2(340, 300), 0, (1500, 1000)))

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

        p1 = Vector2(250, 100) #Point en haut a gauche a editer
        p2 = Vector2(p1.x, p1.y + buttomHeight)
        p3 = Vector2(p1.x + buttomWidth, p1.y + buttomHeight)
        p4 = Vector2(p1.x + buttomWidth, p1.y)
        p5 = Vector2(p1.x + 200, p1.y + 10) #Text position

        #core.Draw.polygon((255, 255, 255), ((p1), (p2), (p3), (p4)))
        #core.Draw.text((255, 0 , 255), "PLAYING", p5, 30, "Arial")

        #SETTING
        p1 = Vector2(250, 200)  # Point en haut a gauche a editer
        p2 = Vector2(p1.x, p1.y + buttomHeight)
        p3 = Vector2(p1.x + buttomWidth, p1.y + buttomHeight)
        p4 = Vector2(p1.x + buttomWidth, p1.y)
        p5 = Vector2(p1.x + 200, p1.y + 10)  # Text position

        #core.Draw.polygon((255, 255, 255), ((p1), (p2), (p3), (p4)))
        #core.Draw.text((255, 0, 255), "SETTING", p5, 30, "Arial")

        # EXIT
        p1 = Vector2(250, 300)  # Point en haut a gauche a editer
        p2 = Vector2(p1.x, p1.y + buttomHeight)
        p3 = Vector2(p1.x + buttomWidth, p1.y + buttomHeight)
        p4 = Vector2(p1.x + buttomWidth, p1.y)
        p5 = Vector2(p1.x + 220, p1.y + 10)  # Text position

        #core.Draw.polygon((255, 255, 255), ((p1), (p2), (p3), (p4)))
        #core.Draw.text((255, 0, 255), "EXIT", p5, 30, "Arial")

    if core.memory("screen").__eq__(Screen.Screen.INGAME):
        pass

    if core.memory("screen").__eq__(Screen.Screen.SETTING):
        pass

    if core.memory("screen").__eq__(Screen.Screen.GAMEOVER):
        pass

    if core.getMouseLeftClick():
        core.getMouseLeftClick()
        pass

   # if not core.memory("texture").ready:
   #     core.memory("texture").load()
   # core.memory("texture").show()



core.main(setup, run)
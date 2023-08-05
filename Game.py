from direct.showbase.ShowBase import ShowBase

from direct.actor.Actor import Actor
from panda3d.core import CollisionTraverser, CollisionHandlerPusher, CollisionSphere, CollisionTube, CollisionNode
from panda3d.core import AmbientLight, DirectionalLight
from panda3d.core import Vec4, Vec3
from panda3d.core import WindowProperties

from direct.gui.DirectGui import *

# from GameObject import *

# from menus import Menus

import random

class Game(ShowBase):
    def __init__(self,manager,size):
        # self.state = state
        ShowBase.__init__(self)
        # self.menus = Menus()
        # self.menus.setdesktop(manager,size=size)
        self.setupPanda()
        self.setscene()
        # self.setkeys()
        self.setcollisions()
        
        # self.score = 0

        # self.scoreUI = OnscreenText(text = "0",
        #                             pos = (-1.3, 0.825),
        #                             mayChange = True,
        #                             align = TextNode.ALeft,
        #                             font = base.font)

        # self.healthIcons = []
        # # self.spawning()
        self.players = {}
        self.enemies = {}

    def setupPanda(self):
        # self.disableMouse()

        # self.setmonitor()

        self.exitFunc = self.cleanup
        
    def setscene(self):
        pass
    
    def setcollisions(self):
        pass

    def cleanup(self):

        # GameObject.cleanup(self)

    def update(self,dt,events):#get size, update size if it changes, but update that here
        # for event in events:
            # if event in self.menus.register:
                # self.updateTask = taskMgr.add(self.menus.register[event](),"event")
        
        for value in self.players.values():
            self.updateTask = taskMgr.add(value.update(dt), "update")

        for value in self.enemies.values():
            self.updateTask = taskMgr.add(value.update(dt), "update")


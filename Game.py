from direct.showbase.ShowBase import ShowBase

from direct.actor.Actor import Actor
from panda3d.core import CollisionTraverser, CollisionHandlerPusher, CollisionSphere, CollisionTube, CollisionNode
from panda3d.core import Spotlight,OrthographicLens,PerspectiveLens
from panda3d.core import Vec4, Vec3
from panda3d.core import WindowProperties

from direct.gui.DirectGui import *

from Room import makeRoom

from GameObject import Player

# from menus import Menus

class Game(ShowBase):
    def __init__(self,manager=None,size=None,apppath=None):
        # self.state = state
        ShowBase.__init__(self)
        self.apppath = apppath
        self.setupPanda(size)
        self.rooms = makeRoom()
        self.setscene()
        # self.setkeys()
        self.setcollisions()
        self.actor = Player()
        self.players = {}
        self.enemies = {}

    def setupPanda(self,size=None):
        # self.disableMouse()
        properties = WindowProperties()
        if size != None and size[2] > 1000:
            properties.setSize(size[2], size[3])
        else:
            properties.setSize(1000,750)
        self.win.requestProperties(properties)

        self.exitFunc = self.cleanup
        
    def setscene(self):
        # lens = OrthographicLens()
        # lens.setFilmSize(20, 15)  # Or whatever is appropriate for your scene
        # base.cam.node().setLens(lens)
        base.camera.setPos(0, 15, 20)
        # base.camera.setHpr(0, -70, 0)
        base.camera.lookAt(0,0,0)
        base.useDrive()
        slight = Spotlight('slight')
        slight.setColor((1, 1, 1, 1))
        lens = PerspectiveLens()
        slight.setLens(lens)
        slnp = render.attachNewNode(slight)
        # slnp.setPos(0, -10, 10)
        slnp.setPos(0, 15, 20)
        slnp.lookAt(0, 0, 0)

        # slnp.lookAt(self.Player) # look at character
        render.setLight(slnp)
    
    def setcollisions(self):
        pass

    def cleanup(self):
        pass
        # GameObject.cleanup(self)

    def update(self,dt,events):#get size, update size if it changes, but update that here
        for event in events:
            if event in self.menus.register:
                self.updateTask = taskMgr.add(self.menus.register[event](),"event")
        
        for value in self.players.values():
            self.updateTask = taskMgr.add(value.update(dt), "update")

        for value in self.enemies.values():
            self.updateTask = taskMgr.add(value.update(dt), "update")

if __name__ == "__main__":
    game = Game()
    game.run()
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from direct.task import Task
from panda3d.core import CollisionTraverser, CollisionHandlerPusher, CollisionSphere, CollisionTube, CollisionNode
from panda3d.core import Spotlight,OrthographicLens,PerspectiveLens
from panda3d.core import Vec4, Vec3
from panda3d.core import WindowProperties

from direct.gui.DirectGui import *

from Room import generaterooms

from GameObject import Player

class Game(ShowBase):
    def __init__(self,manager=None,size=None,apppath=None):
        ShowBase.__init__(self)
        self.apppath = apppath
        self.playGame(size)
    
    def setupPanda(self,size=None):
        self.disableMouse()
        properties = WindowProperties()
        if size != None and size[2] > 1000:
            properties.setSize(size[2], size[3])
        else:
            properties.setSize(1000,750)
        self.win.requestProperties(properties)
        self.exitFunc = self.cleanup
        
    #sets the lens and spotlight
    def setscene(self):
        lens = OrthographicLens()
        lens.setFilmSize(20, 15)
        base.cam.node().setLens(lens)
        
        slight = Spotlight('slight')
        slight.setColor((1, 1, 1, 1))
        lens = PerspectiveLens()
        slight.setLens(lens)
        slnp = self.players['primary'].move.attachNewNode(slight)
        slnp.setPos(0, -10, 10)
        # slnp.setPos(0, 15, 20)
        slnp.lookAt(0, 0, 0)
        # slnp.lookAt(self.Player) # look at character
        render.setLight(slnp)

    def playGame(self,size):
        self.setupPanda(size)
        self.rooms = generaterooms()
        self.players = {'primary': Player()}
        self.setscene()
        # self.setkeys()
        self.setcollisions()
        
        self.enemies = {}
        taskMgr.add(self.update,"update-whole-game")
    
    def setcollisions(self):
        pass

    def cleanup(self):
        pass
        # GameObject.cleanup(self)
    
    # updates the whole gameplay. 
    # Call anything you want to change during a match here
    def update(self,task):#get size, update size if it changes, but update that here
        dt = globalClock.getDt()
        # for event in events:
        #     if event in self.menus.register:
        #         self.updateTask = taskMgr.add(self.menus.register[event](),"event")
        for player in self.players.keys():
            taskMgr.add(self.players[player].update, f'update-{player}',extraArgs=[dt])

        for enemy in self.enemies.keys():
            taskMgr.add(self.enemies[enemy].update, f'update-{enemy}',extraArgs=[dt],appendTask=True)
        # base.cam.setPos(0, -15, 20)#TODO set to player location
        # base.cam.lookAt(0,0,0)#TODO set to look at player location
        return task.cont

if __name__ == "__main__":
    game = Game()
    game.run()
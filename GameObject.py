from panda3d.core import Vec4, Vec3, Vec2, Plane, Point3, BitMask32
from direct.actor.Actor import Actor
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage
from panda3d.core import NodePath
from panda3d.core import TextNode
from panda3d.core import AudioSound
from panda3d.core import PointLight
from panda3d.core import CollisionNode,CollisionSphere
from State import ActorFSM
from sys import path
from Input import Movement
from open_source.updatepos import updatepos

FRICTION = 150.0

class GameObject():
    def __init__(self,pos=Vec3(0, 0, 0),modelName='ball',modelAnims=None,maxHealth=20,maxSpeed=20,maxMana=None,maxStamina=None,parent=None,move=None):
        if modelAnims is None:
            self.actor = Actor(path[0]+'/models/ball.bam', {
                    'walk': path[0]+'/models/bouncing ball.bam',
                    'jump': path[0]+'/models/jumping ball.bam'
                })
        else:
            self.actor = modelAnims
        if not move:
            self.move = self.actor
        else:
            self.move = move
        if not parent:
            self.actor.reparentTo(render)
        else:
            self.actor.reparentTo(parent)
        self.setSpeedAcc(maxHealth,maxSpeed)
        self.addCollider()
        # self.actor = Actor(modelName, modelAnims)
        # self.actor.reparentTo(render)
        self.actor.setPos(pos)
        self.actor.setDepthTest(False)

        # colliderNode = CollisionNode(colliderName)
        # colliderNode.addSolid(CollisionSphere(0, 0, 0, 0.3))
        # self.collider = self.actor.attachNewNode(colliderNode)
        # self.collider.setPythonTag("owner", self)
    
    def update(self,dt):
        updatepos(self.move,self.velocity,self.maxSpeed,FRICTION,self.state.state,dt)

    def setSpeedAcc(self,maxHealth,maxSpeed):
        self.maxSpeed = maxSpeed
        self.velocity = Vec3(0, 0, 0)
        self.acceleration = 300.0
        self.jump = 20

        self.maxHealth = maxHealth
        self.health = maxHealth

    def addCollider(self):
        capsule = CollisionSphere(0, 0, 3, 3)
        cnodePath = self.move.attachNewNode(CollisionNode('gameobject'))
        cnodePath.node().addSolid(capsule)

class Player(GameObject):
    def __init__(self,pos=[0,0,0]):
        playernode = NodePath('PlayerPos')
        playernode.setPos(pos[0],pos[1],pos[2])
        playernode.reparentTo(render)
        GameObject.__init__(self,parent=playernode,move=playernode)
        self.state = ActorFSM(self.actor)
        self.input = Movement()
        
    def update(self,dt):#TODO account for jumping and for swinging and shooting and wall crawl
        GameObject.update(self, dt)
        if self.input.movement['down'] != 0:
            self.velocity.addY(-self.acceleration*dt)
        if self.input.movement['up'] != 0:
            self.velocity.addY(self.acceleration*dt)
        if self.input.movement['left'] != 0:
            self.velocity.addX(-self.acceleration*dt)
        if self.input.movement['right'] != 0:
            self.velocity.addX(self.acceleration*dt)
        if self.input.movement['jump'] != 0:
            self.velocity.addZ(self.jump*dt)
        if self.velocity != Vec3(0, 0, 0):
            if self.state.state != 'Walking':
                self.state.request('Walking')
        elif self.state.state == 'Walking':
                self.state.request('Standing')
        base.cam.setPos(self.move.getX(),-15+self.move.getY(),20+self.move.getZ())
        base.cam.lookAt(self.move.getX(),self.move.getY(),self.move.getZ())

class TheCloud(GameObject):
    def __init__(self):
        pass

    def update(self,dt):
        self.runlogic()

    def runlogic(self):
        pass

class NPC(GameObject):
    def __init__(self):
        GameObject.__init__()

    def update(self,dt):
        self.runlogic()

    def runlogic(self):
        pass
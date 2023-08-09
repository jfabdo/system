from panda3d.core import Vec4, Vec3, Vec2, Plane, Point3, BitMask32
from direct.actor.Actor import Actor
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage
from direct.task import Task
from panda3d.core import CollisionSphere, CollisionNode, CollisionRay, CollisionSegment, CollisionHandlerQueue
from panda3d.core import TextNode
from panda3d.core import AudioSound
from panda3d.core import PointLight
from State import ActorFSM
import math, random
from os.path import abspath
from sys import path

FRICTION = 150.0

class GameObject():
    def __init__(self,pos=Vec3(0, 0, 0),modelName="ball",modelAnims=None,maxHealth=10,maxSpeed=10,maxMana=None,maxStamina=None):
        if modelAnims is None:
            self.actor = Actor(path[0]+'/models/ball.bam', {
                    'walk': path[0]+'/models/bouncing ball.bam',
                    'jump': path[0]+'/models/jumping ball.bam'
                })
        else:
            self.actor = modelAnims
        self.actor.reparentTo(render)
        self.setSpeedAcc(maxHealth,maxSpeed)
        self.addCollider()
        self.actor = Actor(modelName, modelAnims)
        self.actor.reparentTo(render)
        self.actor.setPos(pos)

        # colliderNode = CollisionNode(colliderName)
        # colliderNode.addSolid(CollisionSphere(0, 0, 0, 0.3))
        # self.collider = self.actor.attachNewNode(colliderNode)
        # self.collider.setPythonTag("owner", self)
    
    def update(self,dt):
        speed = self.velocity.length()
        if speed > self.maxSpeed:
            self.velocity.normalize()
            self.velocity *= self.maxSpeed
            speed = self.maxSpeed

        if not self.walking:
            frictionVal = FRICTION*dt
            if frictionVal > speed:
                self.velocity.set(0, 0, 0)
            else:
                frictionVec = -self.velocity
                frictionVec.normalize()
                frictionVec *= frictionVal

                self.velocity += frictionVec

        self.actor.setPos(self.actor.getPos() + self.velocity*dt)

    def setSpeedAcc(self,maxHealth,maxSpeed):
        self.maxSpeed = maxSpeed
        self.velocity = Vec3(0, 0, 0)
        self.acceleration = 300.0

        self.maxHealth = maxHealth
        self.health = maxHealth

    def addCollider(self):
        pass

class Player(GameObject):
    def __init__(self):
        GameObject.__init__(self)
        self.state = ActorFSM(self.actor)
        
    def update(self,dt):
        GameObject.update(self, dt)
        
        Task.done

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
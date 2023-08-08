# from random import choice
from direct.fsm.FSM import FSM

welcomescreen = [
    "Welcome, fool",
    "Welcome to the dungeons"
]

class MenuFSM(FSM):
    def __init__(self):
        FSM.__init__(self, 'MenuState')
        self.defaultTransitions = {
            'Intro' : [ 'Exited', 'Playing' ],
            'Playing' : [ 'Escaped', 'Paused' ],
            'Escaped' : [ 'Exited', 'Intro', 'Playing' ],
            'Paused' : [ 'Escaped', 'Playing' ],
            'Exited' : [ ]
        }

    def enterIntro(self):
        # self.GUI.introscreen.show()
        pass

    def exitIntro(self):
        # self.GUI.introscreen.hide()
        pass

    def enterPlaying(self):
        # self.GUI.updateTask = taskMgr.add(self.update, "update")
        pass

class ActorFSM(FSM):
    def __init__(self,actr=None):
        FSM.__init__(self, 'ActorState')
        # self.defaultTransitions = {
        #     'Standing' :
        # }
        if actr == None:
            print("pass the actor")
            exit(1)
        self.actor = actr
        self.magicstate = MagicFSM(self)
        self.weaponstate = WeaponFSM(self)
    
    def enterStanding(self):
        self.actor.play('')

    def exitStanding(self):
        self.actor.stop('')

    def enterWalking(self):
        self.actor.loop('walk')
    
    def exitWalking(self):
        self.actor.setPlayRate(3)
        self.actor.pose('walk',17)
        self.actor.setPlayRate(1)

    def enterJump(self):
        self.actor.setPlayRate(3)
        self.actor.pose('walk',9)
        self.actor.setPlayRate(1)
        self.actor.play('jump')

    def exitJump(self):
        self.actor.stop('jump')
        self.actor.setPlayRate(-3)
        self.actor.play('walk', fromFrame=7, toFrame=1)
        self.actor.setPlayRate(1)

    def enterWeapon(self): #be sure to allow for both hand fighting
        self.weaponstate.request("Strike")
    
    def enterMagic(self):
        self.magicstate.request("Charging")

    def enterHit(self):
        pass

    def enterDead(self):
        pass

    def enterExit(self):
        Actor.cleanup()

class WeaponFSM(FSM):
    def __init__(self,hand=None):
        FSM.__init__(self, 'WeaponState')
        self.defaultTransitions = {
                'Draw' : [ 'Idle' ],
                'Idle' : [ 'Strike', 'Block', 'Away' ],
                'Strike' : [ 'Idle'],
                'Block' : [ 'Idle', 'Strike' ],
                'Away' : [ ]
        }
    
    def enterIdle(self):
        pass

    def enterStrike(self):
        pass
    
    def exitStrike(self):
        pass

    def enterBlock(self):
        pass

    def enterAway(self):
        self.gameobject.cleanup()

class MagicFSM(FSM):
    def __init__(self,magicpoint=None):
        FSM.__init__(self, 'MagicState')
        self.defaultTransitions = {
                'Idle' : [ 'Charging', 'Away' ],
                'Charging' : [ 'Firing' ],
                'Firing' : [ 'Hit' ],
                'Hit' : [ 'Idle' ],
                'Away' : [ ]
        }

    def enterIdle(self):
        pass

    def enterCharging(self):
        #hold off until the button is released
        self.game
        self.request("Firing")

    def enterFiring(self):
        self.request("Hit")

    def enterHit(self):
        self.request('Idle')

    def enterAway(self):
        pass #destroy object
from random import choice
import direct.fsm.FSM as FSM

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
            'Exited' : [ ],
        }
        self.GUI = GUI(self)
        self.GUI.run()

    def enterIntro(self):
        self.GUI.introscreen.show()

    def exitIntro(self):
        self.GUI.introscreen.hide()

    def enterPlaying(self):
        self.GUI.updateTask = taskMgr.add(self.update, "update")

class ActorFSM(FSM):
    def __init__(self,actr):
        FSM.__init__(self, 'ActorState')
        # self.defaultTransitions = {
        #     'Standing' :
        # }
        if actr == None:
            print("pass the actor")
            exit(1)

        self.magicstate = MagicFSM(self)
        self.weaponstate = WeaponFSM(self)
    
    def enterStanding(self):
        pass

    def enterWalking(self):
        pass

    def enterJump(self):
        self.request("Jump")

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
    def __init__(self):
        FSM.__init__(self, 'WeaponState')
        self.defaultTransitions = {
                'Draw' : [ 'Idle' ],
                'Idle' : [ 'Strike', 'Block', 'Away' ],
                'Strike' : [ 'Idle'],
                'Block' : [ 'Idle', 'Strike' ],
                'Away' : [ '' ]
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
    def __init__(self):
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
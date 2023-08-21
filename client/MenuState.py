from direct.fsm.FSM import FSM
from collections import deque

inqueue = deque()
outqueue = deque()

welcomescreen = [
    'Enter, fool',
    'Welcome to the dungeons'
]

# Controls the interplay of menu and game, such as 
# transparancy for game menus in game and putting up the right menu
# when in game
class MasterState():
    def __init__(self):
        self.menu = MenuFSM()
        self.game = GameFSM()

# Controls the menu state. Easier to continue to use these hooks 
# than to do control state another way
class MenuFSM(FSM):
    def __init__(self):
        FSM.__init__(self, 'MenuState')
        self.defaultTransitions = {
            'Open': [ 'Closed', 'Exit' ],
            'Closed': [ 'Open' ],
            'Exit': []
        }

# Contols the gameplay, when to run the game, etc
class GameFSM(FSM):
    def __init__(self):
        FSM.__init__(self, 'GameState')
        self.defaultTransitions = {
            'Root': [ 'SinglePlayer', 'Multiplayer', 'Exit' ],
            'SinglePlayer': [ 'Root', 'Exit' ],
            'Multiplayer': [ 'Root', 'Exit' ],
            'Exit': []
        }
    
    #start up server on network thread, have the server read the network stack
    # enter sets up panda, gets everything from server, starts processing queue on a new thread
    # start processing queue, stuff from server
    def enterSinglePlayer(self):
        pass
    
    # Look for server and start reading stack from network
    def enterMultiplayer(self):
        pass
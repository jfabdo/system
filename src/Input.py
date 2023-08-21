from direct.showbase import DirectObject

class Movement(DirectObject.DirectObject):
    def __init__(self):
        self.accept('Move',self._keymove)
        self.accept('Look',self._mouselook)
        self.accept('MobileMove',self._mobilemove)
        self.registerkeys()
        self.movement = {
            'down' : 0,
            'up' : 0,
            'left' : 0,
            'right' : 0,
            'jump' : 0
        }

    def registerkeys(self):
        movekeys = ['time-a','time-w','time-s','time-d','time-space']
        for i in movekeys:
            self.accept(f'{i}',self._keymove,[f'{i}'])
            self.accept(f'{i}-up',self._keymove,[f'{i}-up'])

    def _keymove(self,key,time):
        if key == 'time-s':
            self.movement['down'] = time
        elif key == 'time-w':
            self.movement['up'] = time
        elif key == 'time-a':
            self.movement['left'] = time
        elif key == 'time-d':
            self.movement['right'] = time
        elif key == 'time-space':
            self.movement['jump'] = time
        elif key == 'time-s-up':
            self.movement['down'] = 0
        elif key == 'time-w-up':
            self.movement['up'] = 0
        elif key == 'time-a-up':
            self.movement['left'] = 0
        elif key == 'time-d-up':
            self.movement['right'] = 0
        elif key == 'time-space-up':
            self.movement['jump'] = 0

    def _mouselook(self):
        pass #look at mouse

    def _mobilemove(self):
        pass #catch events from the main screen


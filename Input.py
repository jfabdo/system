import direct.directbase.DirectStart
from direct.showbase import DirectObject

class Movement(DirectObject.DirectObject):
    def __init__(self):
        self.accept("Move",self._keymove)
        self.accept("Look",self._mouselook)
        self.accept("MobileMove",self._mobilemove)
        self.registerkeys()

    def registerkeys(self):
        keys = ['a','w','s','d','space','shift']
        for i in keys:
            self.accept(f'{i}',self._keymove,[f'{i}'])
            self.accept(f'{i}-up',self._keymove,[f'{i}-up'])

    def _keymove(self,key):
        pass #add velocity in the direction of movement

    def _mouselook(self):
        pass #look at mouse

    def _mobilemove(self):
        pass #catch events from the main screen


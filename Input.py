import direct.directbase.DirectStart
from direct.showbase import DirectObject

class Test(DirectObject.DirectObject):
    def __init__(self):
        self.accept("Move",self._keymove)
        self.accept("Look",self._mouselook)
        self.accept("MobileMove",self._mobilemove)

    def _keymove(self):
        pass #add velocity in the direction of movement

    def _mouselook(self):
        pass #look at mouse

    def _mobilemove(self):
        pass #catch events from the main screen
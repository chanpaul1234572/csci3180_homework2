from Player import *
from Weapon import *
from Axe import *
class Chark(Player):
    def __init__(self, posx, posy, index, game):
        super(Chark, self).__init__(100, 4, posx, posy, index, game)
        self._myString = "C" + str(index)
        self._equipment = Axe(self)
    
    def teleport(self):
        super(Chark, self).teleport()
        self._equipment.enhance()
    
    def askForMove(self):
        print "You are a Chark (C{0}) using Axe. (Range: {1}, Damage: {2})".format(self._index,
			self._equipment.getRange(), self._equipment.getEffect())
        super(Chark, self).askForMove()

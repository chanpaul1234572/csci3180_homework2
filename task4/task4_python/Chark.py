from Player import *
from Axe import *
from Wand import *
class Chark(Player):
    def __init__(self, posx, posy, index, game, weaponOrHeal):
        super(Chark, self).__init__(100, 4, posx, posy, index, game)
        self._myString = "C" + str(index)
        if(weaponOrHeal == 1):
            self._equipment = Axe(self)
        else:
            self._equipment = Wand(self)
    
    def teleport(self):
        super(Chark, self).teleport()
        self._equipment.enhance()
    
    def askForMove(self):
        if (isinstance(self._equipment, Axe)):
            print "You are a Chark (C{0}) using Axe. (Range: {1}, Damage: {2})".format(self._index,
			self._equipment.getRange(), self._equipment.getEffect())
        elif (isinstance(self._equipment, Wand)):
            print "You are a Chark (C{0}) using Wand. (Range: {1}, Effect: {2})".format(self._index,
			self._equipment.getRange(), self._equipment.getEffect())
        super(Chark, self).askForMove()

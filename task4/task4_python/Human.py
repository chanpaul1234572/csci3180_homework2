from Player import *
from Rifle import *
from Wand import *
class Human(Player):
    def __init__(self, posx, posy, index, game, weaponOrHeal):
        super(Human, self).__init__(80, 2, posx, posy, index, game)
        self._myString = 'H' + str(index)
        if (weaponOrHeal == 1):
            self._equipment = Rifle(self)
        else:
            self._equipment = Wand(self)
    
    def teleport(self):
        super(Human, self).teleport()
        self._equipment.enhance()
    
    def distance(self, posx, posy):
        pass
    
    def askForMove(self):
        if (type(self._equipment) is Rifle):
            print "You are a human (H{0}) using Rifle. (Range: {1}, Ammo #: {2}, Damage per shot: {3})".format(self._index,
            self._equipment.getRange(), self._equipment.getAmmo(),
            self._equipment.getEffect())
        elif (type(self._equipment) is Wand):
            print "You are a human (H{0}) using Wand. (Range: {1}, effect: {2})".format(self._index, 
            self._equipment.getRange(), self._equipment.getEffect())
        super(Human, self).askForMove()
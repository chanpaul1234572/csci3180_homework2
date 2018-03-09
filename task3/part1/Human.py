from Player import Player
from Rifle import Rifle
class Human(Player):
    def __init__(self, posx, posy, index, game):
        super(Human, self).__init__(80, 2, posx, posy, index, game)
        self._myString = 'H' + str(index)
        self._equipment = Rifle(self)
    
    def teleport(self):
        super(Human, self).teleport()
        self._equipment.enchance()
    
    def distance(self, posx, posy):
        pass
    
    def askForMove(self):
        print "You are a human (h{0}) using Rifle. (Range {1}, Ammo #: {2}, Damage per shot: {3})".format(self._index,
        self._equipment.getRange(), self._equipment.getAmmo(),
        self._equipment.getEffect())
        super(Human, self).askForMove()
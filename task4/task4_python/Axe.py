from Weapon import *
from Player import *
class Axe (Weapon):
    __AXE_RANGE = 1
    __AXE_INIT_DAMAGE = 40
    def __init__(self, owner):
        super(Axe, self).__init__(Axe.__AXE_RANGE, Axe.__AXE_INIT_DAMAGE, owner)
    
    def enhance(self):
        self._effect += 10
    
    def action(self, posx, posy):
        print "You are using axe attacking " + str(posx) + " " + str(posy) + "."
        if self._owner._pos.distance(posx, posy) <= self._range:
            player = self._owner._game.getPlayer(posx, posy)
            if isinstance(player, type(self._owner)) == False and player != None  :
                player.decreaseHealth(self._effect)
            elif isinstance(player, type(self._owner)) and player != None:
                print "Cannot attack same race"
        else:
            print "Out of reach."
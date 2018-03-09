from Weapon import *
from Player import *
class Axe (Weapon):
    __AXE_RANGE = 1
    __AXE_INIT_DAMAGE = 40
    def __init__(self, owner):
        super(Axe, self).__init__(Axe.__AXE_RANGE, AXE.__AXE_INIT_DAMAGE, owner)
    
    def enhance(self):
        self.effect += 10
    
    def action(posx, posy):
        print "You are using axe attacking " + posx + " " + posy + "."
        if self.owner.pos.distance(posx, posy) <= self._range:
            player = owner.game.getPlayer(posx, posy)

            if player != None:
                player.decreaseHealth(self.effect)
        else:
            print "Out of reach."
from Weapon import *
#from Human import *
#from Chark import *
class Wand(Weapon):
    __WAND_RANGE = 5
    __WAND_INIT_DAMAGE = 5
    def __init__(self, owner):
        super(Wand, self).__init__(Wand.__WAND_RANGE, Wand.__WAND_INIT_DAMAGE, owner)
        self.maxhealth = owner._health
    
    def enhance(self):
        self._effect = self._effect + 5
    
    def action(self, posx, posy):
        print "You are using Wand healing " + str(posx) + " " + str(posy) + " " + "."
        if (self._owner._pos.distance(posx, posy) <= self._range):
            player = self._owner._game.getPlayer(posx, posy)
            if (player is None) == False:
                if isinstance(self._owner, type(player)):
                    player.increaseHealth(self.getEffect())
                    if player._health > self.maxhealth:
                        player._health = self.maxhealth
                else:
                    print "Cannot use to heal the different race"
        else:
            print "out of range"

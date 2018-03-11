from Weapon import *
from Human import *
#from Chark import *
class Rifle(Weapon):
    __RIFLE_RANGE = 4
    __RIFLE_INIT_DAMAGE = 10
    __AMMO_LIMIT = 6
    __AMMO_RECHARGE = 3
    def __init__(self, owner):
        super(Rifle, self).__init__(Rifle.__RIFLE_RANGE, Rifle.__RIFLE_INIT_DAMAGE, owner)
        self.__ammo = Rifle.__AMMO_LIMIT

    def action(self, posx, posy):
        print "You are using rifle attacking " + str(posx) + " " + str(posy) + '.'
        print "Type how many ammos you want to use."
        ammoToUse = int(raw_input())
        if (ammoToUse > self.__ammo):
            print "You don't have that ammos."
            return
        
        if self._owner._pos.distance(posx, posy) <= self._range :
            player = self._owner._game.getPlayer(posx, posy)
            if player != None:
                if isinstance(player, type(self._owner)) == False:
                    player.decreaseHealth(self._effect * ammoToUse)
                    self.__ammo = self.__ammo - ammoToUse
                elif isinstance(player, type(self._owner)):
                    print "Cannot attack same race"
            else:
                print "Out of reach."
    
    def enhance(self):
        self.__ammo = min(Rifle.__AMMO_LIMIT, self.__ammo + Rifle.__AMMO_RECHARGE)
    
    def getAmmo(self):
        return self.__ammo

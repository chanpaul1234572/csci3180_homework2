from Weapon import Weapon
def Rifle(Weapon):
    __RIFLE_RANGE = 4
    __RIFLE_INIT_DAMAGE = 10
    __AMMO_LIMIT = 6
    __AMMO_RECHARGE = 3
    def __init__(self, owner):
        super(Rifle, self).__init__(Rifle.__RIFLE_RANGE, Rifle.__RIFLE_INIT_DAMAGE, owner)
        self.__ammo = Rifle.__AMMO_LIMIT

    def enchance(self):
        self.__ammo = min(Rifle.__AMMO_RECHANGE, self.__ammo + Rifle.__AMMO_RECHANGE)

    def action(self, posx, posy):
        print "You are using rifle attacking " + posx + " " + posy + '.'
        print "Type how many ammos you want to use."
        ammoToUse = int(raw_input())
        if (ammoToUse > self.__ammo):
            print "You don't have that ammos."
            return
        
        if self.owner.pos.distance(posx, posy) <= self._range :
            player = owner.game.getPlayer(posx, posy)
            if player != None:
                player.decreaseHealth(self._effect * ammoToUse)
                self.__ammo -= ammoToUse
        else:
            print "Out of reach."
    
    def getAmmo(self):
        return self.__ammo

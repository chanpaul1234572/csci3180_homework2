import random
import abc
from Pos import Pos
from Weapon import Weapon
class Player(object):
    __metaclass__ = abc.ABCMeta
    def __init__(self, healthCap, mob, posx, posy, index, game):
        self.__MOBILITY = mob
        self._health = healthCap
        self._pos = Pos(posx, posy)
        self._index = index
        self._game = game
        self._myString = ""
        self._equipment = ""
    
    def getPos(self):
        return self._pos
    
    def teleport(self):
        randx = random.randint(0, self._game.D - 1)
        randy = random.randint(0, self._game.D - 1)
        while(self._game.positionOccupied(randx, randy)):
            randx = random.randint(0, self._game.D - 1)
            randy = random.randint(0, self._game.D - 1)
        self._pos.setPos(randx, randy)
    
    def increaseHealth(self, h):
        self._health = h + self._health
    
    def decreaseHealth(self, h):
        self._health = self._health - h
        if (self._health <= 0):
            self._myString = "C" + self._myString[0]
    
    def getName(self):
        return self._myString
    
    def askForMove(self):
        print "Your health is ", 
        print self._health ,
        print ". Your position is ({0},{1}). Your mobility is {2}.".format(self._pos.getX(), self._pos.getY(), self.__MOBILITY)
        print "You now have following options: "
        print "1. Move"
        print "2. Attack"
        print "3. End the turn"

        a = int(raw_input())

        if (a == 1):
            print "Specify your target position (Input 'x y')."
            posx = int(raw_input())
            posy = int(raw_input())
            if(self._pos.distance(posx, posy) > self.__MOBILITY):
                print "Beyond your reach. Staying still."
            elif self._game.positionOccupied(posx, posy):
                print "Position occupied. Cannot move there."
            else:
                self._pos.setPos(posx, posy)
                self._game.printBoard()
                print "You can now "
                print "1.attack"
                print "2.End the turn"
                if (int(raw_input()) == 1):
                    print "Input position to attack. (Input 'x y')"
                    attx = int(raw_input())
                    atty = int(raw_input())
                    self._equipment.action(attx, atty)
        elif (a == 2):
            print "Input position to attack."
            attx = int(raw_input())
            atty = int(raw_input())
            self._equipment.action(attx, atty)
        elif (a == 3):
            return




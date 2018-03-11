import random
from Pos import *
class Obstacle(object):
    def __init__(self, posx, posy, index, game):
        self.__pos = Pos(posx, posy)
        self.__index = index
        self.__game = game
    
    def getPos(self):
        return self.__pos
    
    def teleport(self):
        randx = random.randint(0, self.__game.D - 1)
        randy = self.__game.D - randx - 1
        while(self.__game.positionOccupied(randx, randy)):
            randx = random.randint(0, self.__game.D - 1)
            randy = self.__game.D - randx - 1
            print "x:", randx, "y:", randy, self.__game.positionOccupied(randx, randy)
        self.__pos.setPos(randx, randy)
        
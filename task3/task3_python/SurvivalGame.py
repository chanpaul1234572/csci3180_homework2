from Pos import* 
from Human import *
from Chark import *
from Axe import *
from Obstacle import *
from sys import *
class SurvivalGame(object):
    #__n = 0
    #D = 10
    #__O = 2
    #__teleportObjects = object()

    def __init__(self):
        self.__n = 0      #number of player
        self.D = 10       #dimension of board
        self.__O = 2      #number of obstacle
        self.__teleportObjects = object()


    def printBoard(self):
        printObject = [["  " for _ in range(self.D)] for _ in range(self.D)]
        for i in range(0 , self.__n):
            pos = self.__teleportObjects[i].getPos()
            printObject[pos.getX()][pos.getY()] = self.__teleportObjects[i].getName()
        for i in range(self.__n, self.__O + self.__n):
            pos = self.__teleportObjects[i].getPos()
            printObject[pos.getX()][pos.getY()] = "O" + str(i - self.__n)

        print " ",
        for i in range(0, self.D):
            print "| {0} ".format(i),
        print "|"
        for i in range (0, int(self.D * 5.5)):
            stdout.write('-')
            stdout.write('')
        print ""

        for row in range(0, self.D):
            print row,
            for col in range(0, self.D):
                print "| {0}".format(printObject[row][col]),
            print "|"
            for i in range(0, int(self.D * 5.5)):
                stdout.write('-')
                stdout.write('')
            print ""

    def positionOccupied(self, randx, randy):
        for o in self.__teleportObjects:
            if (isinstance(o, Player)):
                pos = o.getPos()
                if (pos.getX() == randx and pos.getY() == randy):
                    return True
            elif(isinstance(o, Obstacle)):
                pos = o.getPos()
                if (pos.getX() == randx and pos.getY() == randy):
                    return True
        return False

    def getPlayer(self, randx, randy):
        for o in self.__teleportObjects:
            if (isinstance(o, Player)):
                pos = o.getPos()
                if pos.getX() == randx and pos.getY() == randy:
                    return o
        return None

    def init(self): 
        print "Welcome to Kafustrok. Light blesses you. \nInput number of players: (a even number)"
        self.__n = int(raw_input())
        self.__teleportObjects = [object() for _ in range(0, self.__n + self.__O)]
        #create N/2 Humans
        for i in range(0, self.__n / 2):
            self.__teleportObjects[i] = Human(0, 0, i, self)
            self.__teleportObjects[i + self.__n / 2] = Chark(0, 0, i, self)
        #create O obstacles. You cannot stand there
        for i in range(0, self.__O):
            self.__teleportObjects[i + self.__n] = Obstacle(0, 0, i, self)
        #position would be reinitialized later. 0,0 is dummy

    def __gameStart(self):
        turn = 0
        numOfAlivePlayers = self.__n
        while(numOfAlivePlayers > 1):
            if turn == 0:
                for obj in self.__teleportObjects:
                    obj.teleport()
                print "Everything gets teleported"
            t = self.__teleportObjects[turn]
            if t._health > 0:
                self.printBoard()
                t.askForMove()
                print "\n"
            turn = (turn + 1) % self.__n
            numOfAlivePlayers = 0
            for i in range(0, self.__n):
                if self.__teleportObjects[i]._health > 0:
                    numOfAlivePlayers += 1
        print "Game over."
        self.printBoard()
    
    def open(self):
        self.init()
        self.__gameStart()

game = SurvivalGame()
game.open()






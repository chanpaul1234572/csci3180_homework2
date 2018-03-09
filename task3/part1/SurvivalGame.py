from Pos import* 
from Human import *
class SurvivalGame(object):
    #__n = 0
    #D = 10
    #__O = 2
    #__teleportObjects = object()

    def __init__(self):
        self.__n = 0
        self.D = 10
        self.__O = 2
        self.__teleportObjects = object()


    def printBoard(self):
        printObject = [[" " for _ in range(D)] for _ in range(D)]
        for i in range(0 , self.D):
            pos = self.__teleportObjects[i].getPos()
            printObject[pos.getX()][pos.getY()] = self.__teleportObjects[i].getName()
        for i in range(self.__n, self.__O + n):
            pos = self.__teleportObjects[i].getPos()
            printObject[pos.getX()][pos.getY()] = "O" + str(i - n)

        print " ",
        for i in range(0, self.D):
            print "| {0} ".format(i),
        print "|"

        for i in range(0, self.D * 5.5):
            print "-",
        print ""

        for row in range(0, self.D):
            print row,
            for col in range(0, self.D):
                print "| {0} ".format(printObject[row][col]),
            print "|"
            for i in range(0, D * 5.5):
                print "-",
            print ""

    def positionOccupied(self, randx, randy):
        for o in self.__teleportObjects:
            if (type(o) is Player):
                pos = o.getPos()
                if (pos.getX() == randx and pos.getY() == randy):
                    return True
                else:
                    pos = o.getPos()
                    if (pos.getX() == randx and pos.getY() == randy):
                        return True
        return False

    def getPlayer(self, randx, randy):
        for o in self.__teleportObjects:
            if (type(o) is Player):
                pos = o.getPos()
                if pos.getX() == randx and pos.getY() == randy:
                    return o
        return None

    def init(self): 
        print "Welcome to Kafustrok. Light blesses you. \nInput number of players: (a even number)"
        n = int(raw_input())
        self.__teleportObjects = [object() for _ in range(0, n + self.__O)]
        #create N/2 Humans
        for i in range(0, n / 2):
            self.__teleportObjects[i] = Human(0, 0, i, self)
            self.__teleportObjects[i + n / 2] = Chark(0, 0, i, self)
        #create O obstacles. You cannot stand there
        for i in range(0, O):
            self.__teleportObjects[i + n] = Obstacle(0, 0, i, self)
        #position would be reinitialized later. 0,0 is dummy

    def __gameStart(self):
        turn = 0
        numOfAlivePlayers = n
        while(numOfAlivePlayers > 1):
            if turn == 0:
                for obj in self.__teleportObjects:
                    if type(obj) is Human:
                        obj.teleport()
                    elif type(obj) is Chark:
                        obj.teleport()
                    elif type(obj) is Obstacle:
                        obj.teleport()
                print "Everything gets teleported"
            printBoard()
            t = teleportObjects[turn]
            if t.health > 0:
                t.askForMove()
                print "\n"
            turn = (turn + 1) % n
            numOfAlivePlayers = 0

            for i in range(0, n):
                if teleportObjects[i].health > 0:
                    numOfAlivePlayers += 1


        print "Game over."
        printBoard()

game = SurvivalGame()
game.init()
game.gameStart()






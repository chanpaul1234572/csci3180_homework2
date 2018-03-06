#from Player import *
import Player
class Human(Player.Player):
    def __init__(self, symbol, gameboard):
        super(Human, self).__init__(symbol, gameboard)

    def nextMove(self):
        while True:
            str = "Player " + self.PlayerSymbol + "'s turn!"
            print str
            str = raw_input("Type the row and col to put the disc: ")
            if str[0].isdigit() == True and str[2].isdigit() == True and str[1] == ' ':
                row = int(str[0])
                col = int(str[2])
                if row > 9 or row < 1 or col > 9 or col < 1:
                    print "invaild input!"
                elif self.gameBoard[row - 1][col - 1] != 0:
                    print "invaild input!"
                else:
                    return (row - 1, col - 1)
            else:
                print "invaild input!"
            

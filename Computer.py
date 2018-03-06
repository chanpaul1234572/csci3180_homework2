from Player import Player
import random
class Computer(Player):
    def __init__(self, symbol, gameboard):
        super(Computer, self).__init__(symbol, gameboard)

    def nextMove(self):
        str = "Player " + self.PlayerSymbol + "'s turn!"
        print str
        while True:
            row = random.randint(1, 9)
            col = random.randint(1, 9)
            if self.gameBoard[row - 1][col - 1] == 0:
                print row, col 
                break
        print "Type the row and col to put the disc:", row, col
        return (row - 1, col - 1)



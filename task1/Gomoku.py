#/*
#* CSCI3180 Principles of Programming Languages
# *
# * --- Declaration ---
# *
# * I declare that the assignment here submitted is original except for source
# * material explicitly acknowledged. I also acknowledge that I am aware of
# * University policy and regulations on honesty in academic work, and of the
# * disciplinary guidelines and procedures applicable to breaches of such policy
# * and regulations, as contained in the website
# * http://www.cuhk.edu.hk/policy/academichonesty/
#*
# * Assignment 2
# * Name : Chan Paul
# * Student ID : 1155078895
#* Email Addr : pchan6@cse.cuhk.edu.hk
#*/
import sys
import Player
import Human
import Computer
class Gomoku(object):
#emptyspace = 0
#playerO = 1
#playerX = 2
    def __init__(self):
        self.player1 = 1
        self.player2 = 1
        self.turn = 1
        w, h =9, 9
        self.gameBoard = [[0 for _ in range(w)] for _ in range(h)] 
        '''for i in range(h):
            print i + 1,
            for j in range(w):
                print self.gameBoard[i][j],
            print
        '''
    def createPlayer(self, symbol, playerNum):
        if self.turn == 1:
            if playerNum == 1:
                self.player1 = Human.Human(symbol, self.gameBoard)
            elif playerNum == 2:
                self.player1 = Computer.Computer(symbol, self.gameBoard)
            self.turn = 2
        elif self.turn == 2:
            if playerNum == 1:
                self.player2 = Human.Human(symbol, self.gameBoard)
            elif playerNum == 2:
                self.player2 = Computer.Computer(symbol, self.gameBoard)
            self.turn = 1
    def startGame(self):
        print_choice = lambda y : "Human" if y == 1 else "Computer"
        print("Please choose player 1 (O) :")
        print("1. Human")
        print("2. computer Player")
        choice = int(raw_input("Your choice is: "))
        self.createPlayer('O', choice)
        str1 = "Player O is " + print_choice(choice) + '.'
        print str1
        if choice != 3:
            print("Please choose player 2 (X) :")
            print("1. Human")
            print("2. computer Player")
            choice = int(raw_input("Your choice is: "))
            self.createPlayer('X', choice)
            str2 = "Player X is " + print_choice(choice) + '.'
            print str2
        self.printGameBoard()
        #finished the init
        while True:
            if self.checkWin() == 0 and self.checkTie() == 0:
                if self.turn == 1:
                    x, y = self.player1.nextMove()
                    self.gameBoard[x][y] = 1
                    self.turn = 2
                elif self.turn == 2:
                    x, y = self.player2.nextMove()
                    self.gameBoard[x][y] = 2
                    self.turn = 1
                self.printGameBoard()
            elif self.checkWin() == 1:
                print "Game ends. Player O wins"
                break
            elif self.checkWin() == 2:
                print "Game ends. Player X wins"
                break
            elif self.checkTie() == 1:
                print "Game ends in a tie."
                break
    def printGameBoard(self):
        #self.gameBoard[2][3] = 2
        print(' | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |')
        print('.....................................')
        for i in range(0, 9):
            numindex = str(i + 1)
            print numindex + '|',
            for j in range(0, 9):
                if self.gameBoard[i][j] == 0:
                    print ' ',
                elif self.gameBoard[i][j] == 1:
                    print 'O',
                elif self.gameBoard[i][j] == 2:
                    print 'X',
                print '|', 
            print
            print('.....................................')
    def checkWin(self):
        #check for row
        win = 0
        for i in range(0, 9):
            for j in range(0, 5):
                if self.gameBoard[i][j] == 1 and self.gameBoard[i][j + 1] == 1 and self.gameBoard[i][j + 2] == 1 and self.gameBoard[i][j + 3] == 1 and self.gameBoard[i][j + 4] == 1:
                    win = 1
                    break
                elif self.gameBoard[i][j] == 2 and self.gameBoard[i][j + 1] == 2 and self.gameBoard[i][j + 2] == 2 and self.gameBoard[i][j + 3] == 2 and self.gameBoard[i][j + 4] == 2:
                    win = 2
                    break
        #check for column
        for i in range(0, 5):
            for j in range(0, 9):
                if self.gameBoard[i][j] == 1 and self.gameBoard[i + 1][j] == 1 and self.gameBoard[i + 2][j] == 1 and self.gameBoard[i + 3][j] == 1 and self.gameBoard[i + 4][j] == 1:
                    win = 1
                    break
                elif self.gameBoard[i][j] == 2 and self.gameBoard[i + 1][j] == 2 and self.gameBoard[i + 2][j] == 2 and self.gameBoard[i + 3][j] == 2 and self.gameBoard[i + 4][j] == 2:
                    win = 2
                    break
        #check for left diagonal
        for i in range(0, 5):
            for j in range(0, 5):
                if self.gameBoard[i][j] == 1 and self.gameBoard[i + 1][j + 1] == 1 and self.gameBoard[i + 2][j + 2] == 1 and self.gameBoard[i + 3][j + 3] == 1 and self.gameBoard[i + 4][j + 4] == 1:
                    win = 1
                    break
                elif self.gameBoard[i][j] == 2 and self.gameBoard[i + 1][j + 1] == 2 and self.gameBoard[i + 2][j + 2] == 2 and self.gameBoard[i + 3][j + 3] == 2 and self.gameBoard[i + 4][j + 4] == 2:
                    win = 2
                    break
        #check for right diagonal
        for i in range(0, 8):
            for j in range(0, 5):
                if i - 4 < 0:
                    break
                else:
                    if self.gameBoard[i][j] == 1 and self.gameBoard[i - 1][j + 1] == 1 and self.gameBoard[i - 2][j + 2] == 1 and self.gameBoard[i - 3][j + 3] == 1 and self.gameBoard[i - 4][j + 4] == 1:
                        win = 1
                        break
                    elif self.gameBoard[i][j] == 2 and self.gameBoard[i - 1][j + 1] == 2 and self.gameBoard[i - 2][j + 2] == 2 and self.gameBoard[i - 3][j + 3] == 2 and self.gameBoard[i - 4][j + 4] == 2:
                        win = 2
                        break
        return win
    def checkTie(self):
        full = 1
        for i in range(0 ,9):
            for j in range(0 ,9):
                if self.gameBoard[i][j] == 0:
                    return 0
        if self.checkWin() == 0:
            return 1
        else:
            return 0
test = Gomoku()
test.startGame()

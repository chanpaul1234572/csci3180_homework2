import sys
import abc
class Player(object):
    __metaclass__ = abc.ABCMeta
    def __init__(self, symbol, gameboard):
        self.PlayerSymbol = symbol
        self.gameBoard = gameboard
    
    @abc.abstractmethod
    def nextMove(self):
        #return a tuple
        pass


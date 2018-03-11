import abc
import random
from Pos import Pos
class Weapon(object):
    __metaclass__ = abc.ABCMeta
    def __init__(self, range, damage, owner):
        self._range = range
        self._effect = damage
        self._owner = owner
    
    @abc.abstractmethod
    def action(posx, posy):
        pass
    @abc.abstractmethod
    def enhance():
        pass
    
    def getEffect(self):
        return self._effect
    
    def getRange(self):
        return self._range



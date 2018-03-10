class Pos(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def distance(self, another1, another2=None):
        if  another2 == None:
            return abs(self.__x - another1.x) + abs(self.__y - another1.y)
        else:
            return abs(self.__x - another1) + abs(self.__y - another2)
    
    def setPos(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
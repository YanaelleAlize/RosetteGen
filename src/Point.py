import numpy as np
from math import cos, sin, acos, sqrt


class Point :

    def __init__(self, x0 = 0, y0 = 0):
        self._x = x0
        self._y = y0

    def getX(self):
        return self._x

    def getY(self):
        return self._y
    
    def getNorm(self):
        return sqrt(self._x * self._x + self._y * self._y)
    
    def getOriginVector(self, mu = 1):
        return Point(mu * self._x / self.getNorm(), mu * self._y / self.getNorm())
    
    def getOriginAngle(self):
        return acos( self._x / self.getNorm())
    
    def setX(self, x):
        self._x = x

    def setY(self, y):
        self._y = y
        
    def setPointFromOriginAngle(self, alpha, r = 1):
        self._x = r * cos(alpha)
        self._y = r * sin(alpha)

    def __repr__(self):
        return "P({}, {})".format(self._x, self._y)

if __name__ == "__main__" :
    print("Point Unit tests : ")
    print("\tAngle (1, sqrt(3)) {}".format(Point(1, sqrt(3)).getOriginAngle() * 180 / np.pi))
    # Il faut penser à faire des comparaisons avec les erreurs potentielles de calculs
    # genre abs(x - y) / min(abs(x), abs(y)) < 1e-15 --> pour x == y
    

"""    
    def __init__(self, P):
        # copy ctor
        self._x = P._x
        self._y = P._y
"""
import numpy as np
from math import acos, sqrt

class Point :

    def __init__(self, x0 = 0, y0 = 0):
        self._x = x0
        self._y = y0

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getOriginAngle(self):
        return acos( self._x / sqrt(self._x * self._x + self._y * self._y))

    def __repr__(self):
        return "P({}, {})".format(self._x, self._y)

if __name__ == "__main__" :
    print("Point Unit tests : ")
    print("\tAngle (1, sqrt(3)) {}".format(Point(1, sqrt(3)).getOriginAngle() * 180 / np.pi))
    # Il faut penser à faire des comparaisons avec les erreurs potentielles de calculs
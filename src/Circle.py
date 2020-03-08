import numpy as np
from src.Point import Point
from src.PlotOptions import PlotOptions
from src.Figure import Figure

class Circle(Figure) :

    def __init__(self, Optn = PlotOptions(), Center = Point(), r = 1):
        self.super()
        self._Center = Center
        self._Optn = Optn
        self._r = r

    def __init__(self, Optn=PlotOptions(), x_0 = 0, y_0 = 0, r = 1):
        self.super()
        self._Center = Point(x_0, y_0)
        self._Optn = Optn
        self._r = r

    def getCenter(self):
        return self._Center

    def drawCircle(self):
        return self.drawSemiCircle()

    def drawSemiCircle(self, startAngle = 0, drawAngle = 2 * np.pi, parcoursSensTrigonometrique = True):
        x_0, y_0 = np.array([self._x0] * self._Optn.getN()), np.array([self._y0] * self._Optn.getN())
        if parcoursSensTrigonometrique :
            theta = np.linspace(startAngle, startAngle + drawAngle, self._Optn.getN())
        else :
            theta = np.linspace(startAngle - drawAngle, startAngle, self._Optn.getN())
        x1 = np.add(x_0, self._r * np.cos(theta))
        x2 = np.add(y_0, self._r * np.sin(theta))
        return x1, x2

    def drawSemiCircleFromOriginVector(self, drawAngle=2 * np.pi, parcoursSensTrigonometrique=True):
        alpha = self._Center.getOriginAngle()
        return self.drawSemiCircle(alpha - np.pi, drawAngle, parcoursSensTrigonometrique)

    def __repr__(self):
        return "Circle defined by (X - {})² + (Y - {})² = {}²".format(self._Center.getX(), self._Center.getY(), self._r)

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    print("Circle Unit tests : ")
    print("")
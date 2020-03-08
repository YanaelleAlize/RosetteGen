import numpy as np
from Point import Point
from PlotOptions import PlotOptions
from Figure import Figure


class Circle(Figure) :

    def __init__(self, Optn = PlotOptions(), Center = Point(), r = 1):
        super()
        self._Center = Center
        self._Optn = Optn
        self._r = r

    def getCenter(self):
        return self._Center

    def drawCircle(self):
        return self.drawSemiCircle()

    def drawSemiCircle(self, startAngle = 0, drawAngle = 2 * np.pi, parcoursSensTrigonometrique = True):
        x_0, y_0 = np.array([self._Center.getX()] * self._Optn.getN()), np.array([self._Center.getY()] * self._Optn.getN())
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
    from math import sqrt
    opt = PlotOptions()
    C1 = Circle(opt, Point(2, 2 * sqrt(3)), 1)
    print("Circle Unit tests : ")
    print(C1)
    
    print("\tTest Draw Circle : ")
    fig, a1 = plt.subplots(1)
    a1.set_aspect(1)
    xy_plot = C1.drawCircle()
    a1.plot(xy_plot[0], xy_plot[1])
    plt.show()
    
    print("\tTest Draw SemiCircle : ")
    fig, a2 = plt.subplots(1)
    a2.set_aspect(1)
    xy_plot = C1.drawSemiCircle(0, np.pi / 2)
    a2.plot(xy_plot[0], xy_plot[1])
    plt.show()
    
    print("\tTest Draw SemiCircle Antitrigo : ")
    fig, a3 = plt.subplots(1)
    a3.set_aspect(1)
    xy_plot = C1.drawSemiCircle(0, np.pi / 2, False)
    a3.plot(xy_plot[0], xy_plot[1])
    plt.show()
    
    print("\tTest Draw SemiCircleFromOriginVector : ")
    fig, a4 = plt.subplots(1)
    a4.set_aspect(1)
    xy_plot = C1.drawSemiCircleFromOriginVector(np.pi / 3)
    a4.plot(xy_plot[0], xy_plot[1])
    plt.show()
    
    print("\tTest Draw SemiCircleFromOriginVector Antitrigo : ")
    fig, a5 = plt.subplots(1)
    a5.set_aspect(1)
    xy_plot = C1.drawSemiCircleFromOriginVector(np.pi / 3, False)
    a5.plot(xy_plot[0], xy_plot[1])
    plt.show()
    
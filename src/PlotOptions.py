class PlotOptions :

    def __init__(self, N = 10000, DPI= 300, r = 1):
        """
        Class of plot parameters
        :param N: number of points on a circle
        :param DPI: to save the image
        :param r: Radius of the circles
        """
        self._N = N
        self._DPI = DPI
        self._r = r

    def getN(self):
        return self._N

    def getDPI(self):
        return self._DPI

    def getRadius(self):
        return self._r

    def setN(self, N):
        self._N = N

    def setDPI(self, DPI):
        self._DPI = DPI

    def setRadius(self, r):
        self._r = r

    def __str__(self):
        return "Current plot parameters :\n\t N : " + self._N.__str__() + "\t(Number of points on a circle)\n\t DPI : " + self._DPI.__str__() + "\t(to save the image)\n\t r : " + self._r.__str__() + "\t(Radius of the circles)"

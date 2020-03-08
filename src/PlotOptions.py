import json


class PlotOptions :

    def __init__(self, N = 10000, DPI= 300, r = 1):
        """
        Class of plot parameters
        :param N: number of points on a circle
        :param DPI: Digits per inches to save the image
        :param r: Default radius of the circles
        """
        self._N = N
        self._DPI = DPI
        self._r = r

    def getN(self):
        return self._N

    def getDPI(self):
        return self._DPI

    def getDefaultRadius(self):
        return self._r

    def setN(self, N):
        self._N = N

    def setDPI(self, DPI):
        self._DPI = DPI

    def setDefaultRadius(self, r):
        self._r = r
        
    def json_load(self, filepath):
        with open(filepath, "r") as f :
            json_string = f.read()
            f.close()
        dico = json.loads(json_string)
        self._N = int(dico["_N"])
        self._DPI = int(dico["_DPI"])
        self._r = float(dico["_r"])

    def json_save(self, filepath):
        with open(filepath, "w") as f :
            json_string = json.dumps({"_N" : self._N, "_DPI" : self._DPI, "_r" : self._r})
            f.write(json_string)
            f.flush()
            f.close()

    def __str__(self):
        return "Current plot parameters :\n\t N : " + self._N.__str__() + "\t(Number of points on a circle)\n\t DPI : " + self._DPI.__str__() + "\t(to save the image)\n\t r : " + self._r.__str__() + "\t(Radius of the circles)"

class Hora:
    __hora = 0
    __min = 0
    __seg = 0
    def __init__ (self, hs=0, m=0, seg=0):
        self.__hora = hs
        self.__min = m
        self.__seg = seg
    def MostrarHora (self):
        print("Hora {}:{}:{}".format(self.__hora, self.__min, self.__seg))
    def getHora (self):
        return self.__hora
    def getMin (self):
        return self.__min
    def getSeg (self):
        return self.__seg
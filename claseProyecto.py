class Proyecto:
    __idProyecto = ''
    __titulo = ''
    __palabrasClave = ''
    __puntaje = 0
    def __init__ (self, idPro = '', tit = '', palabras = ''):
        self.__idProyecto = idPro
        self.__titulo = tit
        self.__palabrasClave = palabras
        self.__puntaje = 0
    def mostrarProyecto (self):
        print("Id proyecto: {} \nTitulo: {} \nPalabras claves: {}\nPuntaje: {}".format(self.__idProyecto, self.__titulo, self.__palabrasClave, self.__puntaje))
    def getIdProyecto (self):
        return self.__idProyecto
    def getTitulo (self):
        return self.__titulo
    def getPalabrasClave (self):
        return self.__palabrasClave
    def getPuntaje (self):
        return self.__puntaje

    def acumularPuntos (self, puntos):
        self.__puntaje += puntos

    def restarPuntos (self, puntos):
        self.__puntaje -= puntos

    def __gt__ (self, otroProyecto):
        if ((type(self)) == (type(otroProyecto))):
            return (self.__puntaje > (otroProyecto.getPuntaje()))
class Camion:
    __id =None
    __nombre = ''
    __patente = ''
    __marca = ''
    __tara = 0
    def __init__(self, id = 0, nombre = '', patente = '', marca = '', tara = 0):
        self.__id = id
        self.__nombre = nombre
        self.__patente = patente
        self.__marca = marca
        self.__tara = tara
    def getPeso (self):
        return self.__tara
    def mostrarCamion (self):
        print("Id Camion: {} - Conductor: {} - Patente: {} - Marca: {} - Tara: {}".format(self.__id, self.__nombre, self.__patente, self.__marca, self.__tara))
    def getNro (self):
       return self.__id
    def getPatente (self):
        return self.__patente
    def getNombre(self):
        return self.__nombre     
import sys
from claseManejadorCamion import ManejadorCamion
from claseCosecha import Cosecha
class MenuCamion:
    __switcher=None
    __camiones = []
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
            '2':self.opcion2,
            '3':self.salir
        }
        self.__camiones = ManejadorCamion()
        self.__camiones.testListaCamion()

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op, cos):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(cos)
    
    def salir(self):
        print('Salida del Programa')

    def opcion1(self, cos):
        print("Ejecutamos la Opcion 1\n")
        nroCamion = int (input("Ingrese un identificador de camion: "))
        pesoTotalC = cos.buscarPeso(nroCamion)
        if (pesoTotalC != -1):                                  #peso obtenido es valido
            print("La cantidad de kilos descargados es: %.2f" % (self.__camiones.buscarCamion(nroCamion, pesoTotalC))) 
        else:
            print("Identificador de camion y peso no valido\n")

    def opcion2(self, cos):
        print("Ejecutamos la Opcion 2\n")
        nrodia = int(input("Ingrese un numero de dia: "))
        cos.mostrarDia(nrodia)
import sys
from claseManejadorCamion import ManejadorCamion
from claseCosecha import Cosecha
class MenuCamion:
    __switcher=None
    __camiones = []
    __cosechas = []
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
            '2':self.opcion2,
            '3':self.salir
        }
        self.__camiones = ManejadorCamion()
        self.__camiones.testListaCamion()
        self.__cosechas = Cosecha ()
        self.__cosechas.testLista()

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()
    
    def salir(self):
        print('Salir')

    def opcion1(self):
        print("Ejecutamos la Opcion 1\n")
        nroCamion = int (input("Ingrese un identificador de camion: "))
        pesoTotalC = self.__cosechas.buscarPeso(nroCamion)
        if (pesoTotalC != -1):                                  #peso obtenido es valido
            print("La cantidad de kilos descargados es: ", self.__camiones.buscarCamion(nroCamion, pesoTotalC)) 
        

    def opcion2(self):
        print("Ejecutamos la Opcion 2\n")
        nrodia = int(input("Ingrese un numero de dia: "))
        self.__cosechas.mostrarDia(nrodia)
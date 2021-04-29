import sys
from claseManejadorViajero import ManejadorViajero
class Menu:
    __switcher=None
    __listav = []
    def __init__(self):
        self.__switcher = { 'a':self.opcion1,
            'b':self.opcion2,
            'c':self.opcion3,
            'd':self.salir
        }
        self.__listav = ManejadorViajero()
        self.__listav.testListaViajeros()

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op, numerov):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(numerov)
    
    def salir(self):
        print('Salida del Programa')

    def opcion1(self, numerov):
        print("Ejecutamos la Opcion 1\n")
        self.__listav.consultarMillas (numerov)

    def opcion2(self, numerov):
        m = int(input("Ejecutamos Opcion 2\nIngrese cantidad de millas a acumular: "))
        self.__listav.acumular(numerov, m)
    
    def opcion3 (self, numerov):
        m = int(input("Ejecutamos Opcion 3\nIngrese cantidad de millas a canjear: "))
        self.__listav.canjear(numerov, m)

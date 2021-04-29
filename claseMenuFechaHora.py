import sys
from claseFechaHora import FechaHora
class MenuFechaHora:
    __switcher = None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.salir
        }
    
    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op, unaFecha, otraFecha):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(unaFecha, otraFecha)
    
    def salir(self):
        print('Salida del Programa')

    def opcion1(self, unaFecha, otraFecha):
        print("Ejecutamos la Opcion 1\n")
        print("La suma de las Fechas: ")
        suma = unaFecha + otraFecha
        suma.Mostrar()
        suma.validarBisiesto()
        suma.validar()

    def opcion2(self, unaFecha, otraFecha):
        print("Ejecutamos la Opcion 2\n")
        print("La resta de las Fechas es: ")
        band = unaFecha > otraFecha
        if (band == True):
            resta = unaFecha - otraFecha
        else:
            resta = otraFecha - unaFecha
        print("La resta de las dos fechas equivalentes en segundos es: {}\n".format(resta))
    
    def opcion3 (self, unaFecha, otraFecha):
        print("Ejecutamos la Opcion 3\n")
        #print("La fecha Mayor es: ")
        #unaFecha > otraFecha
        bandera = unaFecha > otraFecha
        print(bandera)
        if (bandera == True):
            print("La fecha Mayor es: ")
            unaFecha.Mostrar()
        else:
            print("La fecha Mayor es: ")
            otraFecha.Mostrar()
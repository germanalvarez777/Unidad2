import sys
from claseManejadorAlumno import ManejadorAlumno
class MenuAlumno:
    __switcher=None
    __listaAlumnos = []
    def __init__(self):
        self.__switcher = { 'a':self.opcion1,
            'b':self.opcion2,
            'c':self.salir
        }
        self.__listaAlumnos = ManejadorAlumno()
        self.__listaAlumnos.testListaAlumno()

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()
    
    def salir(self):
        print('Salida del Programa')

    def opcion1(self):
        print("Ejecutamos la Opcion 1\n")
        anioDiv = (input("Ingrese un año y division: "))
        self.__listaAlumnos.porcentaje(anioDiv)

    def opcion2(self):
        print("Ejecutamos la Opcion 2\n")
        nuevo = int(input("Ingrese la nueva cantidad maxima de inasistencias: "))
        self.__listaAlumnos.modificarInas(nuevo)
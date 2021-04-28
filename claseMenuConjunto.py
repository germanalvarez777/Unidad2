from claseConjunto import Conjunto
class MenuConjunto:
    __switcher = None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.salir
        }
        #self.__fechahora = FechaHora()          #agregamos algunos valores
    
    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op, unConj, otroConj):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(unConj, otroConj)
    
    def salir(self):
        print('Salida del Programa')

    def opcion1(self, unConj, otroConj):
        print("Ejecutamos la Opcion 1\n")
        suma = unConj + otroConj
        print("La union(+) de dos conjuntos es: {}".format(suma))

    def opcion2(self, unConj, otroConj):
        print("Ejecutamos la Opcion 2\n")
        resta = unConj - otroConj
        print("La diferencia de dos conjuntos es: {}".format(resta))
    
    def opcion3 (self, unConj, otroConj):
        print("Ejecutamos la Opcion 3\n")
        print("Los dos conjuntos son iguales?: ")
        print(unConj == otroConj)
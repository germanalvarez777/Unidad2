import csv
from claseIntegrantesProyecto import IntegrantesProyecto
class ManejadorIntegProyecto:
    __listaInteg = []
    def __init__ (self):
        self.__listaInteg = []
    def agregarInteg (self, unInteg):
        self.__listaInteg.append(unInteg)
    def testListaInteg (self):
        archi = open ('integrantesProyecto.csv', 'r')
        Reader = csv.reader (archi, delimiter= ';')
        band = True
        for fila in Reader:
            #fila[0] es idproy, fila[1] es apellnom, fila[2] es dni, fila[3] es categoria, fila[4] es rol
            if band:
                "saltear cabecera"
                band = not band
            else:
                idproy = fila[0]
                apellnom = fila[1]
                dni = int(fila[2])
                categ = fila[3]
                rol  =fila[4]
                if ((categ != 'I') and (categ != 'II') and (categ != 'III') and (categ != 'IV') and (categ != 'V')):
                    print("Datos de Integrantes proyecto no son validos\n")
                else:
                    unintegp = IntegrantesProyecto (idproy, apellnom, dni, categ, rol)
                    self.agregarInteg (unintegp)
        archi.close()
    
    def mostrarListadoInteP (self):
        for integP in self.__listaInteg:
            print("==".center(40, '='))
            integP.mostrarIntegrante()

    #metodos para calcular puntaje

    def contar (self, idBuscar):
        cont = 0
        for intproy in self.__listaInteg:
            if (idBuscar == intproy.getId()):
                cont += 1                       #contamos que hayan mas de 3 integrantes        
        return cont
    
    def validarDirector (self, idBuscar):
        band = False
        for intproy in self.__listaInteg:
            if (idBuscar == intproy.getId()):
                if (intproy.getRol() == 'director'):
                    band = True
        return band

    def validarCodirector (self, idBuscar):
        band = False
        for intproy in self.__listaInteg:
            if (idBuscar == intproy.getId()):
                if (intproy.getRol() == 'codirector'):
                    band = True
        return band

    def director (self, idBuscar):
        band = False
        for intproy in self.__listaInteg:
            if (idBuscar == intproy.getId()):
                if (intproy.getRol() == 'director'):
                    if ((intproy.getCategoria() == 'I') or (intproy.getCategoria() == 'II')):
                        band = True
        
        return band

    def coDirector (self, idBuscar):
        band = False
        for intproy in self.__listaInteg:
            if (idBuscar == intproy.getId()):
                if (intproy.getRol() == 'codirector'):
                    if ((intproy.getCategoria() == 'I') or (intproy.getCategoria() == 'II') or (intproy.getCategoria() == 'III')):
                        band = True
        
        return band
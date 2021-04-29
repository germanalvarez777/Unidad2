import csv
from claseCamion import Camion
class ManejadorCamion:
    __listaCamion = []
    def __init__ (self):
        self.__listaCamion = []
    def agregarLista (self, uncamion):
        self.__listaCamion.append(uncamion)
    def testListaCamion (self):
        archi = open ('camiones.csv', 'r')
        Reader = csv.reader(archi, delimiter = ',')
        band = True
        for fila in Reader:
            #fila[0] es id, fila[1] es nom, fila[2] patente, fila[3] marca, fila[4] tara
            if band:
                "saltear cabecera"
                band = not band
            else:
                id = int(fila[0])
                nom = fila[1]
                pat = fila[2]
                marca = fila[3]
                tara = float(fila[4])
                if ((id >= 1) and (id <= 20)):
                    unCamion = Camion(id, nom, pat, marca, tara)
                    self.agregarLista (unCamion)
                else:
                    print("Id Camion {} , patente {} no es valido". format(id, pat))
        archi.close()

    def buscarCamion (self, nroCamion, pesoTotalC):             
        for c in self.__listaCamion:
            if (c.getNro() == nroCamion):
                return pesoTotalC - c.getPeso()             #peso descargado = peso total-tara , pesototal > tara   
    def mostrarLista (self):
        for c in self.__listaCamion:
            print("Camion x".center(50, "="))
            c.mostrarCamion()
    def obtenerCamion (self, indice, pesototal):
        for camion in self.__listaCamion:
            if (camion.getNro() == indice):
                print("%s      %s           %.2f" %(camion.getPatente(), camion.getNombre(), self.buscarCamion(indice, pesototal)))

import csv
import os
from claseViajeroFrecuente import ViajeroFrecuente
# ejecutamos el programa desde modulo main2.py

class ManejadorViajero:
    __listaViajeros = []
    def __init__ (self):
        self.__listaViajeros = []
    def mostrarLista (self):
        for viajero in (self.__listaViajeros):
            viajero.mostrarDatos()
            print("".center(50, '-'),"\n")

    def agregarLista (self, unviajero):
        self.__listaViajeros.append(unviajero)
    def testListaViajeros (self):                 #apartado 1
        #recibimos instancias de viajeros desde archivo csv
        archivo = open ('viajeroFrecuente.csv', 'r')
        Reader = csv.reader(archivo, delimiter= ',')
        bandera = True
        for fila in Reader:
            if bandera:
                "saltear cabecera"
                bandera = not bandera
            else:
                nrov = int(fila[0])
                dni = int(fila[1].replace(".", "") )
                nombre = fila[2]
                apellido = fila[3]
                millas = int(fila[4])
                viajero = ViajeroFrecuente (nrov, dni, nombre, apellido, millas)
                self.agregarLista(viajero)
    def consultarMillas (self, numerov):                       #apartado 2a
        for viajero in self.__listaViajeros:
            if (viajero.getnroViajero() == numerov):
                print("La cantidad de millas del viajero {} es {}". format(viajero.getNombreViajero(), viajero.cantidadTotaldeMillas()))

    def acumular (self, numerov, m):                            #apartado 2b
        for viajero in self.__listaViajeros:
            if (viajero.getnroViajero() == numerov): 
                viajero.acumularMillas(m)
                print("Viajerx {} tiene nueva cantidad de millas {}".format(viajero.getNombreViajero(), viajero.cantidadTotaldeMillas()))   

    def canjear (self, numerov, m):                             #apartado 2c
        for viajero in self.__listaViajeros:
            if (viajero.getnroViajero() == numerov):
                viajero.canjearMillas(m)  

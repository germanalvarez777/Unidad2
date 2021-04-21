import csv
from claseManejadorCamion import ManejadorCamion
class Cosecha:
    __listaBi = []
    def __init__ (self):
        self.__listaBi = [[0 for j in range(20)] for i in range(45)]
    
    def testLista (self):
        archivo = open ('cosechaBodega.csv', 'r')
        Reader = csv.reader(archivo, delimiter = ',')
        bandera = True
        #cont = 1
        dias = []
        for fila in Reader:
            #fila[0] es id de camion, fila[1] es dia, fila[2] es pesototal camion
            if bandera:
                "salteamos la cabecera"
                bandera = not bandera
            else:
                dia = int(fila[1])
                idc = int(fila[0])
                peso = int(fila[2])   
                #print("dia ", dia, "idc ", idc, "peso ", peso)
                self.__listaBi[dia-1][idc-1] = peso
        archivo.close()  
              
    def buscarPeso (self, nroCamion):                           #opcion1 menu
        acum = 0
        for i in range (45):
            for j in range(20):
                if (nroCamion == j+1):
                    acum += self.__listaBi[i][j]
        return acum
        
    def mostrarDia (self, undia):                               #opcion2 menu
        manc = ManejadorCamion()
        manc.testListaCamion()
        for i in range(45):
            if (i+1 == undia):
                print("PATENTE          CONDUCTOR               CANTIDAD DE KILOS")
                for j in range(20):
                    if (self.__listaBi[i][j] > 0):              #peso total de algun camion positivo
                        peso = self.__listaBi[i][j]
                        manc.obtenerCamion(j+1, peso)
                
    def mostrarLista(self):
        for i in range(45):
            print("==============","Dia numero: ", i+1, "==============")
            print(self.__listaBi[i])            

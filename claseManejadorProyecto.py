import csv
from claseProyecto import Proyecto
class ManejadorProyecto:
    __listaProyecto = []
    def __init__ (self):
        self.__listaProyecto = []
    def agregarProyecto (self, unProyecto):
        self.__listaProyecto.append(unProyecto)
    def testListaProyecto (self):
        archivo = open ('proyectos.csv', 'r')
        Reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in Reader:
            # fila[0] es idproyecto, fila[1] es titulo, fila[2] son palabras claves
            if band:
                "salteamos la cabecera del archivo"
                band = not band
            else:
                id = fila[0]
                tit = fila[1]
                palabras = fila[2]
                if ((id != '0') or (tit != 'fin')):
                    unProyecto = Proyecto (id, tit, palabras)
                    self.agregarProyecto(unProyecto)
                else:
                    print("Datos de Proyecto no validos\n")
        
        archivo.close()
    def mostrarListadoProy (self):
        for proy in self.__listaProyecto:
            print("==".center(30, '='))
            proy.mostrarProyecto()

    #metodos para calcular y acumular puntaje
    def reglaNegocioA (self, mip):                                  #mip hace referencia al Manejador de Integrantes
        print('\n------El Proyecto debe tener como mínimo 3 integrantes------')
        for proy in self.__listaProyecto:
            idBuscar = proy.getIdProyecto()
            
            contador = mip.contar (idBuscar)
            
            if (contador >= 3):
                print("El proyecto {}, TIENE como minimo 3 integrantes, en total {}".format(idBuscar, contador))
                proy.acumularPuntos (10)
            else:
                print("El proyecto {}, NO tiene como minimo 3 integrantes, en total {}".format(idBuscar, contador))
                proy.restarPuntos (20)

    def reglaNegocioRoles (self, mip):
        print("\n------Un proyecto debe tener un Director y Codirector------")
        for proy in self.__listaProyecto:
            id = proy.getIdProyecto()
            validar1 = mip.validarDirector (id)
            validar2 = mip.validarCodirector (id)
            if (validar1 == True):
                print("El proyecto {} tiene un Director".format(id))
            else:
                print("El proyecto {} NO tiene un Director".format(id))
                proy.restarPuntos (10)
            
            if (validar2 == True):
                print("\nEl proyecto {} tiene un Codirector".format(id))
            else:
                print("\nEl proyecto {} NO tiene un Codirector".format(id))
                proy.restarPuntos (10)

    def reglaNegocioB (self, mip):
        print("\n------El Director del Proyecto debe tener categoría I o II------")
        for proy in self.__listaProyecto:
            id = proy.getIdProyecto()
            verificar = mip.director (id)
            if (verificar == True):
                print("El proyecto {} tiene un director con categoria I o II".format(id))
                proy.acumularPuntos (10)
            else:
                print("El proyecto {} NO tiene un director con categoria I o II".format(id))
                proy.restarPuntos (5)

    def reglaNegocioC (self, mip):
        print("\n------El Codirector del Proyecto debe tener como mínimo categoría III------")
        for proy in self.__listaProyecto:
            id = proy.getIdProyecto()
            verificar = mip.coDirector (id)
            if (verificar == True):
                print("El proyecto {} tiene un CoDirector con categoria I o II o III".format(id))
                proy.acumularPuntos (10)
            else:
                print("El proyecto {} NO tiene un CoDirector con categoria I o II o III".format(id))
                proy.restarPuntos (5)

    def calcularPuntaje (self, mip):
        self.reglaNegocioA (mip)
        self.reglaNegocioRoles(mip)
        self.reglaNegocioB (mip)
        self.reglaNegocioC (mip)

    def listadoOrdenado (self):
        #ordenamos la lista del manejador
        self.__listaProyecto.sort()
        #mostramos la lista en forma ordenada
        self.mostrarListadoProy()
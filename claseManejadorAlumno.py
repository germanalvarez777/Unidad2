import csv
from claseAlumnoEscuela import AlumnoEscuela
class ManejadorAlumno:
    __listaAlum = []
    def __init__ (self):
        self.__listaAlum = []
    def agregarAlumno (self, unAlumno):
        self.__listaAlum.append(unAlumno)
    def testListaAlumno (self):
        archivo = open('alumnoEscuela.csv', 'r')
        Reader = csv.reader(archivo, delimiter= ',')
        bandera = True
        for fila in Reader:
            #fila[0] es nombre del alumno, fila[1] es anio y division, fila[2] es cantid inasistencias
            if bandera:
                "saltear cabecera"
                bandera = not bandera
            else:
                nom = fila[0]
                aniodiv = fila[1]
                inas = int(fila[2])
                if (nom != 'fin'):
                    unAlumno = AlumnoEscuela (nom, aniodiv, inas)
                    self.agregarAlumno(unAlumno)
                else:
                    print("Datos de Alumno {} no validos\n".format(nom))
            
        archivo.close()
    def mostrarLista (self):
        for alum in self.__listaAlum:
            alum.mostrarAlumno()
            print("===".center(50, '='))

    def porcentaje (self, anioDiv):                     #opcion a
        print("Alumno               Porcentaje\n")
        for alum in self.__listaAlum:
            if (anioDiv == (alum.getDiv())):
                if (alum.getInas() > AlumnoEscuela.getMaxInasistencias()):
                    porc = (alum.getInas() * 100)/AlumnoEscuela.getMaxInasistencias()
                    print("%s       %3.2f" %(alum.getNombre(), porc-100))               #como el porcentaje supera los 100, restamos para solo mostrar el incremento
                else:
                    print("--Alumno {} no supero la cantidad max de inasistencias--\n".format(alum.getNombre()))
 

    def modificarInas (self, nuevaCant):                #opcion b
        AlumnoEscuela.setMaxInasistencias(nuevaCant)
        print("La nueva cantidad maxima de inasistencias es: ", AlumnoEscuela.getMaxInasistencias())

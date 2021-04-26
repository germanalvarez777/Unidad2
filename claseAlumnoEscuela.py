class AlumnoEscuela:
    cantMaxClases = 180
    cantMaxInasistencias = 30           #datos miembros estaticos (variables de clase)
    __nombre = ''
    __aniodivision = ''
    __cantInasistencias = 0
    def __init__ (self, nom='', andiv='', cant=0):
        self.__nombre = nom
        self.__aniodivision = andiv
        self.__cantInasistencias = cant
    def mostrarAlumno (self):
        print("Nombre: {} -  Anio y Division: {} - Inasistencias: {}\n".format(self.__nombre, self.__aniodivision, self.__cantInasistencias))

    def contarInasistencia (self, cant):
        self.__cantInasistencias += cant

    def getDiv (self):
        return self.__aniodivision

    def getInas (self):
        return self.__cantInasistencias
    def getNombre (self):
        return self.__nombre

    @classmethod
    def getCantClases (cls):
        return cls.cantMaxClases
    @classmethod
    def getMaxInasistencias (cls):                  #funciones miembro estatico
        return cls.cantMaxInasistencias
    @classmethod
    def setMaxInasistencias (cls, valor):
        cls.cantMaxInasistencias = valor
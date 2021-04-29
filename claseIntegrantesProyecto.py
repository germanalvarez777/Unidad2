class IntegrantesProyecto:
    __Idproyecto = ''
    __apellidoNom  = ''
    __dni = 0
    __categoria = ''
    __rol = ''
    def __init__ (self, id='', apell='', dni = 0, cat = '', rol=''):
        self.__Idproyecto = id
        self.__apellidoNom = apell
        self.__dni = dni
        self.__categoria = cat
        self.__rol = rol
    def mostrarIntegrante (self):
        print("Nombre: {} \nId Proyecto: {}\nDNI: {} \nCategoria: {} \nRol: {}".format(self.__apellidoNom, self.__Idproyecto, self.__dni, self.__categoria, self.__rol))
    def getId (self):
        return self.__Idproyecto
    def getNombre (self):
        return self.__apellidoNom
    def getDni (self):
        return self.__dni
    def getCategoria (self):
        return self.__categoria
    def getRol (self):
        return self.__rol    
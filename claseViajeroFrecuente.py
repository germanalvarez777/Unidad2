class ViajeroFrecuente:
    __nroViajero = 0
    __dni = 0
    __nombre = ''
    __apellido = ''
    __millasAcum = 0
    def __init__ (self, nrov=0, dni = 0, nombre='', apellido='', millasacum=0):
        self.__nroViajero = nrov
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millasAcum = millasacum
    
    def __str__(self):
        return "%d %d %s %s %d" % (self.__nroViajero, self.__dni, self.__nombre, self.__apellido, self.__millasAcum)

    def getnroViajero (self):
        return self.__nroViajero

    def getNombreViajero (self):
        return self.__nombre + self.__apellido

    def cantidadTotaldeMillas (self):
        return self.__millasAcum

    def acumularMillas (self, millas):
        self.__millasAcum += millas
        
    def canjearMillas (self, cantmillas):
        if (cantmillas <= self.__millasAcum):
            print("Se puede canjear la cantidad de millas determinada".center (10, "-"))
        else:
            print("Error en la operacion de canjear millas")
    def mostrarDatos (self):
        print("\nNumero Viajero: {} - DNI: {} - Nombre: {} - Apellido: {} - Millas: {}\n".format(self.__nroViajero, self.__dni, self.__nombre, self.__apellido, self.__millasAcum))

#para verificar la correcion de clase viajero
"""
if __name__ == '__main__':
    nro = int(input("Ingrese el numero del viajero: "))
    dni = int(input ("Ingrese el dni del viajero {}: ".format(nro)))
    nombre = input("Ingrese el nombre del viajero: ")
    apellido = input("Ingrese el apellido del viajero: ")
    millas = int(input("Ingrese la cantidad de millas que cuenta: "))

    v = ViajeroFrecuente(nro, dni, nombre, apellido, millas)
    v.mostrarDatos()
    print("Millas acumuladas: ", v.cantidadTotaldeMillas())
    acum = int(input("Ingrese la cantidad de millas recorridas en el ultimo viaje:\n "))
    v.acumularMillas (acum)
    print("Nuevas millas acumuladas: ", v.cantidadTotaldeMillas())
    canjear = int(input("Ingrese las millas a canjear: "))
    v.canjearMillas (canjear)
"""
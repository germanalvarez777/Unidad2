import csv
from claseEmail import Email

class ManejadorEmail:
    __listaemail = []
    def __init__ (self):
        self.__listaemail = []

    def agregarEmail (self, unCorreo):
        self.__listaemail.append(unCorreo)

    def getunEmail (self, indice):
        return self.__listaemail[indice]

    def mostrarLista (self):
        print("\nMostramos la informacion de la lista". center(25, "="))
        for email in self.__listaemail:
            email.mostrarDatos()

    def testLista (self, direccion):                       #apartado3
        c = Email ()
        c.crearCuenta(direccion)
        self.agregarEmail(c)


def envioMsj (unCorreo, nombre):      #apartado1   
    print("Estimado {}, te enviaremos tus mensajes a la dirección {}".format(nombre, unCorreo.retornaEmail()))
    
def modificarClave (unCorreo):        #apartado2
    op = input("Usted ha ingresado la clave por defecto=(12345) ?(s/n)")
    if (op == 's'):
        claveVieja = '12345'
    else:
        claveVieja = input("Ingrese la clave de su cuenta: ")

    claveAc = unCorreo.getClave() 
    print("Clave actual: {}".format(claveAc))
    if (claveVieja == claveAc):
        newClave = input ("Ingrese una nueva contraseña: ")
        print("Nueva clave es ", newClave)
        unCorreo.setClave(newClave)
    else:
        print("La clave de la cuenta email es incorrecta")
    
def testArchivocsv ():
    dom = str(input("Ingrese un dominio a trabajar: "))
    cont = 0
    archivo = open ('direccionesEmail.csv')       # el modo lectura "r" no hace falta detallar
    Reader = csv.reader (archivo, delimiter = ",")
    emailEj = Email()           #le asigno valores por defecto
    for comp in Reader:
            for i in range(10): 
                emailEj.crearCuenta(comp[i])
                domin = emailEj.getDominio()
                if dom == domin:
                    cont += 1

    print("La cantidad de direcciones con dominio igual al ingresado es ", cont)

def test ():
    print("TEST".center(40,'='))
    idcuenta = input("Ingrese el id de la cuenta: ")
    dom = input("Ingrese el dominio: ")
    tipod = input("Ingrese el tipo de dominio: ")
    clave = input ("Ingrese la clave: ")
    emTest = Email(idcuenta, dom, tipod, clave)
    emTest.mostrarDatos()

    cuentaTest = Email()
    direcc = input("Ingrese una direccion: ")
    cuentaTest.crearCuenta(direcc)
    cuentaTest.mostrarDatos()


if __name__ == '__main__':
    #Probamos la funcionalidad

    test()
    print("\n----Ha finalizado el testeo de datos----")
    input("Presione enter para continuar: ")

    claveDefecto = '12345'
    manejE = ManejadorEmail()
    asig = input ("Quiere asignarle ala persona la clave por defecto?(s/n): ")
    if (asig == 's'):
        print("La clave por defecto es 12345")
    elif (asig == 'n'):
        claveDefecto = input("Ingrese la contraseña de la persona: ")
    else:
        print("No selecciono la opcion correcta")
    
    idcuenta = input("Ingrese el id de la cuenta: ")
    dom = input("Ingrese el dominio: ")
    tipod = input("Ingrese el tipo de dominio: ")

    em = Email(idcuenta, dom, tipod, claveDefecto)
    manejE.agregarEmail(em)
    #Apartado 1
    print("Apartado 1".center(50, "*"))
    nombre = input("Ingrese el nombre de una persona: ")
    envioMsj(em, nombre)
    #Apartado 2
    print("Apartado 2".center(50, "*"))
    modificarClave(em)
    print("\n")
    #Apartado 3
    print("Apartado 3".center(50, "*"))
    dircorreo = input("Ingrese un correo electronico\n")
    # manejE.testLista(em.retornaEmail())       Funciona retornando un email
    manejE.testLista (dircorreo)
    manejE.mostrarLista()
    print("\n")
    #Apartado 4
    print("Apartado 4".center(50, "*"))
    print("-----Trabajamos con archivo csv-----")
    testArchivocsv ()
    

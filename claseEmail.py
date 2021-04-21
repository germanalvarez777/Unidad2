class Email:
    __idCuenta = ''
    __dominio = ''
    __tipoDom = ''
    __clave = ''
    def __init__ (self, idcuenta= '', dominio= '', tipod= '', contras= ''):
        self.__idCuenta = idcuenta
        self.__dominio = dominio
        self.__tipoDom = tipod
        self.__clave = contras
    def retornaEmail (self):
        return self.__idCuenta + '@'+ self.__dominio+'.'+ self.__tipoDom
    def getDominio (self):
        return self.__dominio
    def getIdCuenta (self):
        return self.__idCuenta
    def setClave (self, c):
        self.__clave = c
    def getClave (self):
        return self.__clave
    def crearCuenta (self, Dirccorreo):
        i = Dirccorreo.rfind('@')               #utilizamos rfind, para q busque el caracter desde el ultimo hacia adelante
        j = Dirccorreo.rfind('.')
        print("".center(50,"="), "\n")
        if ((i != -1) & (j != -1)):             #coloco -1 para comparar que se haya encontrado, sino find retorna -1
            self.__idCuenta = Dirccorreo[:i]
            self.__dominio = Dirccorreo[i+1:j]
            self.__tipoDom = Dirccorreo[j+1:]
            if ((self.__idCuenta != '') and (self.__dominio != '') and (self.__tipoDom != '')):
                print("Id {}, dominio {}, tipod {}".format(self.__idCuenta, self.__dominio, self.__tipoDom))
                print("Contraseña: ", self.__clave)
            else:
                print("Direccion de correo electronico incorrecto")
                self.__dominio = ''
        else:
            print("Direccion de correo electronico incorrecto")  
            self.__dominio = '' 
       
    def mostrarDatos (self):
        print("Id de Cuenta: {} - Dominio: {} - Tipo de Dominio: {} - Clave: {}". format(self.__idCuenta, self.__dominio, self.__tipoDom, self.__clave))

#Colocamos este main para verificar el uso de la clase Email
""" 
if __name__ == '__main__':
    #crearEmail()
    cadena = "german@gmail.com"
    print("Ingresamos los siguientes valores para crear un Email\n")
    idcuenta = input("Ingrese un identificador para su correo: ")
    dominio = input("Ingrese un dominio de correo (Gmail-Outlook- Hotmail):\n")
    tipod = input("Ingrese tipo de dominio (com, net, org, edu): ")       
    contra = input ("Ingrese una contraseña apropiada: ")
    unCorreo = Email (idcuenta, dominio, tipod, contra)    
    unCorreo.crearCuenta (unCorreo.retornaEmail())
"""

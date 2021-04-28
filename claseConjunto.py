class Conjunto:
    __lista = []
    def __init__ (self):
        self.__lista = []
    def mostrarConjunto (self):
        for i in range (len(self.__lista)):
            print("Elemento nº ", i+1, "" .center(50, "="))
            print("Valor del elemento: {}".format(self.__lista[i]))
    
    def buscarValor (self, unvalor):
        valor = 0
        i = 0
        while i < (len(self.__lista)):
            if (unvalor == self.__lista[i]):
                valor = -1
            i += 1
        return valor

    def getValor (self, indice):
        return self.__lista[indice]    

    def longitud (self):
        return (len(self.__lista))

    def cargarConjunto (self):
        valor = int(input("Ingrese un valor entero(Distinto de -1): "))
        while (valor != -1):
            validar = self.buscarValor (valor)
            if (validar != -1):
                self.__lista.append (valor)
            else:
                print("Elemento del conjunto repetido:\n")
            valor = int(input("Ingrese un valor entero: "))
    
    def buscarElem (self, elem, otroConj):
        b = False
        indice = 0
        while indice < (otroConj.longitud()):               #UTILIZAR WHILE
            if (elem == otroConj.getValor(indice)):
                b = True
            indice += 1
        return b

    def __add__ (self, otroConj):
        if (type(self) == type(otroConj)):
            suma = Conjunto()
            #suma = self.__lista.extend([otroConj])
            lon = otroConj.longitud()
            l = self.longitud()
            for j in range(l):
                suma.__lista.append(self.__lista[j])            #agregamos elementos del primer conjunto
            
            #analizamos si se repiten elementos en el segundo conjunto
            for i in range(lon):                         
                if (self.buscarElem(otroConj.getValor(i), suma) == False):       #no hay elementos iguales   
                    suma.__lista.append(otroConj.getValor(i))               #agregamos elementos del 2do conjunto
            #suma.mostrarConjunto()
            return suma.__lista
 
    def __sub__ (self, otroConj):
        band = False
        if (type(self) == type(otroConj)):
            resta = Conjunto()
            for i in range (self.longitud()):
                for j in range(otroConj.longitud()):
                    band = self.buscarElem (self.__lista[i], otroConj)
                    if (band == False):                                     #no se encontro el elemento
                        if (self.buscarElem(self.__lista[i], resta) == False):           #para que no se repitan los elementos
                            resta.__lista.append(self.__lista[i])

            #resta.mostrarConjunto()                                  #en la diferencia, el conj resultante es el primero y mayor
            return resta.__lista

    def __eq__ (self, otroConj):
        cont = 0
        band = False
        if (type(self) == type(otroConj)):
            l = len(self.__lista)
            #print("Longitud de otro: ", otroConj.longitud(), "y de self: ", l)
            if (l == (otroConj.longitud())):
                for i in range (l):
                    j = self.buscarElem(self.__lista[i], otroConj)
                    if (j == True):
                        #print("Conteo: ", cont)
                        cont += 1
            if (cont == otroConj.longitud()):           #el contador de igualdades coincide con long de los conjuntos
                band = True
        
        return band

class FechaHora:
    __dia = 0
    __mes = 0
    __anio = 0
    __hs = 0
    __min = 0
    __seg = 0
    def __init__ (self, d=1, m=1, a=2020, h=0, mi=0, s=0):    
        self.__dia = d
        self.__mes = m
        self.__anio = a
        self.__hs = h
        self.__min = mi
        self.__seg = s

    def validar (self):
        if ((self.__dia <= 31) and (self.__mes <= 12) and (self.__hs <= 24) and (self.__min < 60) and (self.__seg < 60)):
            if ((self.__dia <= 31) and ((self.__mes == 1) or (self.__mes == 3) or (self.__mes == 5) or (self.__mes == 7) or (self.__mes == 8) or (self.__mes == 10) or (self.__mes == 12))):
                print("{}/{}/{} - hora {}:{}:{} es valido\n".format(self.__dia,self.__mes,self.__anio,self.__hs,self.__min,self.__seg))
            
            elif ((self.__dia <= 30) and ((self.__mes == 4) or (self.__mes == 6) or (self.__mes == 9) or (self.__mes == 11))):
                print("{}/{}/{} - hora {}:{}:{} es valido\n".format(self.__dia,self.__mes,self.__anio,self.__hs,self.__min,self.__seg))
            
            elif ((self.__mes == 2) and (self.__dia <= 29)):
                print("Mes de febrero con dia valido para fecha {}/{}/{} - hora {}:{}:{}\n".format(self.__dia,self.__mes,self.__anio,self.__hs,self.__min,self.__seg))
            else:
                print("{}/{}/{} no es una Fecha valida\n".format(self.__dia, self.__mes,self.__anio))
                self.cambios()
                self.Mostrar()      
        else:
            print("Fecha {}/{}/{} - hora {}:{}:{}  con datos erroneos\n".format(self.__dia,self.__mes,self.__anio,self.__hs,self.__min,self.__seg))
            self.cambios()
            self.Mostrar()


    def Mostrar (self):
        print("Dia: {}, Mes: {}, Anio: {}, Hora: {}, Min: {}, Segundo: {}".format(self.__dia, self.__mes, self.__anio, self.__hs, self.__min, self.__seg))
        print("===".center(50, '='))

    def validarBisiesto(self):
        if ((self.__anio  %4 == 0) and (self.__anio % 100 == 0) and (self.__anio % 400 == 0)):
            print("\nEl anio actual {} es biciesto, tiene 366 dias\n".format(self.__anio))
            return True
        else:
            print("\nEl anio actual {} no es biciesto(es Natural), tiene 365 dias\n".format(self.__anio))
            return False

    def cambios (self): 
        bisiesto = self.validarBisiesto()
        if (self.__seg == 60):
            self.__min += 1
            self.__seg = 0
        elif (self.__seg > 60):
            self.__min += self.__seg // 60               #asignamos nuevo valor a min
            self.__seg = self.__seg - 60
        if (self.__min == 60):
            self.__hs += 1
            self.__min = 0
        elif (self.__min > 60):
            self.__hs += self.__min // 60                #asignamos nuevo valor a hora
            self.__min = self.__min - 60
        if (self.__hs == 24):
            self.__dia += 1
            self.__hs = self.__hs- 24
        elif (self.__hs > 24):
            self.__dia += self.__hs // 24                #asignamos nuevo valor a dia
            self.__hs = self.__hs - 24
        if ((self.__dia == 31) and ((self.__mes == 1) or (self.__mes == 3) or (self.__mes == 5) or (self.__mes == 7) or (self.__mes == 8) or (self.__mes == 10) or (self.__mes == 12))):
            self.__mes += 1
            self.__dia = 1
        elif ((self.__dia == 30) and ((self.__mes == 4) or (self.__mes == 6) or (self.__mes == 9) or (self.__mes == 11))):
            self.__mes += 1
            self.__dia = 1
        elif (self.__dia > 31):
            self.__mes += (self.__dia // 30)             #asignamos nuevo valor a mes
            self.__dia = self.__dia - 31
            if (self.__dia > 31):
                self.__mes += (self.__dia // 30)
                self.__dia = self.__dia - 31
        if (self.__mes > 12): 
            self.__anio += 1
            self.__mes = self.__mes - 12
            if (self.__mes > 12):                   #se evalua si el total de meses sigue siendo mayor a 12
                self.__anio += 1
                self.__mes = self.__mes - 12
        if bisiesto:
            if ((self.__dia == 29) and (self.__mes == 2)):
                print("Febrero 29 Biciesto")
                self.__mes += 1
                self.__dia = 1
                self.__hs = 0
        else:
            if ((self.__dia == 28) and (self.__mes == 2)):
                print("Febrero 28 Natural")
                self.__mes += 1
                self.__dia = 1
                self.__hs = 0
        if ((self.__mes == 12) and (self.__dia == 31)):
            self.__anio += 1
            self.__mes = 1
            self.__dia = 1
            self.__hs = 0
            self.__min = 0
            self.__seg = 0

    def PonerEnHora (self, h=0, mi=0, s=0):
        if ((h <= 24) and (mi <= 60) and (s <= 60)):
            self.__hs = h
            self.__min = mi
            self.__seg = s
        else:
            print("El horario ingresado es incorrecto\n")   
        self.cambios()

    def AdelantarHora (self, h=0, mi=0):
        if ((h <= 24) and (mi <= 60)):
            self.__hs += h
            self.__min += mi
            self.cambios()
        else:
            print("El horario a adelantar es incorrecto\n")
    
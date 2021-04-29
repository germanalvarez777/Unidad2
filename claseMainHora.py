from claseFechaHora import FechaHora
from claseHora import Hora
if __name__ == '__main__':

   d = int(input("Ingrese Dia: "))

   mes = int(input("Ingrese Mes: "))

   a = int(input("Ingrese Año: "))

   h = int(input("Ingrese Hora: "))

   m = int(input("Ingrese Minutos: "))

   s = int(input("Ingrese Segundos: "))

   f = FechaHora(d,mes,a,h, m, s)
   f.Mostrar()
   f.validar()

   input("Presione una tecla para continuar1: ")

   h1 = int(input("Ingrese Hora: "))

   m1 = int(input("Ingrese Minutos: "))

   s1 = int(input("Ingrese Segundos: "))

   r = Hora(h, m, s)
   r.MostrarHora()

   input("Presione una tecla para continuar2: ")

   f2 = f +r

   f2.Mostrar()
   f2.validar()

   input("Presione una tecla para continuar3: ")

   f3 = r + f

   f3.Mostrar()
   f3.validar()
   input("Presione una tecla para continuar4: ")

   f4 = f3 - 1 # Al restar un número entero a un objeto FechaHora se debe restar la cantidad de días indicada por el número entero

   f4.Mostrar()
   f4.validar()
   f4 = 1 + f2 # suma un día a un objeto FechaHora

   input("Presione una tecla para continuar5: ")
   f4.Mostrar()
   f4.validar()     
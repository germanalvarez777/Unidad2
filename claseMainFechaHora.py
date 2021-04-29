import os
import csv
from claseMenuFechaHora import MenuFechaHora
from claseFechaHora import FechaHora

def cargarFecha ():
    #hacemos todos los input
    d=int(input("Ingrese Dia: "))
    mes=int(input("Ingrese Mes: "))
    a=int(input("Ingrese Año: "))
    h=int(input("Ingrese Hora: "))
    m=int(input("Ingrese Minutos: "))
    s=int(input("Ingrese Segundos: "))
    fecha = FechaHora(d,mes,a,h,m,s)
    print("==".center(50, '='))
    return fecha

def test ():
    print("TEST".center(50,'='))
    print("Cargamos la primera fecha Test: ")
    unaFechaTest = cargarFecha()
    print("Cargamos la segunda fecha Test: ")
    otraFechaTest = cargarFecha()

    unaFechaTest.Mostrar()
    otraFechaTest.Mostrar()

if __name__ == '__main__':

    test()
    print("----Ha finalizado el testeo----")
    input("Presione una tecla para continuar: ")

    print("Cargamos la primera fecha: ")
    unaFecha = cargarFecha()
    print("Cargamos la segunda fecha: ")
    otraFecha = cargarFecha()
    #unaFecha = FechaHora (31,12,2020,24,59,59)
    #otraFecha = FechaHora (31,12,2021,22,57,55)

    unaFecha.Mostrar()
    otraFecha.Mostrar()

    menu = MenuFechaHora()
    salir = True
    while salir:
        print("""
            Menu de Opciones
            1- Sumar dos objetos de la clase FechaHora, con sobrecarga(+).
            2- Restar dos objetos de la clase FechaHora, con sobrecarga(-). 
            3- Distinguir entre dos objetos de la clase FechaHora, cual es el mayor (>).
            """)
        op = (input('Ingrese una opcion: '))
        os.system('clear')                              #Windows utilizamos cls, en Linux clear
        if ((op != '1') and (op != '2') and (op != '3') and (op != '4')):
            print("Opcion no valida")
            salir = False
        else:
            if (op == '4'):
                menu.salir()
                salir = False
            else:
                menu.opcion(op, unaFecha, otraFecha)
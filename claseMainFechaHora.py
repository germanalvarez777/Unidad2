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

if __name__ == '__main__':
    print("Cargamos la primera fecha: ")
    #unaFecha = cargarFecha()
    print("Cargamos la segunda fecha: ")
    #otraFecha = cargarFecha()
    unaFecha = FechaHora (23,4,2031,17,42,55)
    otraFecha = FechaHora (23,4,2031,17,42,58)

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
        menu.opcion(op, unaFecha, otraFecha)
        if ((op != '1') and (op != '2') and (op != '3')):
            salir = False

from claseMenuCamion import MenuCamion
import os
import csv
from claseCosecha import Cosecha
from claseManejadorCamion import ManejadorCamion

def test ():
    print("TEST".center(40, '='))
    mcTest = ManejadorCamion()
    mcTest.testListaCamion()
    print("Mostramos la lista de camiones")
    mcTest.mostrarLista()
    cosTest = Cosecha()
    print("Se carga la lista Bidimensional desde el archivo csv\n")
    cosTest.testLista()
    print("Ingresamos algunos pesos desde el teclado\n")
    cosTest.acumularPesos()
    print("\nMostramos la lista Bidimensional de Cosecha")
    cosTest.mostrarLista()

if __name__ == '__main__':

    test()
    print("\n--Ha finalizado el testeo de datos---")
    input("Presione una tecla para continuar: ")

    mc = ManejadorCamion()
    mc.testListaCamion()
    print("Mostramos la lista de camiones")
    mc.mostrarLista()
    cos = Cosecha()
    print("Se carga la lista Bidimensional desde el archivo csv\n")
    cos.testLista()
    print("Ingresamos algunos pesos desde el teclado\n")
    cos.acumularPesos()
    print("\nMostramos la lista Bidimensional de Cosecha")
    cos.mostrarLista()

    menu = MenuCamion()
    salir = True
    while salir:
        print("""
            Menu de Opciones
            1- Ingresar un camion y mostrar kg descargados.
            2- Ingresar un dia y mostrar su listado. 
            3- Salir.
            """)
        op = (input('Ingrese una opcion: '))
        os.system('clear')                              #Windows utilizamos cls, en Linux clear
        if ((op != '1') and (op != '2') and (op != '3')):
            print("Opcion no valida")
            salir = False
        else:
            if (op == '3'):
                menu.salir()
                salir = False
            else:
                menu.opcion(op, cos)
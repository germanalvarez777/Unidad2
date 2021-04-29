import csv
import os
from claseViajeroFrecuente import ViajeroFrecuente
from claseManejadorViajero import ManejadorViajero
from claseMenuViajero import Menu

if __name__ == '__main__':          #cuando hacemos la lectura del archivo csv, la mejor opcion es hacerla desde main
    
    mv = ManejadorViajero()
    mv.testListaViajeros()
    print("Mostramos la Lista generada".center(40, "="))
    mv.mostrarLista()
    numero = int(input("Ingrese un numero de viajero: "))

    b = mv.validarNro (numero)
    if (b == True):
        print("Numero de viajero valido\n")
    else:
        print("Numero de viajero no valido\n")
        numero = int(input("Ingrese un numero de viajero valido: "))

    menu = Menu()
    salir = True
    while salir:
        print("""
            Menu de Opciones
            a- Consultar Cantidad de Millas.
            b- Acumular Millas. 
            c- Canjear Millas.
            """)
        op = (input('Ingrese una opcion: '))
        os.system('clear')                              #Windows utilizamos cls, en Linux clear
        if ((op != 'a') and (op != 'b') and (op != 'c') and (op != 'd')):
            print("\nOpcion no valida")
            salir = False
        else:
            if (op == 'd'):
                menu.salir()
                salir = False
            else:  
                menu.opcion(op, numero)

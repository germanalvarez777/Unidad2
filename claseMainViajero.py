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

    menu = Menu()
    salir = True
    while salir:
        #print("\n------------Menu------------\n1- Inciso a\n2- Inciso b\n3- Inciso c\n4- Salir\n")
        print("""
            Menu de Opciones
            a- Consultar Cantidad de Millas.
            b- Acumular Millas. 
            c- Canjear Millas.
            """)
        op = (input('Ingrese una opcion: '))
        os.system('clear')                              #Windows utilizamos cls, en Linux clear
        menu.opcion(op, numero)
        if ((op != 'a') and (op != 'b') and (op != 'c')):
            salir = False
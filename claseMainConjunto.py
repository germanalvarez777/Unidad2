import os
from claseMenuConjunto import MenuConjunto
from claseConjunto import Conjunto
if __name__ == '__main__':
    con1 = Conjunto ()
    con1.cargarConjunto()
    conj2 = Conjunto ()
    conj2.cargarConjunto()
    salir = True

    print("\n--Mostramos el primer conjunto--")
    con1.mostrarConjunto()
    print("\n--Mostramos el segundo conjunto--")
    conj2.mostrarConjunto()
    menu = MenuConjunto()
    while salir:
        print("""
            Menu de Opciones
            1- Sumar dos conjuntos (Union), con sobrecarga(+).
            2- Restar dos conjuntos (Diferencia), con sobrecarga(-). 
            3- Distinguir si los conjuntos son iguales, con sobrecarga (==).
            """)
        op = (input('Ingrese una opcion(4 para salir): '))
        os.system('clear')                              #Windows utilizamos cls, en Linux clear
        
        if ((op != '1') and (op != '2') and (op != '3') and (op != '4')):
            print("\nOpcion no valida")
            salir = False
        else:
            if (op == '4'):
                menu.salir()
                salir = False
            else:
                menu.opcion(op, con1, conj2)
    
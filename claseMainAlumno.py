import os
from claseMenuAlumno import MenuAlumno
from claseManejadorAlumno import ManejadorAlumno
from claseAlumnoEscuela import AlumnoEscuela
if __name__ == '__main__':
    ma = ManejadorAlumno()
    ma.testListaAlumno()
    print("-----Mostramos la lista de Alumnos-----\n")
    ma.mostrarLista()
    menu = MenuAlumno()
    salir = True
    while salir:
        print("""
            Menu de Opciones
            a- Ingresar un año y división, y mostrar listado de alumnos.
            b- Modificar la cantidad maxima de inasistencias permitidas. 
            c- Salir.
            """)
        op = (input('Ingrese una opcion: '))
        os.system('clear')                              #Windows utilizamos cls, en Linux clear
        if ((op != 'a') and (op != 'b') and (op != 'c')):
            print("Opcion no valida")
            salir = False
        else:
            if (op == 'c'):
                menu.salir()
                salir = False
            else:
                menu.opcion(op)

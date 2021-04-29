from claseManejadorProyecto import ManejadorProyecto
from claseManejadorIntegProyecto import ManejadorIntegProyecto

def test ():
    print("TEST".center(40, '='))
    mpTest = ManejadorProyecto()
    mpTest.testListaProyecto()
    print("Mostramos el listado de proyectos: ")
    mpTest.mostrarListadoProy()

    mipTest = ManejadorIntegProyecto()
    mipTest.testListaInteg()
    print("Mostramos el listado de integrantes: ")
    mipTest.mostrarListadoInteP()


if __name__ == '__main__':

    test()
    print("Testeo de datos ha finalizado".center(40, '-'))
    input("Presione enter para continuar: ")
    mp = ManejadorProyecto()
    mp.testListaProyecto()

    mip = ManejadorIntegProyecto()
    mip.testListaInteg()
    print("Mostramos el listado de integrantes: ")
    mip.mostrarListadoInteP()

    mp.calcularPuntaje(mip)
    
    print("\nMostramos el listado de Proyectos en forma ordenada(ascendente) por puntaje\n")
    mp.listadoOrdenado ()

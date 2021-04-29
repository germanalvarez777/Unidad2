from claseManejadorProyecto import ManejadorProyecto
from claseManejadorIntegProyecto import ManejadorIntegProyecto

def test ():
    print("TEST".center(40, '='))
    mpTest = ManejadorProyecto()
    mpTest.testListaProyecto()

    mipTest = ManejadorIntegProyecto()
    mipTest.testListaInteg()
    print("Mostramos el listado de integrantes: ")
    mipTest.mostrarListadoInteP()

    mpTest.calcularPuntaje(mipTest)
    
    print("\nMostramos el listado de Proyectos en forma ordenada(ascendente) por puntaje\n")
    mpTest.listadoOrdenado ()

if __name__ == '__main__':

    test()
    print("Testeo de datos ha finalizado".center(30, '-'))
    mp = ManejadorProyecto()
    mp.testListaProyecto()

    mip = ManejadorIntegProyecto()
    mip.testListaInteg()
    print("Mostramos el listado de integrantes: ")
    mip.mostrarListadoInteP()

    mp.calcularPuntaje(mip)
    
    print("\nMostramos el listado de Proyectos en forma ordenada(ascendente) por puntaje\n")
    mp.listadoOrdenado ()

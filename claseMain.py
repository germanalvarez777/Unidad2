from claseManejadorProyecto import ManejadorProyecto
from claseManejadorIntegProyecto import ManejadorIntegProyecto

if __name__ == '__main__':
    mp = ManejadorProyecto()
    mp.testListaProyecto()

    mip = ManejadorIntegProyecto()
    mip.testListaInteg()
    print("Mostramos el listado de integrantes: ")
    mip.mostrarListadoInteP()

    mp.calcularPuntaje(mip)
    
    print("\nMostramos el listado de Proyectos en forma ordenada(ascendente) por puntaje\n")
    mp.listadoOrdenado ()

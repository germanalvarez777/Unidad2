from claseFechaHora import FechaHora
if __name__ == '__main__':

    d=int(input("Ingrese Dia: "))
    mes=int(input("Ingrese Mes: "))
    a=int(input("Ingrese Año: "))
    h=int(input("Ingrese Hora: "))
    m=int(input("Ingrese Minutos: "))
    s=int(input("Ingrese Segundos: "))

    r = FechaHora () #  inicilizar día, mes, año con 1/1/2020, y hora, minutos    segundos con 0h, 0m, 0s.
    r.validar()
    r1 = FechaHora(d,mes,a); # inicializar con 0h 0m 0s
    r1.validar()
    r2= FechaHora(d,mes,a,h, m, s)
    r2.validar
    r3 = FechaHora(30,8,2030,29,45,11)
    r3.validar
    r3.Mostrar()
    r4 = FechaHora (28,2,2000,12,45,33)
    r4.validar()
    r4.Mostrar()
    r4.AdelantarHora(5,3)
    r4.Mostrar()
    r1.Mostrar()

    r2.Mostrar()

    input("Presione una tecla para continuar1: ")

    r.PonerEnHora(5) # solamente la hora

    r.Mostrar()

    input("Presione una tecla para continuar2: ")

    r2.PonerEnHora(13,30) #hora y minutos

    r2.Mostrar()

    input("Presione una tecla para continuar3: ")

    r.PonerEnHora(14, 30, 25) #hora, minutos y segundos

    r.Mostrar()

    input("Presione una tecla para continuar4: ")

    r.AdelantarHora(3) #sumar 3 horas a la hora actual

    r.Mostrar()

    input("Presione una tecla para continuar5: ")

    r1.AdelantarHora(1,15) #sumar 1 hora y 15 minutos a la hora actual

    r1.Mostrar()
    
    # Agregamos unos lotes de prueba para verificar los requisitos
    
    input("Presione una tecla para continuar6: ")
    r2.AdelantarHora (11,30)
    r2.Mostrar()
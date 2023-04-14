tupla = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
try:
    N = input("Ingrese el numero del mes: ")
    print("El mes es: ", tupla[int(N)-1])
except ValueError:
    print("Solo se permiten numeros")
except IndexError:
    print("Solo se permiten numeros entre 1 y 12")
    
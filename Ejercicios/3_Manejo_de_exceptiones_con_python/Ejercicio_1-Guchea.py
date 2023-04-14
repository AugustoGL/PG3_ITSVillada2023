def suma():
    try:
        a = float(input("Ingrese el primer numero: "))
        b = float(input("Ingrese el segundo numero: "))
        print("La suma de los dos numeros es: ", a + b)
    except ValueError:
        print("Error: Solo se permiten numeros")
    else:
        print("La operacion se ha realizado correctamente")
    finally:
        print("Fin de la operacion")

suma()
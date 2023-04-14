def division():
    try:
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        print("La division es: ", num1/num2)
    except ZeroDivisionError:
        print("No se puede dividir entre 0")

division()
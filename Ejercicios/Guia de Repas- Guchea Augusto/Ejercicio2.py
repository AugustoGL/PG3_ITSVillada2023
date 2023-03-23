a=int(input("Ingrese un año: "))
if a%4==0 and a%100!=0 or a%400==0:
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")
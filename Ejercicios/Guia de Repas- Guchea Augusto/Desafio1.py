print("Ingrese la altura del triangulo")
altura= int(input())
print("Ingrese el caracter del triangulo")
caracter= input()
print("-"*10)
for i in range(altura):
    print(" "* (altura -i -1) + caracter * (2 *i +1) )

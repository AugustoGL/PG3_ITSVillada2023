print("Ingrese la frase:")
frase= input()
contador= 0
for i in frase:
    for x in "AEIOUaeiou":
        if i == x:
            print("xf")
            contador+=1

print("Hay", contador,"vocales")
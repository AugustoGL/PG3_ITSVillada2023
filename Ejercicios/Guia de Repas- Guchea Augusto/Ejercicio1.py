vector=[23,56,76,23,89,12]
print("Ingrese el numero que quiere encontrar:")
num = int(input())
for i in vector:
    if i == num:
        print("Se encuntra en la posicion ",vector.index(i))

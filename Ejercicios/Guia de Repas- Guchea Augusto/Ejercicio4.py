print("Ingresa el numero de numeros que va a utilizar")
cantidad_de_numero = int(input())
vector = []
print("Ingresa los numeros")
for numero in range(cantidad_de_numero):
    vector.append(int(input()))
    print(vector)

def ordenamientoXseleccion(vector):
    for mym in range(len(vector)):
        minimo = mym
        for posicion in range(mym, len(vector)):
            if (vector[posicion] > vector[minimo]):
                minimo = posicion
        if (minimo != mym):
            auxiliar = vector[mym]
            vector[mym] = vector[minimo]
            vector[minimo] = auxiliar
    return vector

print(ordenamientoXseleccion(vector))
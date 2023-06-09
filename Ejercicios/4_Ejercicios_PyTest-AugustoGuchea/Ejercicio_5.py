def buscar_en_matriz(matriz, objetivo):
    if not matriz or not matriz[0]:
        return False

    filas = len(matriz)
    columnas = len(matriz[0])

    fila = 0
    columna = columnas - 1

    while fila < filas and columna >= 0:
        if matriz[fila][columna] == objetivo:
            return True
        elif matriz[fila][columna] < objetivo:
            fila += 1
        else:
            columna -= 1

    return False

from Ejercicio_5 import buscar_en_matriz

def test_buscar_en_matriz():
    matriz = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    assert buscar_en_matriz(matriz, 9) == True
    assert buscar_en_matriz(matriz, 8) == False
    assert buscar_en_matriz(matriz, 17) == True
    assert buscar_en_matriz(matriz, 20) == False

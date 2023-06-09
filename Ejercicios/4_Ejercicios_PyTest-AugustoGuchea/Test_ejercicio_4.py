from Ejercicio_4 import calcular_estadisticas

def test_calcular_estadisticas():
    numeros = [1, 2, 3, 4, 5]
    assert calcular_estadisticas(numeros) == (3.0, 1.5811388300841898)

import math

def calcular_estadisticas(numeros):
    media = sum(numeros) / len(numeros)
    suma_cuadrados = sum((x - media) ** 2 for x in numeros)
    desviacion_estandar = math.sqrt(suma_cuadrados / len(numeros))
    return media, desviacion_estandar

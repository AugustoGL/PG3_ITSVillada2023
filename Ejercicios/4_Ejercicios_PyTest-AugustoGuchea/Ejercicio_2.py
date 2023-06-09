def romano_a_decimal(numero_romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    previo = 0

    for caracter in reversed(numero_romano):
        valor = valores[caracter]

        if valor < previo:
            decimal -= valor
        else:
            decimal += valor

        previo = valor

    return decimal

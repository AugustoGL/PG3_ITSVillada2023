from Ejercicio_2 import romano_a_decimal

def test_romano_a_decimal():
    assert romano_a_decimal("IV") == 4
    assert romano_a_decimal("XL") == 40
    assert romano_a_decimal("XC") == 90
    assert romano_a_decimal("MMMCMXCIX") == 3999

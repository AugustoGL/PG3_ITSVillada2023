from Ejercicio_3 import es_anagrama

def test_es_anagrama():
    assert es_anagrama("roma", "amor") == True
    assert es_anagrama("casa", "saca") == False
    assert es_anagrama("anagrama", "managara") == True
    assert es_anagrama("hello", "world") == False

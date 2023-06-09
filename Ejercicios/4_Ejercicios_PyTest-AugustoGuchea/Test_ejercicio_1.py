from Ejercicio_1 import validar_contrasena

def test_validar_contrasena():
    assert validar_contrasena("Contraseña123") == True
    assert validar_contrasena("pass123") == False
    assert validar_contrasena("Contraseña") == False
    assert validar_contrasena("CONTRASEÑA123") == False
    assert validar_contrasena("Contraseña!") == False

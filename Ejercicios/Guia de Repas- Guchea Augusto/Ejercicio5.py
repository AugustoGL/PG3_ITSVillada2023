
palabra = input("Ingrese una palabra: ")
palabra1 = palabra[::-1]
if palabra == palabra1:
    print("La palabra es palindromo")
else:
    print("La palabra no es palindromo")
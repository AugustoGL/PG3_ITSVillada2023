def es_anagrama(palabra1, palabra2):
    palabra1 = palabra1.lower().replace(" ", "")
    palabra2 = palabra2.lower().replace(" ", "")

    return sorted(palabra1) == sorted(palabra2)

from io import open
def write():
    try:
        archivo = open("/Ejercicio_5.txt","w")
        archivo.write("Hola mundo")
        archivo.close()
    except:
        print("Error al abrir el archivo")
    else:
        print("Se ha escrito correctamente")
    finally:
        print("Fin de la ejecución")

write()
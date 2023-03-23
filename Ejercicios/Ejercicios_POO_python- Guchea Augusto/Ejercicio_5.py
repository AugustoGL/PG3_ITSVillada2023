class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def getNombre(self):
        return self.nombre
    
    def getEdad(self):
        return self.edad
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Edad: {self.edad}"
    

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
    
    def getSueldo(self):
        return self.sueldo
    
    def Impuestos(self):
        if self.sueldo > 3000:
            return print("Debe pagar impuestos")
        return print("No debe pagar impuestos")

    def __str__(self):
        return f"Nombre: {self.nombre} - Edad: {self.edad} - Sueldo: {self.sueldo}"
    
Persona = Persona("Juan", 25)
Empleado = Empleado("Pedro", 30, 4000)
print(Persona)
print(Empleado, Empleado.Impuestos())
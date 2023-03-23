
class Person:
    def __init__(self, name, nota):
        self.name = name
        self.nota = nota

    def getName(self):
        return self.name
    
    def getNota(self):
        return self.nota
    
    def AprobadoDesaprobado(self):
        if self.nota >= 6:
            return "Aprobado"
        else:
            return "Desaprobado"
    
    def toString(self):
        return "Mi nombre es", self.name, "y mi nota es", self.nota
    
juan = Person("Juan", 7)
print(juan.toString())
print(juan.AprobadoDesaprobado())
maria = Person("Maria", 5)
print(maria.toString())
print(maria.AprobadoDesaprobado())

        

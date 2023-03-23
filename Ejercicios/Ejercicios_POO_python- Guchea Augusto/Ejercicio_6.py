
class Family:
    def __init__(self, Papa, Mama, hijos):
        self.Papa = Papa
        self.Mama = Mama
        self.hijos = hijos

    def getNombre(self):
        return self.Papa, self.Mama, self.hijos
    
    def __str__(self):
        return f"Nombre del padre: {self.Papa} - Nombre de la madre: {self.Mama} - Hijos: {self.hijos[0]}, {self.hijos[1]}, {self.hijos[2]}"
    
family = Family("Juan", "Maria", ["Pedro", "Juana", "Jose"])
print(family)
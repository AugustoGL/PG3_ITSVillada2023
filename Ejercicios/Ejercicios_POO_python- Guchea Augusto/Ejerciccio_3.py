class Triangulo:
    def __init__(self, Lado1, Lado2, Lado3):
        self.Lado1 = Lado1
        self.Lado2 = Lado2
        self.Lado3 = Lado3
    
    def EsEquilatero(self):
        if self.Lado1 == self.Lado2 and self.Lado2 == self.Lado3:
            return "Es equilatero"
        else:
            return "No es equilatero"
        
    def LadoMasGrande(self):
        if self.Lado1 > self.Lado2 and self.Lado1 > self.Lado3:
            return self.Lado1
        elif self.Lado2 > self.Lado1 and self.Lado2 > self.Lado3:
            return self.Lado2
        else:
            return self.Lado3
        
Triangulo= Triangulo(3, 4, 3)
print(Triangulo.EsEquilatero())
print(Triangulo.LadoMasGrande())
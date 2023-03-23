class Operaciones:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        self.Suma()
        self.Resta()
        self.Multiplicacion()
        self.Division()


    def Suma(self):
        return print(self.numero1 + self.numero2)
    
    def Resta(self):
        return print(self.numero1 - self.numero2)
    
    def Multiplicacion(self):
        return print(self.numero1 * self.numero2)
    
    def Division(self):
        if self.numero2==0:
            return print("No se puede dividir por 0")
        return print(self.numero1 / self.numero2)
    
operacion = Operaciones(5, 5)

class Person:
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def toString(self):
        return "Mi nombre es", self.name

juan = Person("Juan")
print(juan.toString())
maria = Person("Maria")
print(maria.toString())

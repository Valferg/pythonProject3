#Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan puntos que definen sus esquinas.
#Agregue métodos a la clase Rectángulo para calcular su perímetro, calcular su área e indicar si el rectángulo es un cuadrado.

import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangulo:
    def __init__(self, esquina1, esquina2):
        self.esquina1 = esquina1
        self.esquina2 = esquina2

    def calcular_perimetro(self):
        base = (self.esquina1.x, self.esquina2.x)
        altura = (self.esquina1.y, self.esquina2.y)
        return 2 * (base + altura)

    def calcular_area(self):
        base = abs(self.esquina1.x - self.esquina2.x)
        altura = abs(self.esquina1.y - self.esquina2.y)
        return base * altura

    def Cuadrado(self):
        base = (self.esquina1.x, self.esquina2.x)
        altura = (self.esquina1.y, self.esquina2.y)
        return base == altura
esquina1 = Punto(2,5)
esquina2 = Punto(6,3)


rectangulo = Rectangulo(esquina1, esquina2)

print("El perimetro del rectangulo es", rectangulo.calcular_perimetro())
print("El area del rectangulo es", rectangulo.calcular_area())
if rectangulo.Cuadrado():
    print("El rectangulo es un cuadrado")
else:
    print("El rectangulo no es un cuadrado")
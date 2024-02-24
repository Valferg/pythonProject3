#- Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.

import math

class punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self):
        print("Las coordenadas del punto son", self.x, ",", self.y)

    def mover(self, mover_x, mover_y):
        self.x = mover_x
        self.y = mover_y

    def calcular_distancia(self, otro_punto):
        distancia = math.sqrt((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2)
        return distancia

punto1 = punto(3,4)
punto2 = punto(6,8)

punto1.mostrar()
punto2.mostrar()

print("Distancia entre los puntos:", punto1.calcular_distancia(punto2))

punto1.mover(1,2)
punto1.mostrar()
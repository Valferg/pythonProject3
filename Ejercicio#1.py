#Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.

class Vehiculo:
    def __init__(self):
        self.velocidad_maxima = float(input("Ingrese la velocidad máxima del vehículo "))
        self.kilometraje = float(input("Ingrese el kilometraje del vehículo "))

vehiculo = Vehículo()

print("Velocidad máxima del vehículo", vehiculo.velocidad_maxima)
print("Kilometraje del vehículo", vehiculo.kilometraje)

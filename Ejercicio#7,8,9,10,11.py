#7-Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta,
#propietarios y balance. Los tres atributos se deben inicializar en el constructor con valores
#recibidos como parámetros.
class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

# 8-Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta.
    def depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            print(f"Se han depositado {cantidad} en la cuenta")
        else:
            print("La cantidad a depositar debe ser mayor que cero")
#9-Para la clase CuentaBancaria, cree un método retirar que maneje las acciones de retiro de la cuenta.
    def retirar(self, cantidad):
        if 0 < cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Se han retirado {cantidad} de la cuenta.")
        else:
            print("Fondos insuficientes")

#10-Para la clase CuentaBancaria, cree un método aplicar_cuota_manejo que aplique un porcentaje del 2% sobre
#el balance de la cuenta
    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        print(f"Se ha aplicado la cuota de manejo del 2%")

#11-Para la clase CuentaBancaria, cree un método mostrar_detalles que imprima por consola los detalles de la
#cuenta bancaria.
    def mostrar_detalles(self):
        print("Los detalles de la cuenta son", "Numero de cuenta", self.numero_cuenta,
              "Propietarios", self.propietarios, "Balance", self.balance)

cuenta = CuentaBancaria("25689314", ["Lucia", "Roberto"], 1000.0)
print("El numero de cuenta es", cuenta.numero_cuenta)
print("Los propietarios son", cuenta.propietarios)
print("El balance es", cuenta.balance)

print("El balance inicial es", cuenta.balance)
cuenta.depositar(500.0)
print("El balance despues del deposito es", cuenta.balance)

cuenta.retirar(200.0)
print("Nuevo balance después del retiro:", cuenta.balance)

cuenta.aplicar_cuota_manejo()
print("El nuevo balance despues de aplicar la cuota de manejo es", cuenta.balance)

cuenta.mostrar_detalles()
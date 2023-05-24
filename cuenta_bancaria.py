import random
class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
    def __str__(self):
        return f"{self.nombre} {self.apellido} cuenta: {self.numero_cuenta} balance: {self.balance}"
    def depositar(self, monto):
        self.balance += monto
    def retirar(self, monto):
        if self.balance >= monto:
            self.balance -= monto
        else:
            print("Saldo insuficiente")
def init(cliente1):
    opcion = 0
    while opcion != 3:
        print('''Bienvenido al banco
        1. Depositar
        2. Retirar
        3. Salir''')
        opcion = int(input("Seleccione opción: "))
        if opcion == 1:
            monto = int(input("Seleccione cantidad a depositar: "))
            cliente1.depositar(monto)
            print(cliente1)
        if opcion == 2:
            monto = int(input("Seleccione cantidad a retirar: "))
            cliente1.retirar(monto)
            print(cliente1)
def crear_cliente():
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    numero_cuenta = str(random.randrange(10**9, 10**10))
    balance = 0
    cliente1 = Cliente(nombre, apellido, numero_cuenta, balance)
    init(cliente1)
crear_cliente()
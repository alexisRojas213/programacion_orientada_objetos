# Definición de la clase
class Persona:
    def __init__(self, nombre, edad):  # El método constructor siempre se llama __init__
        self.nombre = nombre           # Atributo nombre
        self.edad = edad               # Atributo edad

    def estudiar(self):  # Método de la clase
        print(f"Hola, mi nombre es {self.nombre} y estoy estudiando.")

    def cumplir_anios(self):  # Método de la clase
        self.edad += 1
        print(f"Esta persona cumplió: {self.edad} años")

# Crear objetos (instancias de la clase Persona)
estudiante1 = Persona("Danna", 19)
estudiante2 = Persona("Lucia", 18)

# Usar los métodos
estudiante1.estudiar()
estudiante1.cumplir_anios()
#instancias 
#cada objeto creado de una clase es una instancia podemos tener varias intancias que coexistan con sus propios datos
#objeto=instancia de la clase
#cada vez que se crea un objeto con  clase() se ibtiene una iinstancia depensiente 
#cada instancia tiene sus propios datos aunque venga de la misma clase

#ABSTRACCION
#epresentar solo lo importante en el mundo real ocultando detalles inecesarios

class automovil:                              
    def __init__(self,marca):
        self.marca= marca

    def arrancar(self):
        print(f"{self.marca} arranco")

#crear un objeto auto y asignar una marca

auto= automovil("nissan")
auto.arrancar()
#abstraccion: nos centramos solo en lo que importa (acicion) que es arrancar el automovil ocultando 
# derallees internos como motor, transmicion y tipo_combustible
#enfoque solo en la accion del objeto, 
#objetivo es hacer el codigo mas limpio y facil de usar

#practica 2 atributos publicos y privados

class Persona:
    def __init__(self, nombre, edad):  # constructor de la clase
        self.nombre = nombre
        self.edad = edad
        self.__cuenta = None

    def presentarse(self):
        print(f"{self.nombre} tiene {self.edad} años")
    
    def cumplir_anios(self):
        self.edad += 1
        print(f"{self.nombre} ahora tiene {self.edad} años")

    def asignar_cuenta(self, cuenta):
        self.__cuenta = cuenta
        print(f"{self.nombre} ha asignado una cuenta bancaria.")

    def consultar_saldo(self):
        if self.__cuenta:
            print(f"El saldo de la cuenta de {self.nombre} es: {self.__cuenta.saldo()}")
        else:
            print(f"{self.nombre} no tiene una cuenta bancaria asignada.")


class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo_inicial):
        self.numero_cuenta = numero_cuenta
        self.__saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Se han depositado {monto}. Nuevo saldo: {self.__saldo}")
        else:
            print("El monto a depositar debe ser positivo.")

    def retirar(self, monto):
        if monto > 0 and monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Se han retirado {monto}. Nuevo saldo: {self.__saldo}")
        else:
            print("Monto inválido o saldo insuficiente.")

    def saldo(self):
        return self.__saldo


# Ejemplo de uso
persona1 = Persona("Genesis", 18)
persona1.presentarse()
persona1.cumplir_anios()

cuenta1 = CuentaBancaria("123456789", 1000)
persona1.asignar_cuenta(cuenta1)

persona1.consultar_saldo()

cuenta1.depositar(200)
cuenta1.retirar(150)

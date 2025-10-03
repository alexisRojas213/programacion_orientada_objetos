#Patrón Factory
#Se usa para crear objetos sin exponer la lógica de instanciación al cliente.
#La idea es que el cliente (usuario del código) pide un objeto y el Factory decide qué tipo devolver.
#Útil cuando tienes muchas clases relacionadas y quieres centralizar la creación.
#Ejemplo real: un sistema bancario que crea cuentas (Ahorro, Nómina, Empresarial) según lo que el cliente solicita.



# Patrón Factory aplicado a cuentas bancarias

class Cuenta:
    """Clase base para las cuentas"""
    def __init__(self, titular):
        self.titular = titular

    def mostrar_info(self):
        pass


class CuentaAhorro(Cuenta):
    def mostrar_info(self):
        return f"Cuenta de Ahorro de {self.titular}"


class CuentaNomina(Cuenta):
    def mostrar_info(self):
        return f"Cuenta de Nómina de {self.titular}"


class CuentaEmpresarial(Cuenta):
    def mostrar_info(self):
        return f"Cuenta Empresarial de {self.titular}"


# ----------- FACTORY -----------
class CuentaFactory:
    """Factory que decide qué cuenta crear"""
    @staticmethod
    def crear_cuenta(tipo, titular):
        if tipo == "ahorro":
            return CuentaAhorro(titular)
        elif tipo == "nomina":
            return CuentaNomina(titular)
        elif tipo == "empresarial":
            return CuentaEmpresarial(titular)
        else:
            raise ValueError("Tipo de cuenta no válido")


# ----------- USO DEL FACTORY -----------
cuenta1 = CuentaFactory.crear_cuenta("ahorro", "Alexis")
cuenta2 = CuentaFactory.crear_cuenta("nomina", "Juan")
cuenta3 = CuentaFactory.crear_cuenta("empresarial", "Empresa XYZ")

print(cuenta1.mostrar_info())
print(cuenta2.mostrar_info())
print(cuenta3.mostrar_info())

#Patrón Observer
# Permite que un objeto (Sujeto) notifique automáticamente a muchos otros objetos (Observadores) cuando cambia su estado.
# Se usa mucho en sistemas de notificaciones, eventos, interfaces gráficas.
# Ejemplo real: un canal de YouTube (Sujeto) notifica a sus suscriptores (Observadores) cuando sube un nuevo video.



# Patrón Observer aplicado a notificaciones de un canal

# Sujeto (Canal)
class CanalYouTube:
    def __init__(self, nombre):
        self.nombre = nombre
        self.suscriptores = []  # lista de observadores

    def suscribir(self, usuario):
        self.suscriptores.append(usuario)

    def desuscribir(self, usuario):
        self.suscriptores.remove(usuario)

    def notificar(self, video):
        print(f"\n📢 Nuevo video en {self.nombre}: {video}")
        for sub in self.suscriptores:
            sub.actualizar(self.nombre, video)


# Observador (Suscriptor)
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, canal, video):
        print(f"{self.nombre} recibió notificación de {canal}: '{video}'")


# ----------- USO DEL OBSERVER -----------
canal = CanalYouTube("Canal de Programación")

u1 = Usuario("Ana")
u2 = Usuario("Luis")
u3 = Usuario("María")

# Los usuarios se suscriben
canal.suscribir(u1)
canal.suscribir(u2)
canal.suscribir(u3)

# El canal sube un video nuevo
canal.notificar("Patrón de diseño Observer en Python")

# Un usuario se desuscribe
canal.desuscribir(u2)

# El canal sube otro video
canal.notificar("Patrón Factory explicado con ejemplos")

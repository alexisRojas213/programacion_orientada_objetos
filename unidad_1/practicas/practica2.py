# -------------------------
# Ejemplo de Singleton: Logger
# -------------------------
class Logger:
    _instancia = None  # atributo de clase para almacenar la única instancia

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.archivo = open("app.log", "a")
        return cls._instancia

    def log(self, mensaje):
        self.archivo.write(mensaje + "\n")  # guardamos con salto de línea
        self.archivo.flush()


# Uso de Logger
logger1 = Logger()
logger2 = Logger()

logger1.log("Inicio de sesión en la aplicación")
logger2.log("El usuario se autenticó")

print(logger1 is logger2)  # True, son el mismo objeto


# -------------------------
# Ejemplo de Singleton: Presidente
# -------------------------
class Presidente:
    _instancia = None  # definimos antes de __new__

    def __new__(cls, nombre):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.nombre = nombre
            cls._instancia.historial = []
        return cls._instancia

    def accion(self, accion):
        evento = f"{self.nombre} {accion}"
        self.historial.append(evento)
        print(evento)


# Uso de Presidente
p1 = Presidente("AMLO")
p2 = Presidente("Peña Nieto")
p3 = Presidente("Fox")

p1.accion("firmó decreto")
p2.accion("visitó España")
p3.accion("aprobó un decreto")

print(p1 is p2, p2 is p3)  # True True, todos son el mismo objeto
print(p1.historial)        # Se ven todas las acciones registradas

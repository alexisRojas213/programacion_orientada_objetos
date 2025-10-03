#actividad de la practica

class presidente:
    _instancia = None
    def __new__(cls, nombre):
        if cls._instancia is None:
           cls._instancia = super().__new__(cls)
           cls._instancia.nombre= nombre
           cls._instancia.historial = []
        return cls._instancia
    
    
    def accion (self,accion):
        evento = f"{self.nombre} {accion}"
        self.historial.append(evento)
        print(evento)


p1= presidente ("amlo")
p2= presidente ("peña nieto")
p3= presidente ("fox")

p1.accion("firmo decreto")          
p2.accion("visito españa")   
p3.accion("aprobo un decreto")           
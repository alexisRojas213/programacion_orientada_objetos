import os
os.system('cls')

class Ticket:
    def __init__(self, id, tipo, prioridad, estado="pendiente"):
        self.id = id
        self.tipo = tipo
        self.prioridad = prioridad
        self.estado = estado

    def ticket_imp(self):
        return (
            "----------------------------------\n"
            f"        TICKET #{self.id}\n"
            "----------------------------------\n"
            f"Tipo      : {self.tipo}\n"
            f"Prioridad : {self.prioridad}\n"
            f"Estado    : {self.estado}\n"
            "----------------------------------"
        )

ticket1 = Ticket(1, "software", "alta")
ticket2 = Ticket(2, "prueba", "media")

print(ticket1.ticket_imp())
print(ticket2.ticket_imp())

class Empleado:
    def __init__(self, nombre, puesto):
        self.nombre = nombre
        self.puesto = puesto

    def trabajar_en_ticket(self, ticket):
        print(f"El empleado {self.nombre} revisa el ticket {ticket.id}")

empleado1 = Empleado("Juan", "Soporte")
empleado1.trabajar_en_ticket(ticket1)

class Desarrollador(Empleado):
    def trabajar_en_ticket(self, ticket):
        if ticket.tipo == "software":
            ticket.estado = "resuelto"
            print(f"El desarrollador {self.nombre} ha resuelto el ticket {ticket.id}")
        else:
            print(f"El desarrollador {self.nombre} no puede resolver el ticket {ticket.id} de tipo {ticket.tipo}")

empleado1 = Desarrollador("Ana", "Sofware")
empleado1.trabajar_en_ticket(ticket1) 

class Tester(Empleado):
    def trabajar_en_ticket(self, ticket):
        if ticket.tipo == "prueba":
            ticket.estado = "resuelto"
            print(f"El tester {self.nombre} ha resuelto el ticket {ticket.id}")
        else:
            print(f"El tester {self.nombre} no puede resolver el ticket {ticket.id} de tipo {ticket.tipo}")
empleado1 = Desarrollador("Ane", "Prueba")
empleado1.trabajar_en_ticket(ticket1) 

print("-----Asignación de tickets-----")
class ProjectManager(Empleado):
    def asignar_ticket(self, ticket, empleado):
        print(f"El Project Manager {self.nombre} asigna el ticket {ticket.id} al empleado {empleado.nombre}")
        empleado.trabajar_en_ticket(ticket)
pm1 = ProjectManager("Carlos", "PM")
pm1.asignar_ticket(ticket1, empleado1)  # Asignar a Desarrollador
pm1.asignar_ticket(ticket2, empleado1)  # Asignar a Desarrollador (no puede resolver)
tester1 = Tester("Luis", "Tester")
pm1.asignar_ticket(ticket2, tester1)  # Asignar a Tester
pm1.asignar_ticket(ticket1, tester1)  # Asignar a Tester (no puede resolver)

#Crear tickets y empleados (Instancias de objetos)
ticket1 = Ticket(1, "software", "alta")
ticket2 = Ticket(2, "prueba", "media")
developer1 = Desarrollador("Gustavo", "Software")
tester1 = Tester("Pablo", "Tester")
pm1 = ProjectManager("Susana", "PM")
pm1.asignar_ticket(ticket1, developer1)


# Parte adicional
# Agregar un menú con while y con if que permita:
#1. Crear un ticket
#2. Ver tickets
#3. Asignar tickets
#4. Salir del programa
os.system('cls')
def main():
    tickets = []
    empleados = []
    ticket_id = 1
    resp=True

    while resp:
        os.system('cls')
        print("\n--- Menú de Gestión de Tickets ---")
        print("1. Crear un ticket")
        print("2. Ver tickets")
        print("3. Registrar empleado")
        print("4. Asignar tickets")
        print("5. Salir del programa")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            os.system('cls')
            tipo = input("Ingrese el tipo de ticket (software/prueba): ")
            prioridad = input("Ingrese la prioridad del ticket (alta/media/baja): ")
            ticket = Ticket(ticket_id, tipo, prioridad)
            tickets.append(ticket)
            print(f"Ticket #{ticket_id} creado.")
            ticket_id += 1
            input("Presione Enter para continuar...")

        elif choice == '2':
            os.system('cls')
            if not tickets:
                print("No hay tickets disponibles.")
            else:
                for ticket in tickets:
                    print(ticket.ticket_imp())
            input("Presione Enter para continuar...")

        elif choice == '3':
            os.system('cls')
            print("Tipos de empleado: 1. Desarrollador  2. Tester  3. ProjectManager")
            tipo_emp = input("Seleccione el tipo de empleado (1/2/3): ")
            nombre = input("Ingrese el nombre del empleado: ")
            puesto = input("Ingrese el puesto del empleado: ")
            if tipo_emp == '1':
                empleados.append(Desarrollador(nombre, puesto))
            elif tipo_emp == '2':
                empleados.append(Tester(nombre, puesto))
            elif tipo_emp == '3':
                empleados.append(ProjectManager(nombre, puesto))
            else:
                print("Tipo de empleado no válido.")
            print(f"Empleado {nombre} registrado.")
            input("Presione Enter para continuar...")

        elif choice == '4':
            os.system('cls')
            if not tickets:
                print("No hay tickets para asignar.")
                input("Presione Enter para continuar...")
            elif not empleados:
                print("No hay empleados registrados.")
                input("Presione Enter para continuar...")
            else:
                for ticket in tickets:
                    if ticket.estado == "pendiente":
                        print(ticket.ticket_imp())
                        print("Empleados disponibles:")
                        for idx, emp in enumerate(empleados):
                            print(f"{idx+1}. {emp.nombre} ({emp.puesto})")
                        try:
                            emp_idx = int(input("Seleccione el número del empleado para asignar el ticket: ")) - 1
                            if 0 <= emp_idx < len(empleados):
                                empleado = empleados[emp_idx]
                                pm = next((e for e in empleados if isinstance(e, ProjectManager)), None)
                                if pm:
                                    pm.asignar_ticket(ticket, empleado)
                                else:
                                    print("No hay Project Manager registrado para asignar tickets.")
                            else:
                                print("Selección inválida.")
                        except ValueError:
                            print("Entrada inválida.")
                input("Presione Enter para continuar...")

        elif choice == '5':
            print("Saliendo del programa...")
            resp=False
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "_main_":
    main()


         
   
    





    

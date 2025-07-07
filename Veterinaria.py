class Mascota:
    def __init__(self, nombre, especie, raza, edad):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, value):
        if 0 <= value <= 20:
            self.__edad = value
        else:
            raise ValueError("ERROR: Edad no válida.")
    def mostrar_info_mascota(self):
        print(f"\tNombre: {self.nombre}, especie: {self.especie}, raza: {self.raza}, edad: {self.__edad}")

class Cliente:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.mascotas = []
    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)
    def mostrar_info_cliente(self):
        print(f"\nNombre: {self.nombre}, teléfono: {self.telefono}, correo: {self.correo}")
        if self.mascotas:
            print("Mascotas:")
            for i in self.mascotas:
                i.mostrar_info_mascota()
        else:
            print("No se han registrado mascotas con su nombre")

class CitaMedica:
    def __init__(self, motivo, mascota, diagnostico):
        self.motivo = motivo
        self.mascota = mascota
        self.diagnostico = diagnostico
    def mostrar_visita(self):
        print(f"Mascota atendida: {self.mascota.nombre}, motivo de consulta: {self.motivo}, diagnóstico: {self.diagnostico}")

#Inicio de programa principal:
print("INICIAR SESIÓN:")
while True:
    usuario = input("Ingrese el usuario: ")
    password = input("Ingrese la contraseña: ")
    if usuario == "admin" and password == "admin":
        opcion = "0"
        lista_clientes = []
        lista_mascotas = []
        historial_citas = []
        while opcion != "6":
            print("==SISTEMA VETERINARIA==")
            print("1.Registrar cliente")
            print("2.Registrar mascota")
            print("3.Registrar cita médica")
            print("4.Ver historial de citas")
            print("5.Ver clientes y mascotas")
            print("6.Salir")
            try:
                opcion = input("\nSeleccione una opción: ")
                match opcion:
                    case "1":
                        nombre_cliente = input("Nombre: ")
                        telefono = input("Número de telefono: ")
                        correo = input("Correo: ")
                        nuevo_cliente = Cliente(nombre_cliente, telefono, correo)
                        lista_clientes.append(nuevo_cliente)
                        print("Se ha completado el registro")
                    case "2":
                        if lista_clientes:
                            nombre_mascota = input("Nombre de la mascota: ")
                            especie = input("Especie: ")
                            raza = input("Raza: ")
                            edad = int(input("Edad: "))
                            nueva_mascota = Mascota(nombre_mascota, especie, raza, edad)
                            repetir = True
                            while repetir:
                                owner = input("Nombre del dueño: ")
                                for i in lista_clientes:
                                    if i.nombre.lower() == owner.lower():
                                        i.agregar_mascota(nueva_mascota)
                                        repetir = False
                                if repetir:
                                    print("No se encontre un cliente con el nombre registrado, revise y vuelva a intentarlo.")
                            lista_mascotas.append(nueva_mascota)
                            print("Se ha completado el registro")
                        else:
                            print("Debe registrar clientes antes de registrar mascotas.")
                    case "3":
                        if not lista_mascotas:
                            print("No hay mascotas registradas")
                            continue
                        while True:
                            nombre = input("Nombre de la mascota: ")
                            mascota = next((i for i in lista_mascotas if i.nombre == nombre), None)
                            if mascota is None:
                                print("No se encontro alguna mascota con ese nombre, verifique y vuelva a intentar.")
                                continue
                            break
                        motivo = input("Motivo de la cita: ")
                        diagnostico = input("Diagnostico inicial: ")
                        registrar_cita = CitaMedica(motivo, mascota, diagnostico)
                        historial_citas.append(registrar_cita)
                        print("Cita registrada")
                    case "4":
                        if not historial_citas:
                            print("No se ha registrado ninguna cita.")
                            continue
                        for item in historial_citas:
                            item.mostrar_visita()
                    case "5":
                        if not lista_clientes:
                            print("No se han registrado clientes ni mascotas")
                            continue
                        for item in lista_clientes:
                            item.mostrar_info_cliente()
                    case "6":
                        print("¡Hasta luego!")
                    case __:
                        print(f"La opción {opcion} no está diponible")

            except ValueError:
                print("ERROR: Ha ingresado un dato no válido")
            if opcion != "6":
                input("Presione ENTER para continuar")
    else:
        print("Credenciales no válidas vuelva a intentar.")
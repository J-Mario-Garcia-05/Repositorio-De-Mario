class Mascota:
    def __init__(self, nombre, especie, raza, edad):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.__edad = edad
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad):
        if 0 <= edad <= 12:
            self.edad = edad
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

print("INICIAR SESIÓN:")
while True:
    usuario = input("Ingrese el usuario: ")
    password = input("Ingrese la contraseña: ")
    if usuario == "admin" and password == "admin":
        opcion = "0"
        lista_clientes = []
        while opcion != "6":
            print("==SISTEMA VETERINARIA==")
            print("1.Registrar cliente")
            print("2.Registrar mascota")
            print("3.Agendar cita médica")
            print("4.Ver historial de citas")
            print("5.Ver clientes y mascotas")
            print("6.Salir")
            try:
                opcion = input("\nSeleccione una opción: ")
                match opcion:
                    case "1":
                        nombre_cliente = input("Ingrese el nombre: ")
                        telefono = int(input("Ingrese un número de telefono: "))
                        correo = input("Ingrese un correo: ")
                        nuevo_cliente = Cliente(nombre_cliente, telefono, correo)
                        lista_clientes.append(nuevo_cliente)
                        print("Se ha completado el registro")
                    case "2":
                        nombre_mascota = input("Ingrese el nombre de la mascota: ")
                        especie = input("Ingrese la especie: ")
                        raza = input("Ingrese la raza: ")
                        edad = int(input("Ingrese la edad: "))
                        nueva_masota = Mascota(nombre_mascota, especie, raza, edad)
                        print("Se ha completado el registro")
            except ValueError:
                print("ERROR: Ha ingresado un dato no válido")
    else:
        print("Credenciales no válidas vuelva a intentar.")
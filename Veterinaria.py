class Cliente:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.mascotas = []
    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)
    def mostrar_informacion(self):
        print(f"\nNombre: {self.nombre}, teléfono: {self.telefono}, correo: {self.correo}")
        if self.mascotas:
            print("Mascotas:")
            for i in self.mascotas:
                i.mostrar_informacion()

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
    def mostrar_informacion(self):
        print(f"\tNombre: {self.nombre}, especie: {self.especie}, raza: {self.raza}, edad: {self.__edad}")


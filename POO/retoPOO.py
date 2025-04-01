from datetime import datetime

class Auto:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = 0 

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, Kilometraje: {self.kilometraje} km")

    def actualizar_kilometraje(self, kilometraje):
        if kilometraje >= self.kilometraje:
            self.kilometraje = kilometraje
            print(f"El kilometraje ha sido actualizado a {self.kilometraje} km.")
        else:
            print("No se puede reducir el kilometraje.")

    def realizar_viaje(self, kilometros):
        if kilometros > 0:
            self.kilometraje += kilometros
            print(f"Se ha realizado un viaje de {kilometros} km. Kilometraje actual: {self.kilometraje} km.")
        else:
            print("La cantidad de kilómetros debe ser positiva.")

    def estado_auto(self):
        if self.kilometraje < 20000:
            print("Estoy como nuevo")
        elif 20000 <= self.kilometraje <= 100000:
            print("Ya estoy usado")
        else:
            print("¡Ya déjame descansar por favor!")

    @classmethod
    def auto_nuevo(cls):
        anio_actual = datetime.now().year
        return cls("Toyota", "Modelo genérico", anio_actual)

    @staticmethod
    def validar_kilometraje(auto1, auto2):
        """Verifica si dos autos tienen el mismo kilometraje."""
        return auto1.kilometraje == auto2.kilometraje

    @staticmethod
    def descripcion_auto(auto):
        print(f"El auto {auto.marca} modelo {auto.modelo} del año {auto.anio} tiene {auto.kilometraje} km.")

    @classmethod
    def auto_personalizado(cls, marca, modelo):
        anio_actual = datetime.now().year
        return cls(marca, modelo, anio_actual)

auto1 = Auto("Honda", "Civic", 2018)
auto2 = Auto.auto_nuevo()
auto3 = Auto.auto_personalizado("Ford", "Mustang")

auto1.actualizar_kilometraje(25000)
auto2.realizar_viaje(5000)

print(f"¿Auto1 y Auto2 tienen el mismo kilometraje? {Auto.validar_kilometraje(auto1, auto2)}")

auto1.estado_auto()
auto2.estado_auto()
auto3.estado_auto()

Auto.descripcion_auto(auto1)
Auto.descripcion_auto(auto2)
Auto.descripcion_auto(auto3)
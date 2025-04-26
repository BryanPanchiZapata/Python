class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def descripcion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}"
    
class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio, num_puertas):
        super().__init__(marca, modelo, anio)
        self.num_puertas = num_puertas

    def descripcion(self):
        return f"{super().descripcion()}, Número de Puertas: {self.num_puertas}"

class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, tipo):
        super().__init__(marca, modelo, anio)
        self.tipo = tipo

    def descripcion(self):
        return f"{super().descripcion()}, Tipo: {self.tipo}"
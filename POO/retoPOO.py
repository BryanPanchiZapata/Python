class Auto:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = 0  

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}")

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


mi_auto = Auto("Audi", "Serie 4", 2022)

mi_auto.mostrar_informacion()          
mi_auto.actualizar_kilometraje(50000)  
mi_auto.realizar_viaje(5000)           
mi_auto.estado_auto()                  
mi_auto.actualizar_kilometraje(10000)  
mi_auto.realizar_viaje(-100)          
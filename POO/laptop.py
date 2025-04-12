import random
class laptop:
    def __init__(self, marca, procesador, memoria, costo=500, impuesto=10):
        self.marca = marca
        self.procesador = procesador
        self.memoria = memoria
        self.costo = costo
        self.impuesto = impuesto
    
    def precio_final(self):
        return self.costo + self.impuesto
    
    def valor_descuento(self, porcentaje):
        return (self.costo * porcentaje / 100)
    
    def realizar_diagnostico_sistema(self):
        resultado = {
            "Marca": f"{self.marca}",
            "Procesador": f"{self.procesador}",
            "Memoria RAM": "OK" if self.memoria >= 8 else "Aumentar memoria",
            "Bateria": "OK" if random.choice([True, False]) else "Cambiar bateria",
        }
        return resultado

    @staticmethod
    def comparar_costo(laptop1, laptop2):
        if laptop1.costo < laptop2.costo:
            return f"La laptop {laptop1.marca} tiene un costo menor que la laptop {laptop2.marca}"
        elif laptop1.costo > laptop2.costo:
            return f"La laptop {laptop1.marca} tiene un costo mayor que la laptop {laptop2.marca}"
        else:
            return f"Las laptops {laptop1.marca} y {laptop2.marca} tienen el mismo costo"
        

    @classmethod
    def asus_laptop(cls, costo):
        marca = "Asus"
        procesador = "i5"
        memoria = 16
        return cls(marca, procesador, memoria, costo )
import random
from laptop import laptop

class Laptop_Business(laptop):
    def __init__(self, marca, procesador, memoria, almacenamiento, duracion_bateria, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.almacenamiento = almacenamiento  
        self.duracion_bateria = duracion_bateria  

    def realizar_diagnostico_sistema(self):
        resultado_diagnostico = super().realizar_diagnostico_sistema()
        
        resultado_diagnostico["Almacenamiento"] = "OK" if self.almacenamiento >= 512 else "Espacio insuficiente"
        resultado_diagnostico["Duración de Batería"] = "OK" if self.duracion_bateria >= 6 else "Considerar cambiar batería"

        resultado_conectividad = self.verificar_conectividad_red()
        resultado_diagnostico["Conectividad de Red"] = resultado_conectividad

        return resultado_diagnostico

    def verificar_conectividad_red(self):
        conectividad = {
            "Wi-Fi Disponible": random.choice([True, False]),
            "Acceso a Servidores Empresariales": random.choice([True, False]),
            "Latencia de Red Aceptable": random.choice([True, False])
        }
        return conectividad

laptop_empresa = Laptop_Business("Dell", "i7", 16, 1000, 8)
print(laptop_empresa.realizar_diagnostico_sistema())
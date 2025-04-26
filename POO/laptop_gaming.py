from laptop import laptop

class laptop_gaming(laptop):
    def __init__ (self, marca, procesador,tarjeta_grafica, memoria, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.tarjeta_grafica = tarjeta_grafica

    def __str__(self):
        return f"Marca: {self.marca}\n Procesador: {self.procesador}\n Memoria: {self.memoria}\n Tarjeta Gráfica: {self.tarjeta_grafica}\n Costo: {self.costo} Impuesto: {self.impuesto}"
    def realizar_diagnostico_sistema(self):
        resultado_diagnostico = super().realizar_diagnostico_sistema()
        resultado_juegos = self.realizar_diagnostico_juegos()
        resultado_diagnostico["Resultado Juegos"] = resultado_juegos
        return resultado_diagnostico
    
    def realizar_diagnostico_juegos(self):
        juegos=["League of Legends", "Dota 2", "Counter-Strike", "Valorant"]
        resultados = {}
        for juego in juegos:
            fps_base = 30
            if "RTX" in self.tarjeta_grafica:
                fps = fps_base * 3
            elif "GTX" in self.tarjeta_grafica:
                fps = fps_base * 2
            else:
                fps = fps_base
            
            resultados  [juego] = f"{fps} FPS"
        return resultados

    def realizar_informe_uso(self):
        informe = super().realizar_informe_uso()
        informe.update({
            "Tipo": "Gaming",
            "Uso Recomendado": "Juegos",
            "Uso de Hora": "4 horas",
            "Recomendacion": ["Antivirus", "Limpiar el disco duro", "Actualizar drivers"],
            
        
        })
        return informe
    pass
        
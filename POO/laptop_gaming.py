from laptop import laptop

class laptop_gaming(laptop):
    def __init__ (self, marca, procesador,tarjeta_grafica, memoria, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.tarjeta_grafica = tarjeta_grafica

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


        
        
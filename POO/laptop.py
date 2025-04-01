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

laptop_pepito = laptop("Dell", "i7", 16)

print(laptop_pepito.__dict__)
print(laptop_pepito.precio_final())
print(f"El valor de descuento es: {laptop_pepito.valor_descuento(10)}")


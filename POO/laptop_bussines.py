from laptop import laptop

class LaptopBusiness(laptop):
    def __init__(self, marca, procesador, memoria, software_empresarial, seguridad, costo=1000, impuesto=12):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.software_empresarial = software_empresarial
        self.seguridad = seguridad

    def __str__(self):
        return f"Marca: {self.marca}\n Procesador: {self.procesador}\n Memoria: {self.memoria}\n Software Empresarial: {self.software_empresarial}\n Seguridad: {self.seguridad}\n Costo: {self.costo} Impuesto: {self.impuesto}"
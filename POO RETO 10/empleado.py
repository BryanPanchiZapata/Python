from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    @abstractmethod
    def calcular_salario(self):
        pass

class EmpleadoTiempoCompleto(Empleado):
    def calcular_salario(self):
      
        return self.salario_base * 1.2

class EmpleadoMedioTiempo(Empleado):
    def calcular_salario(self):
       
        return self.salario_base * 1.1
from empleado import EmpleadoTiempoCompleto, EmpleadoMedioTiempo


empleado1 = EmpleadoTiempoCompleto("Juan Pérez", 2000)
empleado2 = EmpleadoMedioTiempo("Ana Gómez", 1000)


print(f"Empleado: {empleado1.nombre}, Salario Final: ${empleado1.calcular_salario():.2f}")
print(f"Empleado: {empleado2.nombre}, Salario Final: ${empleado2.calcular_salario():.2f}")


empleados = [empleado1, empleado2]
print("\nSalarios de todos los empleados:")
for empleado in empleados:
    print(f"Empleado: {empleado.nombre}, Salario Final: ${empleado.calcular_salario():.2f}")
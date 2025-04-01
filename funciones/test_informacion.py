from informacion import agregar_nombre, agregar_edad, nombre_paciente, edad

año_actual = 2025  


pacientes = [
    "Antonio Moreno 2000",
    "Carmen Díaz 2001",
    "Fernando García 2003",
    "Teresa Rodríguez 2004",
    "José López 2005",
    "Miguel Ángel Ortiz 1999",
    "Lucia Gómez 2000",
    "Francisco Javier Sánchez 2001",
    "Beatriz Domínguez 2002",
    "Adrián López 2011",
    "Martina Pascual 2012",
    "Álvaro Torres 2013",
    "Berta Romero 2014"
]


for paciente in pacientes:
    agregar_nombre(paciente) 
    agregar_edad(paciente, año_actual)  

print(f"Lista de nombres: {nombre_paciente}")


print(f"Lista de edades: {edad}")


mayor_edad = max(edad) 
indice_mayor = edad.index(mayor_edad) 
paciente_mayor = nombre_paciente[indice_mayor]

menor_edad = min(edad)  
indice_menor = edad.index(menor_edad) 
paciente_menor = nombre_paciente[indice_menor]

print(f"El paciente mayor es {paciente_mayor} con la edad de {mayor_edad} años.")
print(f"El paciente menor es {paciente_menor} con la edad de {menor_edad} años.")
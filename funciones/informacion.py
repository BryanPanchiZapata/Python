nombre_paciente = []

edad = []

def agregar_nombre(informacion):
    nombre_paciente.append(informacion.split(" ")[0] + " " + informacion.split(" ")[1])

def agregar_edad(informacion, año_actual):
    año_nacimiento = int(informacion.split(" ")[-1])
    edad.append(año_actual - año_nacimiento)

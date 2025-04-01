def datos(nombre, apellido, edad, mensaje="excelente"):
    if edad >= 18:
        print(f"{nombre} {apellido} es mayor de edad y {mensaje}")
    else:
        print(f"{nombre} {apellido} es menor de edad y {mensaje}")
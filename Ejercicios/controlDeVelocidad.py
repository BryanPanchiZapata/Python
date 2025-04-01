pais = input("Ingrese el país a viajar: ").capitalize()
zona = input("Ingrese la zona a viajar: ").lower()

a = "Colombia"
b = "Perú"
c = "Ecuador"
limites ={
    "Colombia": {
        "urbana": (10, 30),
        "rural": (31, 80),
        "perimetral": (81, 100)

    },
    "Perú":{
        "urbana": (10, 40),
        "rural": (41, 60),
        "perimetral": (61, 120)
    },
    "Ecuador": {
        "urbana": (10, 50),
        "rural": (51, 570),
        "perimetral": (71, 90)
    }
}
velocidad = int(input("Ingrese la velocidad del conductor (en Km/h): "))

if pais in limites:
    if zona in limites[pais]:
        velocidad_minima, velocidad_maxima = limites[pais][zona]
        if velocidad < velocidad_minima:
            print(f"La velocidad {velocidad} Km/h es demasiado baja para la zona {zona} en {pais}. Mínimo permitido: {velocidad_minima} Km/h.")
        elif velocidad > velocidad_maxima:
            print(f"La velocidad {velocidad} Km/h excede el límite para la zona {zona} en {pais}. Máximo permitido: {velocidad_maxima} Km/h.")
        else:
            print(f"La velocidad {velocidad} Km/h está dentro del rango permitido en la zona {zona} en {pais}.")
    else:
        print("La zona ingresada no es válida. Por favor, intente con 'urbana', 'rural' o 'perimetral'.")
else:
    print("El país ingresado no es válido. Por favor, elija entre 'Ecuador', 'Colombia' o 'Perú'.")



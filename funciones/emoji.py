def encontrar_palabra(frase):
    if "feliz" in frase:
        print(f"El emoji que te representa es: \U0001F600")
    elif "triste" in frase:
        print(f"El emoji que te representa es: \U0001F929")
    else:
        print(f"No se encontró un emoji en la frase.")

lista = []
def agregar_frase(frase):
    lista.append(frase)
    print(f"Frase agregada: {lista}")
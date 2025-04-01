import emoji

cantidad_frase = int(input("¿Cuántas frases quieres ingresar? "))
for i in range(cantidad_frase):
    frase = input(f"Ingrese la frase {i + 1}: ")
    emoji.encontrar_palabra(frase)
    emoji.agregar_frase(frase)
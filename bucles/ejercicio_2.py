frase = input("ingrese una frase: ")
letra = input("ingrese una letra: ")

contador = 0
for i in frase:
    if i == letra:
        contador += 1
print(f"la letra {letra} se encuentra {contador} veces en la frase")


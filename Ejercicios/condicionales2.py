import random

aleatorio=random.randint(1, 9)
aleatorio2=random.randint(1, 9)

if aleatorio == 4:
    print("Ganaste un iphone")
elif aleatorio == 8:
    print("Ganaste un balón")
elif aleatorio == 3 and aleatorio2 == 7:
    print("Ganaste un carro")
else:
    print("No ganaste nada")
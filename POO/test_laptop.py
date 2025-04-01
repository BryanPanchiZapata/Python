from laptop import laptop
laptop_pepito = laptop("Dell", "i7", 16)
laptop_juanito = laptop("HP", "i5", 8, 600)

for i in range(1, 1000):
    asus_laptop = laptop.asus_laptop(i)
    print(asus_laptop.__dict__)


# print(laptop.comparar_costo(laptop_pepito, laptop_juanito))
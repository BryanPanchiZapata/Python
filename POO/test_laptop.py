from laptop import laptop
from laptop_gaming import laptop_gaming
from laptop_business import Laptop_Business

laptop_pepito = laptop_gaming("Dell", "i7", "NVIDIA GTX 3080", 16)

laptop_juanito = laptop("HP", "i5", 8, 600)

# for i in range(1, 1000):
#     asus_laptop = laptop.asus_laptop(i)
#     print(asus_laptop.__dict__)


# print(laptop.comparar_costo(laptop_pepito, laptop_juanito))

# laptop_marquitos = laptop_gaming("Lenovo", "i7", "RTX 3060", 16)
# print(laptop_marquitos.realizar_diagnostico_sistema())

# laptop_empresa = Laptop_Business("HP", "i5", 16, 512, 7)
# print(laptop_empresa.realizar_diagnostico_sistema())


def imprimir_informe(laptop):
    informe = laptop.realizar_informe_uso()
    for clave, valor in informe.items():
        print(f"{clave}: {valor}")
    print("\n")


print("Informe de Laptop Pepito:")
imprimir_informe(laptop_pepito)
print("Informe de Laptop Juanito:")
imprimir_informe(laptop_juanito)

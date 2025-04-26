from vehiculo import  Auto, Moto


auto = Auto("Toyota", "Corolla", 2021, 4)
moto = Moto("Yamaha", "R1", 2022, "Deportiva")


print(auto.descripcion())
print(moto.descripcion())


vehiculos = [auto, moto]
for vehiculo in vehiculos:
    print(vehiculo.descripcion())
#listas

planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Urano", "Neptuno"]
#print(planetas[-2])

#print(planetas[2:])

#print(len(planetas))

#Trabajar con una lista de números

gravedad_planetas = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
peso_bus = 124054 #Newtons en la tierra

print(f"En la tierra, un autobus de 2 pisos pesa {peso_bus} Newtons")
print (f"En mercurio un autobus de 2 pisos pesa {peso_bus * gravedad_planetas[0]} Newtons")

print(f"Lo mas liviano que seria un autobus en el sistema solar es {peso_bus * min(gravedad_planetas)} Newtons")
print(f"Lo mas pesado que seria un autobus en el sistema solar es {peso_bus * max(gravedad_planetas)} Newtons")
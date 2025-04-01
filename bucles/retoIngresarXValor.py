
datos = []  


cantidad = int(input("¿Cuántos datos desea ingresar? "))  


for i in range(cantidad):
    dato = input(f"Ingrese el dato #{i + 1}: ")
    
    if dato.isdigit():  
        datos.append(int(dato))
    elif '.' in dato and dato.replace('.', '', 1).isdigit():  
        datos.append(float(dato)) 
    
    else:  
        datos.append(dato) 


print(f"Su lista es: {datos}")
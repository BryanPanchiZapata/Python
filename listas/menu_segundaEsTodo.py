menu = []

while True:
    print("\nMenú del restaurante Segunda es Todo:")
    print("1. Añadir plato al menú")
    print("2. Buscar en el menú")
    print("3. Eliminar plato del menú")
    print("4. Mostrar platos del menú")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        plato = input("Ingrese el nombre del plato: ")
        menu.append(plato)
        print(f"Plato '{plato}' añadido al menú.")
    
    elif opcion == "2":
        plato = input("Ingrese el nombre del plato a buscar: ")
        if plato in menu:
            print(f"El plato '{plato}' está en el menú.")
        else:
            print(f"El plato '{plato}' no está en el menú.")
    
    elif opcion == "3":
        plato = input("Ingrese el nombre del plato a eliminar: ")
        if plato in menu:
            menu.remove(plato)
            print(f"Plato '{plato}' eliminado del menú.")
        else:
            print(f"El plato '{plato}' no se encuentra en el menú.")
    
    elif opcion == "4":
        if menu:
            print("Platos en el menú:")
            for p in menu:
                print(f"- {p}")
        else:
            print("El menú está vacío.")
    
    elif opcion == "5":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    
    else:
        print("Opción no válida. Intente de nuevo.")
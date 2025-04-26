from libro import Libro

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 417)
libro2 = Libro("El principito", "Antoine de Saint-Exupéry", 96)
libro3 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863)

print(libro1.mostrar_info())
print(libro2.mostrar_info())
print(libro3.mostrar_info())


print(f"¿El libro '{libro1.titulo}' es grande? {'Sí' if Libro.es_grande(libro1.paginas) else 'No'}")
print(f"¿El libro '{libro2.titulo}' es grande? {'Sí' if Libro.es_grande(libro2.paginas) else 'No'}")
print(f"¿El libro '{libro3.titulo}' es grande? {'Sí' if Libro.es_grande(libro3.paginas) else 'No'}")


print(f"Total de libros creados: {Libro.total_libros()}")
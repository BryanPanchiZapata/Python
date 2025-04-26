class Libro:

    contador_libros = 0

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        Libro.contador_libros += 1


    def mostrar_info(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Páginas: {self.paginas}"


    @staticmethod
    def es_grande(paginas):
        return paginas > 300


    @classmethod
    def total_libros(cls):
        return cls.contador_libros
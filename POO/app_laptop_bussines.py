from laptop_gaming import laptop_gaming
from laptop_bussines import LaptopBusiness
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

class App:
    def __init__(self, root):
        self.root = root
        self.laptops = []
        self.image = ["C:\\Users\\bryan\Desktop\\KrakeDev\\Programacion_BryanPanchi\\Modulo_V\\POO\\img\\1.webp", "C:\\Users\\bryan\\Desktop\\KrakeDev\\Programacion_BryanPanchi\\Modulo_V\\POO\\img\\3.avif", "C:\\Users\\bryan\\Desktop\\KrakeDev\\Programacion_BryanPanchi\\Modulo_V\\POO\\img\\5.png", "C:\\Users\\bryan\\Desktop\\KrakeDev\\Programacion_BryanPanchi\\Modulo_V\\POO\\img\\8.jpg", "C:\\Users\\bryan\\Desktop\\KrakeDev\\Programacion_BryanPanchi\\Modulo_V\\POO\\img\\10.jpg"]

        self.title = "Ingresar Laptop"
        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self.root, text="Marca").grid(column=0, row=0, padx=10, pady=10)
        self.marca = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.marca).grid(column=1, row=0, padx=10, pady=10)

        ttk.Label(self.root, text="Procesador").grid(column=0, row=1, padx=10, pady=10)
        self.procesador = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.procesador).grid(column=1, row=1, padx=10, pady=10)

        ttk.Label(self.root, text="Memoria").grid(column=0, row=2, padx=10, pady=10)
        self.memoria = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.memoria).grid(column=1, row=2, padx=10, pady=10)

        ttk.Label(self.root, text="Tarjeta Gráfica (Opcional)").grid(column=0, row=3, padx=10, pady=10)
        self.tarjeta_grafica = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.tarjeta_grafica).grid(column=1, row=3, padx=10, pady=10)

        ttk.Label(self.root, text="Precio").grid(column=0, row=4, padx=10, pady=10)
        self.precio = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.precio).grid(column=1, row=4, padx=10, pady=10)

        ttk.Label(self.root, text="Software Empresarial").grid(column=0, row=5, padx=10, pady=10)
        self.software_empresarial = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.software_empresarial).grid(column=1, row=5, padx=10, pady=10)

        ttk.Label(self.root, text="Seguridad").grid(column=0, row=6, padx=10, pady=10)
        self.seguridad = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.seguridad).grid(column=1, row=6, padx=10, pady=10)

        ttk.Button(self.root, text="Agregar Laptop Gaming", command=self.agregar_laptop_gaming).grid(column=0, row=7, padx=10, pady=10)
        ttk.Button(self.root, text="Agregar Laptop Business", command=self.agregar_laptop_business).grid(column=1, row=7, padx=10, pady=10)

        self.mostrar_laptops = tk.Text(self.root, width=50, height=10)
        self.mostrar_laptops.grid(column=0, row=8, columnspan=2, padx=10, pady=10)

        self.canva = tk.Canvas(self.root, width=200, height=200)
        self.canva.grid(column=0, row=9, columnspan=2, padx=10, pady=10)

    def agregar_laptop_gaming(self):
        nueva_laptop = laptop_gaming(self.marca.get(), self.procesador.get(), self.memoria.get(), self.tarjeta_grafica.get(), self.precio.get())
        self.laptops.append(nueva_laptop)
        self.mostrar_laptops.insert(tk.END, str(nueva_laptop) + "\n")
        self.mostrar_imagen_aleatoria()

    def agregar_laptop_business(self):
        nueva_laptop = LaptopBusiness(self.marca.get(), self.procesador.get(), self.memoria.get(), self.software_empresarial.get(), self.seguridad.get(), self.precio.get())
        self.laptops.append(nueva_laptop)
        self.mostrar_laptops.insert(tk.END, str(nueva_laptop) + "\n")
        self.mostrar_imagen_aleatoria()

    def mostrar_imagen_aleatoria(self):
        imagen_path = random.choice(self.image)
        image = Image.open(imagen_path)
        image = image.resize((200, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        self.canva.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canva.image = photo

root = tk.Tk()
app = App(root)
root.mainloop()
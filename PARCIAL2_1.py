import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

#REPRESENTA LIBRO
class Libro:
    def __init__(self, titulo, autor, categoria, estado):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.estado = estado

    def __str__(self):
        return f"{self.titulo} - {self.autor} [{self.categoria}] [{self.estado}]"

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "categoria": self.categoria,
            "estado": self.estado
        }

#REPRESENTA USUARIO
class Usuario:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        return f"{self.nombre} (ID: {self.codigo})"

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "codigo": self.codigo
        }

#REPRESENTA BIBLIOTECA
class Biblioteca:
    def __init__(self):  
        self.libros = []
        self.usuarios = []
        self.archivo = "C:/Users/ESTUDIANTES/Documents/Parcial_2/biblioteca.json"
        self.cargar_datos()

    def registrar_libro(self, titulo, autor, categoria, estado):
        if categoria not in ["Ciencia Ficcion", "Paranormal", "Romcom"]:
            messagebox.showerror("Error", "Categoría no válida.")
            return
        if estado not in ["Prestado", "Devuelto"]:
            messagebox.showerror("Error", "Estado no válido.")
            return
        libro = Libro(titulo, autor, categoria, estado)
        self.libros.append(libro)
        self.guardar_datos()
        messagebox.showinfo("Éxito", "Libro registrado exitosamente.")

    def registrar_usuario(self, nombre, codigo):
        usuario = Usuario(nombre, codigo)
        self.usuarios.append(usuario)
        self.guardar_datos()
        messagebox.showinfo("Éxito", "Usuario registrado exitosamente.")

    def mostrar_libros(self):
        if not self.libros:
            return "No hay libros registrados."
        return "\n".join(str(libro) for libro in self.libros)

    def mostrar_usuarios(self):
        if not self.usuarios:
            return "No hay usuarios registrados."
        return "\n".join(str(usuario) for usuario in self.usuarios)

    def guardar_datos(self):
        datos = {
            "libros": [libro.to_dict() for libro in self.libros],
            "usuarios": [usuario.to_dict() for usuario in self.usuarios]
        }
        with open(self.archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    def cargar_datos(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                self.libros = [Libro(**l) for l in datos.get("libros", [])]
                self.usuarios = [Usuario(**u) for u in datos.get("usuarios", [])]


#INTERFAZ GRÁFICA 
biblioteca = Biblioteca()
ventana = tk.Tk()
ventana.title("Biblioteca Parcial")
ventana.geometry("600x500")
ventana.configure(bg="#f0f0f0")

#Título
tk.Label(ventana, text="BIBLIOTECA", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=20)


def registrar_libro():
    titulo = simpledialog.askstring("Título", "Ingrese el título:")
    autor = simpledialog.askstring("Autor", "Ingrese el autor:")
    categoria = simpledialog.askstring("Categoría", "Ciencia Ficcion, Paranormal, Romcom:")
    estado = simpledialog.askstring("Estado", "Prestado o Devuelto:")
    if titulo and autor and categoria and estado:
        biblioteca.registrar_libro(titulo, autor, categoria, estado)


def registrar_usuario():
    nombre = simpledialog.askstring("Nombre", "Ingrese el nombre del usuario:")
    codigo = simpledialog.askstring("Código", "Ingrese el código del usuario:")
    if nombre and codigo:
        biblioteca.registrar_usuario(nombre, codigo)


def ver_libros():
    resultado = biblioteca.mostrar_libros()
    messagebox.showinfo("Libros", resultado)


def ver_usuarios():
    resultado = biblioteca.mostrar_usuarios()
    messagebox.showinfo("Usuarios", resultado)


#Botones
tk.Button(ventana, text="Registrar Libro", command=registrar_libro, width=30).pack(pady=5)
tk.Button(ventana, text="Registrar Usuario", command=registrar_usuario, width=30).pack(pady=5)
tk.Button(ventana, text="Mostrar Libros", command=ver_libros, width=30).pack(pady=5)
tk.Button(ventana, text="Mostrar Usuarios", command=ver_usuarios, width=30).pack(pady=5)
tk.Button(ventana, text="Salir", command=ventana.quit, width=30).pack(pady=20)

ventana.mainloop()

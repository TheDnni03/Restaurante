import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from conexion import conectar_bd

def actualizar_barra():
    progreso = 0
    incremento = 100 / (10 * 10)  
    def incrementar():
        nonlocal progreso
        progreso += incremento
        barra_carga['value'] = progreso
        if progreso < 100:
            ventana.after(100, incrementar)
        else:
            ventana.destroy()

    incrementar()

def iniciar_carga_si_conexion_exitosa():
    try:
        conexion = conectar_bd()
        if conexion:
            actualizar_barra()
        else:
            messagebox.showerror("Error de Conexión", "No se pudo conectar a la base de datos.")
    except Exception as e:
        messagebox.showerror("Error de Conexión", f"Error al conectar a la base de datos: {e}")

ventana = tk.Tk()
ventana.title("Interfaz Restaurante")
ventana.geometry("400x400")

imagen_original = Image.open("img/logo.jpeg")
imagen_redimensionada = imagen_original.resize((50, 50), Image.LANCZOS)
logo = ImageTk.PhotoImage(imagen_redimensionada)

logo_label = tk.Label(ventana, image=logo)
logo_label.pack(pady=20)

texto_label = tk.Label(ventana, text="Restaurante", font=("Arial", 24))
texto_label.pack()

barra_carga = ttk.Progressbar(ventana, orient="horizontal", length=300, mode="determinate")
barra_carga.pack(pady=20)

logo_label.image = logo

iniciar_carga_si_conexion_exitosa()

ventana.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from conexion import conectar_bd

def obtener_lista_meseros():
    try:
        conexion = conectar_bd()
        if conexion:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT nombre FROM mesero")
                meseros = [fila[0] for fila in cursor.fetchall()]
            conexion.close()
            return meseros
        else:
            return []
    except Exception as e:
        print(f"Error al obtener la lista de meseros: {e}")
        return []

def actualizar_barra(ventana, barra_carga):
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

def iniciar_carga_si_conexion_exitosa(ventana, combobox_meseros, barra_carga):
    usuario_seleccionado = combobox_meseros.get()
    if not usuario_seleccionado:
        messagebox.showwarning("Usuario no seleccionado", "Por favor, seleccione un mesero.")
        return

    try:
        conexion = conectar_bd()
        if conexion:
            print(f"Conexión exitosa con el mesero {usuario_seleccionado}")
            actualizar_barra(ventana, barra_carga)
        else:
            messagebox.showerror("Error de Conexión", "No se pudo conectar a la base de datos.")
    except Exception as e:
        messagebox.showerror("Error de Conexión", f"Error al conectar a la base de datos: {e}")

def abrir_carga_mesero():
    ventana = tk.Toplevel()  # Cambiar a Toplevel para no cerrar la ventana principal
    ventana.title("Interfaz Restaurante")
    ventana.geometry("400x400")

    # Logo
    imagen_original = Image.open("img/logo.jpeg")
    imagen_redimensionada = imagen_original.resize((50, 50), Image.LANCZOS)
    logo = ImageTk.PhotoImage(imagen_redimensionada)
    logo_label = tk.Label(ventana, image=logo)
    logo_label.image = logo  # Mantener referencia a la imagen
    logo_label.pack(pady=20)

    # Título
    texto_label = tk.Label(ventana, text="Restaurante", font=("Arial", 24))
    texto_label.pack()

    # Lista de meseros
    lista_meseros = obtener_lista_meseros()
    combobox_meseros = ttk.Combobox(ventana, values=lista_meseros)
    combobox_meseros.set("Seleccione un mesero")
    combobox_meseros.pack(pady=10)

    # Barra de carga
    barra_carga = ttk.Progressbar(ventana, orient="horizontal", length=300, mode="determinate")
    barra_carga.pack(pady=20)

    # Botón para iniciar
    boton_iniciar = tk.Button(
        ventana,
        text="Iniciar",
        command=lambda: iniciar_carga_si_conexion_exitosa(ventana, combobox_meseros, barra_carga)
    )
    boton_iniciar.pack(pady=10)
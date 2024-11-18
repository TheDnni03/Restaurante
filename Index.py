import tkinter as tk
from Mesas import abrir_vista_restaurante  # Importar la función desde Mesas.py

def crear_interfaz():
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Restaurante")
    ventana.attributes('-fullscreen', True)  # Pantalla completa
    ventana.configure(bg="#f0f0f0")  # Fondo claro

    # Salir de la pantalla completa con la tecla ESC
    ventana.bind("<Escape>", lambda event: ventana.attributes('-fullscreen', False))

    # Texto principal centrado
    titulo = tk.Label(
        ventana,
        text="Restaurante 'Nombre'",
        font=("Arial", 30, "bold"),
        bg="#f0f0f0",
        fg="#333"
    )
    titulo.place(relx=0.5, rely=0.3, anchor="center")  # Centrado vertical y horizontal

    # Crear el marco para los botones principales
    contenedor_botones = tk.Frame(ventana, bg="#f0f0f0")
    contenedor_botones.place(relx=0.5, rely=0.5, anchor="center")

    # Botón 1: Mesero
    boton_mesero = tk.Button(
        contenedor_botones,
        text="Mesero",
        font=("Arial", 14),
        bg="#555",
        fg="white",
        width=20,
        height=2,
        command=lambda: print("Mesero seleccionado")
    )
    boton_mesero.pack(pady=10)  # Añadir margen vertical entre botones

    # Botón 2: Encargado
    boton_encargado = tk.Button(
        contenedor_botones,
        text="Encargado",
        font=("Arial", 14),
        bg="#555",
        fg="white",
        width=20,
        height=2,
        command=lambda: print("Encargado seleccionado")
    )
    boton_encargado.pack(pady=10)

    # Botón 3: Vista del Restaurante
    boton_vista = tk.Button(
        contenedor_botones,
        text="Vista del Restaurante",
        font=("Arial", 14),
        bg="#555",
        fg="white",
        width=20,
        height=2,
        command=abrir_vista_restaurante  # Llama a la función en Mesas.py
    )
    boton_vista.pack(pady=10)

    # Botón para cerrar la ventana principal
    boton_cerrar = tk.Button(
        ventana,
        text="Cerrar",
        font=("Arial", 12),
        bg="red",
        fg="white",
        width=10,
        height=2,
        command=ventana.destroy  # Cierra la ventana
    )
    boton_cerrar.place(relx=0.95, rely=0.95, anchor="se")  # Colocar en la esquina inferior derecha

    ventana.mainloop()

# Ejecutar la interfaz principal
if __name__ == "__main__":
    crear_interfaz()

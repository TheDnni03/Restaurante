import tkinter as tk
from Mesas import abrir_vista_restaurante
from Carga import abrir_carga_mesero

def crear_interfaz():
    ventana = tk.Tk()
    ventana.title("Restaurante")
    ventana.attributes('-fullscreen', True)
    ventana.configure(bg="#f0f0f0")

    ventana.bind("<Escape>", lambda event: ventana.attributes('-fullscreen', False))

    titulo = tk.Label(
        ventana,
        text="Restaurante 'Nombre'",
        font=("Arial", 30, "bold"),
        bg="#f0f0f0",
        fg="#333"
    )
    titulo.place(relx=0.5, rely=0.3, anchor="center")

    contenedor_botones = tk.Frame(ventana, bg="#f0f0f0")
    contenedor_botones.place(relx=0.5, rely=0.5, anchor="center")

    boton_mesero = tk.Button(
        contenedor_botones,
        text="Mesero",
        font=("Arial", 14),
        bg="#555",
        fg="white",
        width=20,
        height=2,
        command=lambda: abrir_carga_mesero(ventana)
    )
    boton_mesero.pack(pady=10)

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

    boton_vista = tk.Button(
        contenedor_botones,
        text="Vista del Restaurante",
        font=("Arial", 14),
        bg="#555",
        fg="white",
        width=20,
        height=2,
        command=lambda: print("Vista del Restaurante seleccionada")
    )
    boton_vista.pack(pady=10)

    boton_cerrar = tk.Button(
        ventana,
        text="Cerrar",
        font=("Arial", 12),
        bg="red",
        fg="white",
        width=10,
        height=2,
        command=ventana.destroy
    )
    boton_cerrar.place(relx=0.95, rely=0.95, anchor="se")
    ventana.mainloop()

if __name__ == "__main__":
    crear_interfaz()

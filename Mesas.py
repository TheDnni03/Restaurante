import tkinter as tk
from EjecutarQuery import ejecutar_consulta

def abrir_vista_restaurante():
    ventana_restaurante = tk.Toplevel()
    ventana_restaurante.title("Vista del Restaurante")
    ventana_restaurante.geometry("800x800")
    ventana_restaurante.configure(bg="#f0f0f0")

    query = "SELECT Id_Pedido, Estado FROM Pedido WHERE Estado = %P"
    resultados = ejecutar_consulta(query, ("Activo",))

    if resultados is None:
        tk.Label(
            ventana_restaurante,
            text="Error al cargar los datos.",
            font=("Arial", 14),
            fg="red",
            bg="#f0f0f0"
        ).pack(pady=20)
        return

    contenedor_cuadricula = tk.Frame(ventana_restaurante, bg="#f0f0f0", padx=20, pady=20)
    contenedor_cuadricula.pack(expand=True)  # Centrar en la ventana

    for idx, (id_pedido, estado) in enumerate(resultados):
        fila = idx // 10 
        columna = idx % 10 

        boton = tk.Button(
            contenedor_cuadricula,
            text=f"Pedido {id_pedido}",
            font=("Arial", 10),
            width=10,
            height=2,
            bg="#4caf50" if estado == "Activo" else "#ccc",
            command=lambda x=id_pedido: print(f"Pedido seleccionado: {x}")
        )
        boton.grid(row=fila, column=columna, padx=5, pady=5)

    if not resultados:
        tk.Label(
            ventana_restaurante,
            text="No hay pedidos activos.",
            font=("Arial", 14),
            fg="blue",
            bg="#f0f0f0"
        ).pack(pady=20)

if __name__ == "__main__":
    abrir_vista_restaurante()
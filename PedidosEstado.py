import tkinter as tk
from tkinter import scrolledtext
from EjecutarQuery import ejecutar_consulta
import InsertarPedido

def mostrar_pedidos():
    resultados = ejecutar_consulta("SELECT * FROM Pedidos")
    mostrar_resultados(resultados)

def mostrar_entregados():
    resultados = ejecutar_consulta("SELECT * FROM Pedidos WHERE estado = 'entregado'")
    mostrar_resultados(resultados)

def mostrar_activos():
    resultados = ejecutar_consulta("SELECT * FROM Pedidos WHERE estado = 'activo'")
    mostrar_resultados(resultados)

def mostrar_resultados(resultados):
    cuadro_texto.delete('1.0', tk.END)
    if resultados:
        for fila in resultados:
            cuadro_texto.insert(tk.END, f"{fila}\n")
    else:
        cuadro_texto.insert(tk.END, "No se encontraron resultados.\n")

def salir():
    ventana.destroy()

ventana = tk.Tk()
ventana.title("Gestión de Pedidos")

frame_botones = tk.Frame(ventana)
frame_botones.pack(side=tk.TOP, fill=tk.X)

boton_pedidos = tk.Button(frame_botones, text="Pedidos", command=mostrar_pedidos)
boton_pedidos.pack(side=tk.LEFT, padx=5, pady=5)

boton_entregados = tk.Button(frame_botones, text="Entregados", command=mostrar_entregados)
boton_entregados.pack(side=tk.LEFT, padx=5, pady=5)

boton_activos = tk.Button(frame_botones, text="Activos", command=mostrar_activos)
boton_activos.pack(side=tk.LEFT, padx=5, pady=5)

# Agregar botón "Agregar" para abrir InsertarPedido.py
boton_agregar = tk.Button(frame_botones, text="Agregar", command=InsertarPedido.insertar_pedido)
boton_agregar.pack(side=tk.LEFT, padx=5, pady=5)

boton_salir = tk.Button(frame_botones, text="Salir", command=salir)
boton_salir.pack(side=tk.LEFT, padx=5, pady=5)

cuadro_texto = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=50, height=20)
cuadro_texto.pack(padx=10, pady=10)

ventana.mainloop()

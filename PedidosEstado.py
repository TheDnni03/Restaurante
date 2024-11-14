import tkinter as tk
from EjecutarQuery import ejecutar_consulta

def mostrar_pedidos():
    resultados = ejecutar_consulta("SELECT * FROM Pedido")
    mostrar_resultados(resultados)

def mostrar_entregados():
    resultados = ejecutar_consulta("SELECT * FROM Pedido WHERE estado = 'entregado'")
    mostrar_resultados(resultados)

def mostrar_activos():
    resultados = ejecutar_consulta("SELECT * FROM Pedido WHERE estado = 'activo'")
    mostrar_resultados(resultados)

def mostrar_resultados(resultados):
    # Limpiamos el contenedor de pedidos
    for widget in contenedor_pedidos.winfo_children():
        widget.destroy()
    
    if resultados:
        for fila in resultados:
            # Excluir el ID y formatear el tiempo para incluir segundos
            fecha, estado, pago, total, id_mesero, id_cliente = fila[1:]
            fecha_formateada = fecha.strftime('%Y-%m-%d %H:%M:%S')
            
            # Crear un recuadro (Frame) para cada pedido
            recuadro_pedido = tk.Frame(contenedor_pedidos, bd=1, relief="solid", padx=5, pady=5)
            recuadro_pedido.pack(fill="x", pady=5, padx=5)

            # Crear etiquetas dentro del recuadro para cada campo
            texto_pedido = f"Fecha: {fecha_formateada} | Estado: {estado} | Pago: {pago} | Total: {total} | Mesero ID: {id_mesero} | Cliente ID: {id_cliente}"
            etiqueta_pedido = tk.Label(recuadro_pedido, text=texto_pedido, anchor="w")
            etiqueta_pedido.pack(fill="x")
    else:
        etiqueta_no_resultados = tk.Label(contenedor_pedidos, text="No se encontraron resultados.", anchor="w")
        etiqueta_no_resultados.pack(fill="x", pady=5)

def salir():
    ventana.destroy()

ventana = tk.Tk()
ventana.title("Gestión de Pedidos")

# Sección de botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(side=tk.TOP, fill=tk.X)

boton_pedidos = tk.Button(frame_botones, text="Pedidos", command=mostrar_pedidos)
boton_pedidos.pack(side=tk.LEFT, padx=5, pady=5)

boton_entregados = tk.Button(frame_botones, text="Entregados", command=mostrar_entregados)
boton_entregados.pack(side=tk.LEFT, padx=5, pady=5)

boton_activos = tk.Button(frame_botones, text="Activos", command=mostrar_activos)
boton_activos.pack(side=tk.LEFT, padx=5, pady=5)

boton_salir = tk.Button(frame_botones, text="Salir", command=salir)
boton_salir.pack(side=tk.LEFT, padx=5, pady=5)

# Contenedor para los pedidos
contenedor_pedidos = tk.Frame(ventana)
contenedor_pedidos.pack(fill="both", expand=True, padx=10, pady=10)

ventana.mainloop()
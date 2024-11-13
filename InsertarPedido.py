import tkinter as tk
from tkinter import StringVar
from EjecutarQuery import ejecutar_consulta
from datetime import datetime

def insertar_pedido():
    ventana = tk.Toplevel()
    ventana.title("Insertar Nuevo Pedido")

    # Fecha actual (automática)
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tk.Label(ventana, text="Fecha (YYYY-MM-DD HH:MM:SS):").grid(row=0, column=0, padx=10, pady=5)
    entrada_fecha = tk.Entry(ventana)
    entrada_fecha.grid(row=0, column=1, padx=10, pady=5)
    entrada_fecha.insert(0, fecha_actual)  # Rellena la fecha automáticamente

    # Estado fijo (Activo)
    tk.Label(ventana, text="Estado:").grid(row=1, column=0, padx=10, pady=5)
    entrada_estado = tk.Entry(ventana)
    entrada_estado.grid(row=1, column=1, padx=10, pady=5)
    entrada_estado.insert(0, "Activo")  # Estado siempre será 'Activo'
    entrada_estado.config(state="readonly")  # No se puede editar

    # Método de pago (Menú desplegable)
    tk.Label(ventana, text="Método de Pago:").grid(row=2, column=0, padx=10, pady=5)
    metodo_pago_var = StringVar(ventana)
    metodo_pago_var.set("Efectivo")  # Valor predeterminado
    opciones_metodo_pago = ["Efectivo", "Tarjeta"]
    menu_metodo_pago = tk.OptionMenu(ventana, metodo_pago_var, *opciones_metodo_pago)
    menu_metodo_pago.grid(row=2, column=1, padx=10, pady=5)

    # Monto Total
    tk.Label(ventana, text="Monto Total:").grid(row=3, column=0, padx=10, pady=5)
    entrada_monto_total = tk.Entry(ventana)
    entrada_monto_total.grid(row=3, column=1, padx=10, pady=5)

    # ID Cliente
    tk.Label(ventana, text="ID Cliente:").grid(row=4, column=0, padx=10, pady=5)
    entrada_id_cliente = tk.Entry(ventana)
    entrada_id_cliente.grid(row=4, column=1, padx=10, pady=5)

    # Función para crear el pedido
    def crear_pedido():
        fecha = entrada_fecha.get()
        estado = entrada_estado.get()
        metodo_pago = metodo_pago_var.get()
        monto_total = entrada_monto_total.get()
        id_cliente = entrada_id_cliente.get()

        # Ejecuta la consulta de creación de pedido
        query_crear = "SELECT CrearPedido(%s, %s, %s, %s, %s)"
        parametros_crear = (fecha, estado, metodo_pago, monto_total, id_cliente)
        resultado = ejecutar_consulta(query_crear, parametros_crear)

        if resultado:
            global id_pedido_creado
            id_pedido_creado = resultado[0][0]  # Guarda el ID de pedido
            tk.Label(ventana, text=f"Pedido creado con ID: {id_pedido_creado}", fg="green").grid(row=7, column=0, columnspan=2, pady=10)
            boton_agregar_producto.config(state=tk.NORMAL)
        else:
            tk.Label(ventana, text="Error al crear el pedido.", fg="red").grid(row=7, column=0, columnspan=2, pady=10)

    boton_crear_pedido = tk.Button(ventana, text="Crear Pedido", command=crear_pedido)
    boton_crear_pedido.grid(row=5, column=0, columnspan=2, pady=10)

    # Campos para agregar productos al pedido
    tk.Label(ventana, text="ID Producto:").grid(row=8, column=0, padx=10, pady=5)
    entrada_id_producto = tk.Entry(ventana)
    entrada_id_producto.grid(row=8, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Cantidad:").grid(row=9, column=0, padx=10, pady=5)
    entrada_cantidad = tk.Entry(ventana)
    entrada_cantidad.grid(row=9, column=1, padx=10, pady=5)

    # Función para agregar productos al pedido
    def agregar_producto():
        id_producto = entrada_id_producto.get()
        cantidad = entrada_cantidad.get()

        # Ejecuta la consulta para agregar producto al pedido
        query_agregar = "SELECT AgregarProductoAPedido(%s, %s, %s)"
        parametros_agregar = (id_pedido_creado, id_producto, cantidad)
        resultado = ejecutar_consulta(query_agregar, parametros_agregar)

        if resultado:
            tk.Label(ventana, text="Producto agregado con éxito!", fg="green").grid(row=11, column=0, columnspan=2, pady=10)
        else:
            tk.Label(ventana, text="Error al agregar el producto.", fg="red").grid(row=11, column=0, columnspan=2, pady=10)

    boton_agregar_producto = tk.Button(ventana, text="Agregar Producto", command=agregar_producto, state=tk.DISABLED)
    boton_agregar_producto.grid(row=10, column=0, columnspan=2, pady=10)

    # Variable global para almacenar el ID de pedido generado
    global id_pedido_creado
    id_pedido_creado = None

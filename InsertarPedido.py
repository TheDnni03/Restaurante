import tkinter as tk
from datetime import datetime
from EjecutarQuery import ejecutar_consulta

def insertar_orden():
    ventana = tk.Tk()
    ventana.title("Insertar Nueva Orden")

    tk.Label(ventana, text="Nombre del Cliente:").grid(row=0, column=0, padx=10, pady=5)
    entrada_nombre = tk.Entry(ventana)
    entrada_nombre.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Apellidos del Cliente:").grid(row=1, column=0, padx=10, pady=5)
    entrada_apellidos = tk.Entry(ventana)
    entrada_apellidos.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Email del Cliente:").grid(row=2, column=0, padx=10, pady=5)
    entrada_email = tk.Entry(ventana)
    entrada_email.grid(row=2, column=1, padx=10, pady=5)

    def crear_cliente():
        nombre = entrada_nombre.get()
        apellidos = entrada_apellidos.get()
        email = entrada_email.get()
        fecha_registro = datetime.now().strftime("%Y-%m-%d")
        id_cuenta = 28
        id_mesa = 1

        query_cliente = """
            INSERT INTO Cliente (Nombre, Apellidos, Email, FechaRegi, Id_Cuenta, Id_Mesa)
            VALUES (%s, %s, %s, %s, %s, %s) RETURNING Id_Cliente
        """
        parametros_cliente = (nombre, apellidos, email, fecha_registro, id_cuenta, id_mesa)
        resultado = ejecutar_consulta(query_cliente, parametros_cliente)

        if resultado:
            global id_cliente_creado
            id_cliente_creado = resultado[0][0]
            tk.Label(ventana, text=f"Cliente creado con ID: {id_cliente_creado}", fg="green").grid(row=4, column=0, columnspan=2, pady=10)
            boton_insertar_producto.config(state=tk.NORMAL)
        else:
            tk.Label(ventana, text="Error al crear el cliente.", fg="red").grid(row=4, column=0, columnspan=2, pady=10)

    boton_crear_cliente = tk.Button(ventana, text="Crear Cliente", command=crear_cliente)
    boton_crear_cliente.grid(row=3, column=0, columnspan=2, pady=10)

    def obtener_productos():
        query_productos = "SELECT Id_Productos, Producto FROM Productos"
        productos = ejecutar_consulta(query_productos, ())
        return productos

    productos = obtener_productos()
    if productos:
        productos_lista = [f"{producto[1]} (ID: {producto[0]})" for producto in productos]
        id_producto_var = tk.StringVar(ventana)
        id_producto_var.set(productos_lista[0])

        tk.Label(ventana, text="Selecciona Producto:").grid(row=5, column=0, padx=10, pady=5)
        menu_productos = tk.OptionMenu(ventana, id_producto_var, *productos_lista)
        menu_productos.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Cantidad:").grid(row=6, column=0, padx=10, pady=5)
    entrada_cantidad = tk.Entry(ventana)
    entrada_cantidad.grid(row=6, column=1, padx=10, pady=5)

    productos_pedido = []

    def agregar_producto():
        seleccion = id_producto_var.get()
        id_producto = seleccion.split("(ID: ")[1].replace(")", "")
        cantidad = entrada_cantidad.get()

        if cantidad.isdigit() and int(cantidad) > 0:
            productos_pedido.append((id_producto, cantidad))
            tk.Label(ventana, text="Producto agregado.", fg="green").grid(row=8, column=0, columnspan=2, pady=5)
            boton_crear_pedido.config(state=tk.NORMAL)
        else:
            tk.Label(ventana, text="Cantidad inválida.", fg="red").grid(row=8, column=0, columnspan=2, pady=5)

    boton_insertar_producto = tk.Button(ventana, text="Agregar Producto", command=agregar_producto, state=tk.DISABLED)
    boton_insertar_producto.grid(row=7, column=0, columnspan=2, pady=10)

    tk.Label(ventana, text="Monto Total:").grid(row=9, column=0, padx=10, pady=5)
    entrada_monto_total = tk.Entry(ventana)
    entrada_monto_total.grid(row=9, column=1, padx=10, pady=5)

    def crear_pedido():
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        estado = "Activo"
        metodo_pago = "Efectivo"  # Por defecto
        monto_total = entrada_monto_total.get()
        id_cliente = id_cliente_creado

        query_pedido = "SELECT CrearPedido(%s, %s, %s, %s, %s)"
        parametros_pedido = (fecha, estado, metodo_pago, monto_total, id_cliente)
        resultado_pedido = ejecutar_consulta(query_pedido, parametros_pedido)

        if resultado_pedido:
            id_pedido_creado = resultado_pedido[0][0]
            tk.Label(ventana, text=f"Pedido creado con ID: {id_pedido_creado}", fg="green").grid(row=11, column=0, columnspan=2, pady=10)

            for id_producto, cantidad in productos_pedido:
                query_agregar_producto = "SELECT AgregarProductoAPedido(%s, %s, %s)"
                parametros_producto = (id_pedido_creado, id_producto, cantidad)
                ejecutar_consulta(query_agregar_producto, parametros_producto)

            tk.Label(ventana, text="Productos agregados al pedido.", fg="green").grid(row=12, column=0, columnspan=2, pady=10)
        else:
            tk.Label(ventana, text="Error al crear el pedido.", fg="red").grid(row=11, column=0, columnspan=2, pady=10)

    boton_crear_pedido = tk.Button(ventana, text="Crear Pedido", command=crear_pedido, state=tk.DISABLED)
    boton_crear_pedido.grid(row=10, column=0, columnspan=2, pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    insertar_orden()

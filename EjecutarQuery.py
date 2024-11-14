from conexion import conectar_bd

def ejecutar_consulta(query, params=None):  # Añade params=None
    conexion = conectar_bd()
    if conexion is None:
        return None

    try:
        with conexion.cursor() as cursor:
            cursor.execute(query, params)  # Usa los parámetros opcionales
            if query.strip().lower().startswith("select"):
                resultados = cursor.fetchall()
            else:
                conexion.commit()
                resultados = cursor.rowcount  # Retorna la cantidad de filas afectadas
        return resultados
    except Exception as e:
        print("Error al ejecutar la consulta:", e)
        return None

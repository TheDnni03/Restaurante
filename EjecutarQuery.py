from conexion import conectar_bd

def ejecutar_consulta(query):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultados
    return []

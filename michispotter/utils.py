import sqlite3
from .database import Bd
from .models import Gato

"""
Funciones auxiliares para buscar gatos y exportar listado de gatos.

"""


def buscar_gatos(termino_busqueda):
    """
    Busca gatos que coinciden con el término de búsqueda en apodo, raza, ubicación o descripción.
    Devuelve una lista de objetos Gato.
    """
    conexion = Bd.abrir()
    cursor = conexion.cursor()

    # Término para SQL LIKE(búsqueda parcial).
    termino = f"%{termino_busqueda}"

    # Consulta SQL para buscar gatos que coincidan con el término de búsqueda usando OR.
    resultado = cursor.execute(
        """
        SELECT id, raza, descripcion, apodo, color 
        FROM gatos
        WHERE apodo LIKE ? OR raza LIKE ? OR ubicacion LIKE ? OR descripcion LIKE ?
        ORDER BY apodo
        """,
        (termino, termino, termino, termino),
    )

    gatos_encontrados = resultado.fetchall()
    lista_gatos = []
    for gato_fila in gatos_encontrados:
        instancia = Gato()
        instancia.id = gato_fila[0]
        instancia.raza = gato_fila[1]
        instancia.descripcion = gato_fila[2]
        instancia.ubicacion = gato_fila[3]
        instancia.apodo = gato_fila[4]
        instancia.color = gato_fila[5]
        lista_gatos.append(instancia)

    return lista_gatos

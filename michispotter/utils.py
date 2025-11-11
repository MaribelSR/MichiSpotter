import sqlite3
import csv
from .database import Bd
from .models import Gato
from .operations import listar_gatos

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
    termino = f"%{termino_busqueda}%"

    # Consulta SQL para buscar gatos que coincidan con el término de búsqueda usando OR.
    resultado = cursor.execute(
        """
        SELECT id, raza, descripcion, ubicacion, apodo, color 
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


def exportar_a_csv(nombre_archivo="gatos.csv"):
    """
    Obtiene todos los gatos de la Base de Datos y los exporta a un archivo CSV.

    Args:
        nombre_archivo (str): El nombre del archivo a generar. Por defecto es "gatos.csv".

    Returns:
        bool: True si la exportación fue exitosa, False si no.
    """
    try:
        # Obtener los datos.
        gatos = listar_gatos()

        # Abrir el archivo en modo escritura ("w"). newline='' es necesario para que csv.writer funcione bien en Windows.
        with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo_csv:

            # Crear el escritor (writer) de CSV.
            escritor = csv.writer(archivo_csv)
            # Escribir la fila de la cabecera (Header).
            escritor.writerow(
                ["ID", "Apodo", "Raza", "Color", "Ubicación", "Descripción"]
            )

            # Escribir los datos de cada gato

            for gato in gatos:
                escritor.writerow(
                    [
                        gato.id,
                        gato.apodo,
                        gato.raza,
                        gato.color,
                        gato.ubicacion,
                        gato.descripcion,
                    ]
                )

        # Exportación exitosa.
        return True
    except IOError as e:
        # Capturamos un posible error si no se pued escribir el archivo
        print(f"Error al escribir el archivo {nombre_archivo}: {e}")
        return False

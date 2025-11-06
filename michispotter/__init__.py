"""
MichiSpotter - Documenta y sigue a los michis de tu barrio 🐱

"""

__version__ = "1.0.0"
__author__ = "Maribel Salvador Rufo"
__license__ = "Apache 2.0"

# Importar las clases y funciones principales para facilitar su uso
from .models import Gato
from .database import Bd
from .operations import (
    crear_gato,
    editar_gato,
    borrar_gato,
    listar_gatos,
    obtener_gato_por_id,
    # contar_gatos,
)

from .utils import (
    buscar_gatos,
    # exportar_a_txt,
    # obtener_estadisticas,
    # obtener_raza_mas_comun,
    # listar_gatos_por_ubicacion,
)

# Define qué se importa cuando alguien hace: from michispotter import *
__all__ = [
    # Modelos
    "Gato",
    # Base de datos
    "Bd",
    # Operaciones CRUD
    "crear_gato",
    "editar_gato",
    "borrar_gato",
    "listar_gatos",
    "obtener_gato_por_id",
    # "contar_gatos",
    # Utilidades
    "buscar_gatos",
    # "exportar_a_txt",
    # "obtener_estadisticas",
    # "obtener_raza_mas_comun",
    # "listar_gatos_por_ubicacion",
]

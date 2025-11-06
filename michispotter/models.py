"""
Modelos de datos para MichiSpotter.

Este módulo contiene las clases que representan las entidades
de la aplicación (en este caso, gatos).
"""


class Gato:
    """
    Representa un gato del barrio.

    Atributos:
        id (int): Identificador único del gato en la base de datos.
        apodo (str): Nombre o apodo del gato (obligatorio).
        raza (str): Raza del gato.
        color (str): Color predominante del gato
        ubicacion (str): Lugar donde se suele ver al gato
        descripcion (str): Características y comportamiento del gato
    """

    def __init__(self):
        """Inicializa un nuevo gato con valores por defecto."""
        self.id = 0
        self.apodo = ""
        self.raza = ""
        self.color = ""
        self.ubicacion = ""
        self.descripcion = ""

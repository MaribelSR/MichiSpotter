from .database import Bd
from .models import Gato


def crear_gato(gato):
    conexion = Bd.abrir()
    cursor = conexion.cursor()
    resultado = cursor.execute(
        "INSERT INTO gatos (raza, descripcion, color, ubicacion, apodo) VALUES (?, ?, ?, ?, ?)",
        (gato.raza, gato.descripcion, gato.color, gato.ubicacion, gato.apodo),
    )
    gato.id = resultado.lastrowid

    return gato.id > 0


def editar_gato(gato):
    conexion = Bd.abrir()
    cursor = conexion.cursor()
    resultado = cursor.execute(
        "UPDATE gatos SET raza=?, descripcion=?, color=?, ubicacion=?, apodo=? WHERE id=?",
        (gato.raza, gato.descripcion, gato.color, gato.ubicacion, gato.apodo, gato.id),
    )

    return resultado.rowcount == 1


def borrar_gato(gato):
    conexion = Bd.abrir()
    cursor = conexion.cursor()
    resultado = cursor.execute("DELETE FROM gatos WHERE id=?", (gato.id,))

    return resultado.rowcount == 1


def listar_gatos():
    conexion = Bd.abrir()
    cursor = conexion.cursor()
    resultado = cursor.execute(
        "SELECT id, raza, descripcion, color, ubicacion, apodo FROM gatos ORDER BY apodo"
    )
    gatos = resultado.fetchall()
    lista_gatos = []
    for gato in gatos:
        instancia = Gato()
        instancia.id = gato[0]
        instancia.raza = gato[1]
        instancia.descripcion = gato[2]
        instancia.ubicacion = gato[3]
        instancia.apodo = gato[4]
        instancia.apodo = gato[5]
        lista_gatos.append(instancia)

    return lista_gatos


def obtener_gato_por_id(id_gato):
    """
    Busca y devuelve un objeto Gato por su ID.
    Si no lo encuentra, devuelve None.
    """
    conexion = Bd.abrir()
    cursor = conexion.cursor()
    # Uso de WHERE id=? para buscar por ID.
    resultado = cursor.execute(
        "SELECT id, raza, descripcion, ubicacion, apodo, color FROM gatos WHERE id=?",
        (id_gato,),  # Se pasa el ID como una tupla.
    )
    # fetchone() devuelve una fila (o None si no hay resultados).
    gato_fila = resultado.fetchone()

    if gato_fila:
        instancia = Gato()
        instancia.id = gato_fila[0]
        instancia.raza = gato_fila[1]
        instancia.descripcion = gato_fila[2]
        instancia.ubicacion = gato_fila[3]
        instancia.apodo = gato_fila[4]
        instancia.color = gato_fila[5]
        return instancia
    else:
        # No se encontró ningún gato con ese ID.
        return None

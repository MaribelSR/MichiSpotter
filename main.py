import sqlite3


class Bd:
    nombre = "gatos.sqlite3"
    __conexion = None

    @staticmethod
    def abrir():
        if Bd.__conexion:
            return Bd.__conexion
        else:
            Bd.__conexion = sqlite3.connect(Bd.nombre)
            cursor = Bd.__conexion.cursor()
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS gatos (id INTEGER PRIMARY KEY AUTOINCREMENT, raza TEXT, descripcion TEXT, ubicacion TEXT, apodo TEXT)"
            )
            return Bd.__conexion

    @staticmethod
    def cerrar():
        if Bd.__conexion:
            Bd.__conexion.commit()
            Bd.__conexion.close()
            Bd.__conexion = None


class Gato:
    id = 0
    raza = ""
    descripcion = ""
    ubicacion = ""
    apodo = ""


def crear_gato(gato):
    conexion = Bd.abrir()
    cursor = conexion.cursor()
    resultado = cursor.execute(
        "INSERT INTO gatos (raza, descripcion, ubicacion, apodo) VALUES (?, ?, ?, ?)",
        (gato.raza, gato.descripcion, gato.ubicacion, gato.apodo),
    )
    gato.id = resultado.lastrowid

    return gato.id > 0


def editar_gato(gato):
    conexion = Bd.abrir()
    cursor = conexion.cursor()
    resultado = cursor.execute(
        "UPDATE gatos SET raza=?, descripcion=?, ubicacion=?, apodo=? WHERE id=?",
        (gato.raza, gato.descripcion, gato.ubicacion, gato.apodo, gato.id),
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
        "SELECT id, raza, descripcion, ubicacion, apodo FROM gatos ORDER BY apodo"
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
        lista_gatos.append(instancia)

    return lista_gatos


if __name__ == "__main__":
    try:
        pass
    finally:
        Bd.cerrar()

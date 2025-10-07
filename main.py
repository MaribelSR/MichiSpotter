import sqlite3

class Bd:
    nombre = "gatos.sqlite3"  
    __conexion = None
    def abrir():
        if Bd.__conexion:
            return Bd.__conexion
        else:
            Bd.__conexion = sqlite3.connect(Bd.nombre)
            cursor = Bd.__conexion.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS gatos (id PRIMARY KEY, raza TEXT, descripcion TEXT, ubicacion TEXT, apodo TEXT)")
            return Bd.__conexion

    def cerrar():
        Bd.__conexion = Bd.abrir()
        Bd.__conexion.commit()
        Bd.__conexion.close()


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
        f"INSERT INTO gatos (raza, descripcion, ubicacion, apodo) VALUES ('{gato.raza}','{gato.descripcion}', '{gato.ubicacion}', '{gato.apodo}')"
    )
    gato.id = resultado.lastrowid
    return gato.id > 0


def editar_gato(gato):
    return False


def borrar_gato(gato):
    return False


def listar_gatos():
    return []


if __name__ == "__main__":
    try:
        pass
    finally:
        Bd.cerrar()

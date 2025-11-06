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
                "CREATE TABLE IF NOT EXISTS gatos (id INTEGER PRIMARY KEY AUTOINCREMENT, raza TEXT, descripcion TEXT, color TEXT, ubicacion TEXT, apodo TEXT)"
            )
            return Bd.__conexion

    @staticmethod
    def cerrar():
        if Bd.__conexion:
            Bd.__conexion.commit()
            Bd.__conexion.close()
            Bd.__conexion = None

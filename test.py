from main import Gato, crear_gato, borrar_gato, Bd
import main


def gato_prueba():
    gato = Gato()
    gato.raza = "Carey"
    gato.descripcion = "Tiene manchas marrones"
    gato.ubicacion = "Calle Porvera, Jerez de la Frontera, Cádiz."
    gato.apodo = "Manchitas"
    return gato


def test_crear_gato():
    main.nombre_bd = ":memory:"
    gato = gato_prueba()

    resultado = crear_gato(gato)
    assert resultado, "crear_gato ha devuelto False."
    assert gato.id > 0, "gato.id no tiene un valor correcto."

    conexion = Bd.abrir()
    cursor = conexion.cursor()
    resultado = cursor.execute(f"SELECT * FROM gatos WHERE id={gato.id}")
    numero_gatos = len(resultado.fetchall())

    assert numero_gatos == 1, "numero_gatos debe ser uno."


def test_borrar_gato():
    main.nombre_bd = ":memory:"
    gato = gato_prueba()

    assert crear_gato(gato), "crear_gato no ha funcionado."
    assert borrar_gato(gato), "borrar_gato no ha funcionado."

    conexion = Bd.abrir()
    cursor = conexion.cursor()
    resultado = cursor.execute(f"SELECT * FROM gatos WHERE id={gato.id}")
    numero_gatos = len(resultado.fetchall())

    assert numero_gatos == 0, "numero_gatos debe ser cero."


if __name__ == "__main__":
    try:
        for fn in [test_crear_gato, test_borrar_gato]:
            try:
                fn()
                print(f"✅ {fn.__name__}")
            except AssertionError as e:
                print(f"❌ {fn.__name__}: {e}")
    finally:
        Bd.cerrar()

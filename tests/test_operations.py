from michispotter import Gato, crear_gato, borrar_gato, Bd, editar_gato, listar_gatos
import pytest


def gato_prueba():
    gato = Gato()
    gato.raza = "Carey"
    gato.descripcion = "Tiene manchas marrones"
    gato.ubicacion = "Calle Porvera, Jerez de la Frontera, Cádiz."
    gato.apodo = "Manchitas"
    return gato


@pytest.fixture
def conexion():
    """
    Fixture creada para que permita la conexión a la base de datos.
    """
    # Usamos una base de datos en memoria para que cada test comience de cero, limpio y rápido.
    Bd.nombre = ":memory:"
    con = Bd.abrir()

    yield con

    Bd.cerrar()


def test_crear_gato(conexion):
    gato = gato_prueba()

    resultado = crear_gato(gato)
    assert resultado, "crear_gato ha devuelto False."
    assert gato.id > 0, "gato.id no tiene un valor correcto."

    cursor = conexion.cursor()
    resultado = cursor.execute(f"SELECT * FROM gatos WHERE id={gato.id}")
    numero_gatos = len(resultado.fetchall())

    assert numero_gatos == 1, "numero_gatos debe ser uno."


def test_borrar_gato(conexion):
    gato = gato_prueba()

    assert crear_gato(gato), "crear_gato no ha funcionado."
    assert borrar_gato(gato), "borrar_gato no ha funcionado."

    cursor = conexion.cursor()
    resultado = cursor.execute(f"SELECT COUNT(*) FROM gatos")
    numero_gatos = resultado.fetchone()[0]

    assert numero_gatos == 0, "numero_gatos debe ser cero."


def test_editar_gato(conexion):
    gato = gato_prueba()
    assert crear_gato(gato), "crear_gato no ha funcionado."

    gato.apodo = "Colmillitos"
    assert editar_gato(gato), "editar_gato no ha funcionado."

    cursor = conexion.cursor()
    resultado = cursor.execute(f"SELECT apodo FROM gatos")
    gatos = resultado.fetchall()

    assert len(gatos) == 1, "Debe de haber un solo gato."
    assert (
        gatos[0][0] == "Colmillitos"
    ), "El único gato que hay debe llamarse Colmillitos"


def test_listar_gatos(conexion):
    gato1 = gato_prueba()
    gato2 = gato_prueba()
    gato3 = gato_prueba()

    gato1.apodo = "Gatito"
    gato2.apodo = "Pelusa"
    gato3.apodo = "Pulga"

    assert crear_gato(gato1), "crear_gato para gato1 no ha funcionado."
    assert crear_gato(gato2), "crear_gato para gato2 no ha funcionado."
    assert crear_gato(gato3), "crear_gato para gato3 no ha funcionado."

    cursor = conexion.cursor()
    resultado = cursor.execute(f"SELECT apodo FROM gatos ORDER BY apodo")
    gatos = resultado.fetchall()

    assert len(gatos) == 3, "Debe de haber 3 gatos en la base de datos."
    assert gatos[0][0] == "Gatito", "El primer gato debe llamarse Gatito."
    assert gatos[1][0] == "Pelusa", "El segundo gato debe llamarse Pelusa."
    assert gatos[2][0] == "Pulga", "El tercer gato debe llamarse Pulga."

    gatos = listar_gatos()
    assert len(gatos) == 3, "Debe de haber 3 gatos devueltos por listar_gatos."
    assert isinstance(
        gatos[0], Gato
    ), "El primer valor de la lista debe ser de tipo Gato."
    assert isinstance(
        gatos[1], Gato
    ), "El segundo valor de la lista debe ser de tipo Gato."
    assert isinstance(
        gatos[2], Gato
    ), "El tercer valor de la lista debe ser de tipo Gato."

    assert gatos[0].apodo == "Gatito", "El primer gato debe apodarse Gatito."
    assert gatos[1].apodo == "Pelusa", "El segundo gato debe apodarse Pelusa."
    assert gatos[2].apodo == "Pulga", "El tercer gato debe apodarse Pulga."

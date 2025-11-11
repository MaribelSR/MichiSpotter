import pytest
import csv
from michispotter import (
    Gato,
    Bd,
    crear_gato,
    editar_gato,
    borrar_gato,
    listar_gatos,
    obtener_gato_por_id,
    buscar_gatos,
    exportar_a_csv,
)


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


def gato_prueba():
    gato = Gato()
    gato.raza = "Carey"
    gato.descripcion = "Tiene manchas marrones"
    gato.ubicacion = "Calle Porvera, Jerez de la Frontera, Cádiz"
    gato.apodo = "Manchitas"
    return gato


def test_crear_gato(conexion):
    """
    Prueba para comprobar crear_gato por ID.
    """
    gato = gato_prueba()

    resultado = crear_gato(gato)
    assert resultado, "crear_gato ha devuelto False."
    assert gato.id > 0, "gato.id no tiene un valor correcto."

    cursor = conexion.cursor()
    resultado = cursor.execute(f"SELECT * FROM gatos WHERE id={gato.id}")
    numero_gatos = len(resultado.fetchall())

    assert numero_gatos == 1, "numero_gatos debe ser uno."


def test_borrar_gato(conexion):
    """
    Prueba para comprobar borrar_gato ha funcionado.
    """
    gato = gato_prueba()

    assert crear_gato(gato), "crear_gato no ha funcionado."
    assert borrar_gato(gato), "borrar_gato no ha funcionado."

    cursor = conexion.cursor()
    resultado = cursor.execute(f"SELECT COUNT(*) FROM gatos")
    numero_gatos = resultado.fetchone()[0]

    assert numero_gatos == 0, "numero_gatos debe ser cero."


def test_editar_gato(conexion):
    """
    Prueba para corrobar que se edita el apodo de forma correcta.
    """
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
    ), "El único gato que hay debe llamarse Colmillitos."


def test_listar_gatos(conexion):
    """
    Prueba para corrobar que se listen todos los gatos de forma correcta.
    """
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


def test_obtener_gato_por_id(conexion):
    """
    Prueba donde se comprueba obtener_gato_por_id y devuelve None si no existe.
    """
    gato = gato_prueba()
    assert crear_gato(gato), "Fallo al crear el gato de prueba."

    # Prueba de un ID existente.
    gato_obtenido = obtener_gato_por_id(gato.id)

    assert gato_obtenido is not None, "El gato obtenido no debería de ser None."
    assert isinstance(gato_obtenido, Gato), "Debería devolver un objeto Gato."
    assert gato_obtenido.id == gato.id, "El ID del gato no coincide."
    assert gato_obtenido.apodo == "Manchitas", "El apodo del gato no coincide."

    # Prueba de un ID no existente
    gato_no_existente = obtener_gato_por_id(999)
    assert gato_no_existente is None, "Debería devolver None para un ID que no existe."


def test_buscar_gatos(conexion):
    """
    Prueba que la función de búsqueda encuentra los gatos correctos.
    """
    # Creamos varios gatos.
    gato1 = gato_prueba()
    gato1.apodo = "Manchitas"
    gato1.ubicacion = "Calle Porvera, Jerez"

    gato2 = gato_prueba()
    gato2.apodo = "Pelusa"
    gato2.raza = "Persa"
    gato2.ubicacion = "Calle Parque González Hontoria"

    gato3 = gato_prueba()
    gato3.apodo = "Bigotes"
    gato3.descripcion = "Duerme mucho en el parque"

    assert crear_gato(gato1), "Fallo al crear gato1."
    assert crear_gato(gato2), "Fallo al crear gato2."
    assert crear_gato(gato3), "Fallo al crear gato3."

    # Prueba de búsqueda por apodo.
    resultados1 = buscar_gatos("Manchitas")
    assert len(resultados1) == 1, "Debería de encontrar un gato por apodo."
    assert resultados1[0].apodo == "Manchitas", "El gato encontrado no es el correcto."

    # Prueba de búsqueda por ubicación (encuentra 2).
    resultados2 = buscar_gatos("Parque")
    assert len(resultados2) == 2, "Debería de encontrar 2 gatos por ¨Parque¨."

    # Prueba de búsqueda por raza.
    resultados3 = buscar_gatos("Persa")
    assert len(resultados3) == 1, "Debería de encontrar 1 gato por raza ¨Persa¨."
    assert resultados3[0].apodo == "Pelusa", "El gato encontrado no es ¨Pelusa¨."

    # Prueba de búsqueda sin resultados
    resultados4 = buscar_gatos("Inexistente123")
    assert len(resultados4) == 0, "No debería de encontrar resultados."


def test_exportar_a_csv(conexion, tmp_path):
    """
    Prueba que la exportación a CSV funciona correctamente, crea un archivo y escribe el contenido que se espera.

    Usa "conexión" para la BBDD en memoria.
    Usa "tmp_path" para crear un archivo temporal de forma segura.
    """
    # Se crea dos gatos para tener datos que exportar.
    gato1 = gato_prueba()
    gato1.apodo = "Manchitas"

    gato2 = gato_prueba()
    gato2.apodo = "Pelusa"
    gato2.raza = "Persa"

    assert crear_gato(gato1), "Fallo al crear el gato1"
    assert crear_gato(gato2), "Fallo al crear el gato2"

    # Definir la ruta del archivo. Uso de / para unir la carpeta temporal con el nombre del archivo.
    archivo_de_prueba = tmp_path / "test_gatos.csv"

    # Ruta completa del archivo de prueba.
    resultado_exportacion = exportar_a_csv(archivo_de_prueba)

    assert (
        resultado_exportacion == True
    ), "La función exportar_a_csv() debería devolver True."
    assert (
        archivo_de_prueba.exists()
    ), "El archivo CSV no se creó en la carpeta temporal."

    # Comprobación de que el contenido del archivo es correcto.
    try:
        # Se abre el archivo que se acaba de crear para leerlo.
        with open(archivo_de_prueba, "r", encoding="utf-8") as f:
            lector = csv.reader(f)
            # Se convierte el contenido en una lista de listas.
            datos_leidos = list(lector)

            # Se comprueba el número de filas (1 cabecera + 2 gatos creados de prueba anteriormente).
            assert (
                len(datos_leidos) == 3
            ), f"El CSV debería de tener 3 filas, pero tiene {len(datos_leidos)}."

            # Se comprueba la cabecera.
            cabecera_esperada = [
                "ID",
                "Apodo",
                "Raza",
                "Color",
                "Ubicación",
                "Descripción",
            ]
            assert (
                datos_leidos[0] == cabecera_esperada
            ), "La fila de cabecera no es correcta."

            # Se comprueba los datos con el apodo.
            assert (
                datos_leidos[1][1] == "Manchitas"
            ), "El apodo del primer gato no es 'Manchitas'."
            assert (
                datos_leidos[2][1] == "Pelusa"
            ), "El apodo del segundo gato no es 'Pelusa'."

    except Exception as e:
        # Si falla la lectura, se hace que el test falle con un mensaje claro.
        assert False, f"Error al leer el archivo CSV de prueba: {e}."

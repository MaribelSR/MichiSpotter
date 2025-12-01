# MichiSpotter 🐱

> Documenta y sigue a los michis de tu barrio

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![SQLite](https://img.shields.io/badge/database-SQLite-green.svg)
![Tests](https://img.shields.io/badge/tests-pytest-blue.svg)
![License](https://img.shields.io/badge/license-Apache%202.0-orange.svg)

**Sistema de registro y seguimiento de gatos callejeros**

MichiSpotter es una aplicación de consola para documentar y localizar gatos callejeros en tu comunidad. Permite registrar información detallada sobre cada gato avistado, facilitando el seguimiento y cuidado de colonias felinas.

## 🎯 Propósito del Proyecto

Este proyecto nace como una herramienta práctica para ayudar a comunidades y cuidadores de gatos a mantener un registro organizado de los felinos. Es también un proyecto de portfolio personal para demostrar habilidades en el desarrollo de software con Python.

## ✨ Características

- ✅ **Estructura de Paquete Modular**: Código separado en `models`, `database`, `operations` y `utils`.
- ✅ **Gestión de Base de Datos**: Persistencia local robusta usando **SQLite**.
- ✅ **Operaciones CRUD Completas**: Funciones para Crear, Leer, Actualizar y Borrar registros.
- ✅ **Búsqueda Avanzada**: Función para buscar gatos por apodo, raza o ubicación.
- ✅ **Exportación de Datos**: Generación de informes en formato CSV para análisis externo.
- ✅ **Pruebas Automatizadas**: Suite de tests completa usando **Pytest** y fixtures.

## 🛠️ Tecnologías

- **Python 3.x**
- **SQLite3**
- **Pytest** (para la suite de pruebas)
- **CSV & Pathlib** (para manejo de archivos)

## 📁 Estructura del Proyecto

La estructura sigue las mejores prácticas de un paquete de Python:

```
MichiSpotter/
│
├── michispotter/     # El paquete principal de la aplicación
│   ├── __init__.py     # Convierte la carpeta en un paquete
│   ├── database.py   # Gestión de la conexión (Clase Bd)
│   ├── models.py     # Definición del modelo (Clase Gato)
│   ├── operations.py # Funciones CRUD (crear_gato, etc.)
│   └── utils.py      # Funciones auxiliares (buscar_gatos, exportar_a_csv, etc.)
│
├── tests/            # Pruebas automatizadas
│   └── test_operations.py
│
├── .gitignore        # Archivos a ignorar por Git
├── README.md         # Este archivo
└── gatos.sqlite3     # Base de datos (generada al ejecutar)
```

## 🚀 Instalación y Uso

### Requisitos Previos

- Python 3.7 o superior
- Git

### Instalación

1.  **Clonar el repositorio:**

    ```bash
    git clone [https://github.com/MaribelSR/MichiSpotter.git](https://github.com/MaribelSR/MichiSpotter.git)
    cd MichiSpotter
    ```

2.  **(Opcional pero recomendado) Crear un entorno virtual:**

    ```bash
    python -m venv venv
    ```

    _En Windows:_ `.\venv\Scripts\activate`
    _En macOS/Linux:_ `source venv/bin/activate`

3.  **Instalar el paquete en modo editable:**
    El modo editable (`-e`) hace que tus cambios en el código se reflejen al instante.
    ```bash
    pip install -e .
    ```

### Uso Básico (Ejemplo en un script)

```python
# Importa las funciones y clases desde el paquete
from michispotter import Gato, Bd, crear_gato, listar_gatos, buscar_gatos, exportar_a_csv

# 1. Crear un nuevo registro de gato
gato_nuevo = Gato()
gato_nuevo.raza = "Común Europeo"
gato_nuevo.descripcion = "Atigrado, muy amigable"
gato_nuevo.ubicacion = "Patio interior, Calle Larga"
gato_nuevo.apodo = "Tigre"
gato_nuevo.color = "Naranja y blanco"

# Guardar en la base de datos
crear_gato(gato_nuevo)
print(f"¡{gato_nuevo.apodo} ha sido registrado!")

# 2. Listar todos los gatos
print("\n--- Listado de Gatos ---")
gatos = listar_gatos()
for g in gatos:
    print(f"ID {g.id}: {g.apodo} ({g.raza})")

# 3. Buscar un gato
print("\n--- Búsqueda de 'Tigre' ---")
gatos_encontrados = buscar_gatos("Tigre")
for g in gatos_encontrados:
    print(f"Encontrado: {g.apodo} en {g.ubicacion}")

# 4. Exportar listado
if exportar_a_csv("mis_gatos.csv"):
    print("\n✅ Archivo 'mis_gatos.csv' generado correctamente.")

# No olvides cerrar la conexión al final de tu app
Bd.cerrar()
```

## 🧪 Ejecutar Tests

Este proyecto usa `pytest` para las pruebas.

1.  **Instalar pytest (si no lo tienes):**

    ```bash
    pip install pytest
    ```

2.  **Ejecutar la suite de tests:**
    Desde la carpeta raíz (`MichiSpotter/`), simplemente ejecuta:
    ```bash
    pytest
    ```
    `pytest` encontrará y ejecutará automáticamente todos los tests en la carpeta `tests/`.

## 🗺️ Roadmap (Plan de desarrollo)

- [x] Estructura base del proyecto (CRUD)
- [x] Implementar Pruebas con Pytest
- [x] Añadir función de Búsqueda (`buscar_gatos`)
- [x] Exportación de datos (CSV, JSON)
- [ ] Interfaz gráfica (GUI con Tkinter o web con Flask)
- [ ] Subida de fotografías de cada gato
- [ ] API REST para acceso remoto

## 🤝 Contribuciones

Este es un proyecto de aprendizaje personal, pero las sugerencias y comentarios son bienvenidos. Si encuentras algún bug o tienes ideas para mejorarlo, no dudes en abrir un issue o enviar un pull request.

## 📝 Licencia

Este proyecto está licenciado bajo la Licencia Apache 2.0. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## 👤 Autor

Desarrollado por **María Isabel Salvador Rufo** como proyecto de portfolio para demostrar habilidades en:

- **Programación Orientada a Objetos (POO)** en Python.
- Diseño de **paquetes modulares** y mantenibles.
- Gestión de bases de datos con **SQLite** (operaciones CRUD completas).
- **Testing automatizado** con **Pytest**, incluyendo `fixtures` personalizadas (BBDD en memoria) y pruebas de efectos secundarios de E/S (`tmp_path`).
- Refactorización y mantenimiento de código limpio.

---

**Estado del proyecto**: 🚧 En desarrollo activo

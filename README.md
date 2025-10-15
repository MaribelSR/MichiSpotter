# MichiSpotter 🐱

**Sistema de registro y seguimiento de gatos callejeros**

MichiSpotter es una aplicación para documentar y localizar gatos callejeros en tu comunidad. Permite registrar información detallada sobre cada gato avistado, incluyendo su raza, características físicas, ubicación y apodo, facilitando el seguimiento y cuidado de colonias felinas.

## 🎯 Propósito del Proyecto

Este proyecto nace como una herramienta práctica para ayudar a comunidades, voluntarios y cuidadores de gatos callejeros a mantener un registro organizado de los felinos que encuentran. Es ideal para:

- Voluntarios de colonias felinas
- Personas que alimentan gatos callejeros
- Organizaciones de rescate animal
- Comunidades de vecinos que cuidan de gatos del barrio

## ✨ Características Actuales

- ✅ **Registro de gatos**: Almacena información completa sobre cada gato
- ✅ **Base de datos SQLite**: Persistencia local de datos
- ✅ **CRUD completo**: Crear, leer, actualizar y eliminar registros
- ✅ **Tests unitarios**: Suite de pruebas para garantizar funcionalidad
- ✅ **Listado ordenado**: Visualización alfabética por apodo

## 🛠️ Tecnologías

- **Python 3.x**
- **SQLite3**: Base de datos ligera y sin configuración
- **Testing nativo de Python**: Suite de pruebas personalizada

## 📁 Estructura del Proyecto

```
MichiSpotter/
│
├── main.py           # Lógica principal y gestión de base de datos
├── test.py           # Suite de tests unitarios
├── gatos.sqlite3     # Base de datos (generada automáticamente)
├── LICENSE           # Licencia Apache 2.0
└── README.md         # Este archivo
```

## 🚀 Instalación y Uso

### Requisitos Previos

- Python 3.7 o superior

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/MaribelSR/MichiSpotter.git
cd MichiSpotter

# No requiere instalación de dependencias adicionales
```

### Uso Básico

```python
from main import Gato, crear_gato, listar_gatos, Bd

# Crear un nuevo registro de gato
gato = Gato()
gato.raza = "Carey"
gato.descripcion = "Pelaje tricolor, orejas grandes"
gato.ubicacion = "Parque Central, banco cerca de la fuente"
gato.apodo = "Manchitas"

# Guardar en la base de datos
crear_gato(gato)

# Listar todos los gatos registrados
gatos = listar_gatos()
for g in gatos:
    print(f"{g.apodo} - {g.raza} - {g.ubicacion}")

# No olvides cerrar la conexión
Bd.cerrar()
```

### Ejecutar Tests

```bash
python test.py
```

## 📊 Modelo de Datos

```python
class Gato:
    id: int              # Identificador único (autoincremental)
    raza: str            # Raza o tipo de gato
    descripcion: str     # Características físicas distintivas
    ubicacion: str       # Lugar donde se avistó
    apodo: str           # Nombre o apodo del gato
```

## 🧪 Tests

El proyecto incluye una suite completa de tests que valida:

- ✅ Creación de registros
- ✅ Borrado de registros
- ✅ Edición de información
- ✅ Listado y ordenamiento

Cada test se ejecuta en una base de datos en memoria para evitar efectos secundarios.

## 🗺️ Roadmap

### Próximas Funcionalidades

- [ ] Interfaz gráfica (GUI con Tkinter o web con Flask)
- [ ] Búsqueda y filtrado de gatos por ubicación o características
- [ ] Subida de fotografías de cada gato
- [ ] Historial de avistamientos con fechas
- [ ] Exportación de datos (CSV, JSON)
- [ ] Sistema de notificaciones para nuevos avistamientos
- [ ] Mapa interactivo con ubicaciones
- [ ] API REST para acceso remoto
- [ ] Autenticación de usuarios

## 🤝 Contribuciones

Este es un proyecto de aprendizaje personal, pero las sugerencias y comentarios son bienvenidos. Si encuentras algún bug o tienes ideas para mejorarlo, no dudes en abrir un issue o enviar un pull request.

## 📝 Licencia

Este proyecto está licenciado bajo la Licencia Apache 2.0. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## 👤 Autor

Desarrollado por María Isabel Salvador Rufo como proyecto de portfolio para demostrar habilidades en:

- Programación orientada a objetos en Python
- Gestión de bases de datos con SQLite
- Testing y calidad de código
- Diseño de APIs limpias y mantenibles

---

**Estado del proyecto**: 🚧 En desarrollo activo

---

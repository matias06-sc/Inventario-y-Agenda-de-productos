# Trabajo Inventario y Agenda de Productos
Sistema web desarrollado con Django que permite la gestión de productos en inventario y administración de agenda, implementando operaciones CRUD (crear, visualizar, actualizar y eliminar), con almacenamiento en base de datos y una interfaz sencilla basada en HTML y CSS.

## 🎯 Product Backlog
Desarrollar un sistema que permita:
- Registrar productos en inventario (nombre, stock, categoría, precio).
- Administrar una agenda con registros organizados (eventos o tareas).
- Visualizar la lista de productos y eventos en tablas dinámicas.
- Actualizar información de productos y agenda mediante formularios.
- Eliminar registros de manera segura con confirmación.
- Aplicar filtros y parámetros de búsqueda en el inventario.
- Proporcionar una interfaz clara, usable y consistente.
- Desplegar y validar avances en GitHub asegurando correcto funcionamiento.

## 🎯 Sprint Goal
El objetivo del sprint es implementar un sistema de inventario y agenda en Django, con funcionalidades CRUD completas para productos y eventos, validaciones correctas, almacenamiento en base de datos y una interfaz web intuitiva.

## 👥 Roles Scrum
| Rol            | Integrante           | Función principal                                                                                                                         |
|----------------|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scrum Master   | Matias Sicha    | Facilita el marco de trabajo Scrum, asegura la correcta aplicación de la metodología ágil y elimina impedimentos.      |
| Product Owner  | Rodrigo Guerra      | Define los requisitos del sistema, prioriza el backlog y valida que el inventario y la agenda cumplan con los objetivos del proyecto.      |
| Developer 2    | Daniel Torres      | Desarrolla la interfaz de usuario en HTML y CSS, asegurando un diseño claro y usable para la gestión de inventario y agenda.   |
| Developer 3    | Juan Solis    | Desarrolla la lógica del módulo de agenda en Django, integrando las vistas y modelos para registrar y gestionar eventos. |
| Developer 4    | Josue Castillo  | Implementa la lógica del sistema en Django para el módulo de inventario, gestionando los procesos CRUD y validaciones.     |
| Developer 5    | Kevin Yupanqui  | Diseña y gestiona la base de datos en MySQL, adaptando la estructura de tablas de productos y agenda, y asegurando integridad de los datos. |

## 🎯 Características Principales
### ✅ **Funcionalidades CRUD**
 - Crear, listar, editar y eliminar productos en el inventario.
 - Crear, listar, editar y eliminar registros en la agenda.
 - Validación de datos mediante formularios de Django.

### ✅ **Interfaz de Usuario**
 - Formularios claros con validación automática.
 - Listados organizados en tablas.
 - Plantillas HTML reutilizables para coherencia visual.

### ✅ **Características Técnicas**
 - Backend: Django 4.x
 - Base de datos: SQLite (configuración por defecto).
 - Frontend: HTML + CSS personalizados.
 - Arquitectura modular con apps independientes (agenda, inventario).

## 🏗️ Estructura del Proyecto

```
Inventario-y-Agenda-de-productos/
├── Trabajo/
│   ├── agenda/               # Aplicación de agenda
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py         # Modelo de agenda
│   │   ├── views.py          # Vistas de la agenda
│   │   ├── tests.py
│   │   ├── migrations/
│   │   └── templates/        # Plantillas HTML (agenda)
│   ├── inventario/           # Proyecto Django principal
│   │   ├── asgi.py
│   │   ├── settings.py       # Configuración principal
│   │   ├── urls.py           # Rutas principales
│   │   ├── wsgi.py
│   │   └── __init__.py
│   ├── manage.py             # Script de gestión Django
│   └── db.sqlite3            # Base de datos SQLite
└── README.md                 # Documentación
```

## 🔗 Enlace del Trello
- https://trello.com/invite/b/680031ae4fc524088e4ac644/ATTI3da99a4d8352f2d05bff4672ed51ae608E2358CF/django-control-de-productos

## 🎥 Video explicativo (entregado por Drive):
- Nombre de la carpeta: Inventario y Agenda de Productos
- Contenido:
  - 🎥 Video
  - 📄 Documentacion
  - 🔗 Link del Drive: https://drive.google.com/drive/folders/1ikd9IJ-VVtOSj0DPwzJwQjCGBaBd_GTK?usp=drive_link

## 🚀 Instalación y Configuración

### 1. **Clonar el repositorio**
```bash
git clone <URL_DEL_REPOSITORIO>
cd Inventario-y-Agenda-de-productos
```

### 2. **Crear entorno virtual**
```bash
python -m venv venv
```

### 3. **Activar entorno virtual**
```bash
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 4. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

### 5. **Configurar la base de datos**
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. **Ejecutar el servidor**
```bash
python manage.py runserver
```

## 📝 Historias de Usuario y Criterios de Aceptación

📌 **HU-01: Registrar Producto**

**Descripción:**
Como usuario del sistema, quiero poder registrar un nuevo producto con su categoría, precio, stock, prioridad, fecha límite y estado, para mantener actualizada la agenda de productos y planificar su gestión.

**Criterios de aceptación:**
 - Se puede acceder al formulario sin errores.
 - El sistema guarda correctamente los datos en la base de datos.
 - Los mensajes de confirmación y error aparecen en el momento correcto.
 - El nuevo producto aparece reflejado en la lista general inmediatamente.

📌 **HU-02: Consultar Productos**

**Descripción:**
Como usuario del sistema, quiero poder visualizar una lista de productos registrados con todos sus datos, para tener control sobre el inventario y su agenda de seguimiento.

**Criterios de aceptación:**
 - La lista muestra todos los productos registrados.
 - Cada columna refleja correctamente la información del producto (nombre, categoría, precio, stock, prioridad, fecha límite, estado).
 - Si se añade, edita o elimina un producto, la lista se actualiza en tiempo real o tras refrescar la vista.

📌 **HU-03: Actualizar Producto**

**Descripción:**
Como usuario del sistema, quiero poder editar los datos de un producto existente (precio, stock, prioridad, fecha límite o estado), para mantener la información al día.

**Criterios de aceptación:**
 - El formulario de edición muestra los datos actuales del producto.
 - Los cambios se guardan en la base de datos correctamente.
 - Los mensajes de error y confirmación aparecen en el momento oportuno.
 - La lista refleja el cambio inmediatamente después de la edición.

📌 **HU-04: Eliminar Producto**

**Descripción:**
Como usuario del sistema, quiero poder eliminar un producto de la agenda, para mantener la base de datos depurada y actualizada.

**Criterios de aceptación:**
 - El sistema solicita confirmación antes de eliminar.
 - El producto desaparece de la base de datos tras eliminarse.
 - El producto eliminado no aparece en la lista de productos.
 - El sistema muestra un mensaje de confirmación al usuario.

📌 **HU-05: Filtrar y Buscar Productos**

**Descripción:**
Como usuario del sistema, quiero poder aplicar filtros y realizar búsquedas en la lista de productos, para encontrar rápidamente registros según mis necesidades.

**Criterios de aceptación:**
 - Los filtros funcionan de forma independiente y combinada.
 - La búsqueda devuelve solo los resultados que coinciden con el criterio.
 - Al limpiar los filtros, vuelve a mostrarse la lista completa.
 - El sistema no presenta errores al aplicar o quitar filtros.

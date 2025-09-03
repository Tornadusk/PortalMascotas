# Portal de Mascotas 🐾

Un portal web desarrollado en Django para la gestión y adopción de mascotas.

## 📋 Descripción

Portal de Mascotas es una aplicación web que permite:
- **Gestión de mascotas**: Registro y administración de información de mascotas
- **Sistema de adopciones**: Proceso completo de adopción de mascotas
- **Filtros avanzados**: Búsqueda y filtrado de mascotas por diferentes criterios
- **Blog**: Artículos y noticias relacionadas con el cuidado de mascotas

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django 5.2.6
- **Base de datos**: SQLite (desarrollo)
- **Frontend**: HTML, CSS, JavaScript
- **Python**: 3.11+

## 📦 Instalación

### Prerrequisitos

- Python 3.11 o superior
- pip (gestor de paquetes de Python)
- Git

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/Tornadusk/PortalMascotas.git
   cd PortalMascotas
   ```

2. **Crear un entorno virtual**
   ```bash
   python -m venv venv
   ```

3. **Activar el entorno virtual**
   
   **En Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **En Linux/Mac:**
   ```bash
   source venv/bin/activate
   ```

4. **Instalar dependencias**
   ```bash
   pip install django
   ```

5. **Aplicar migraciones**
   ```bash
   python manage.py migrate
   ```

6. **Crear un superusuario (opcional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Ejecutar el servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

8. **Acceder a la aplicación**
   
   Abre tu navegador y ve a: `http://127.0.0.1:8000/`

## 🏗️ Estructura del Proyecto

```
portal_mascotas/
├── registro_mascotas/     # App para registro de mascotas
├── solicitud_adopcion/    # App para solicitudes de adopción
├── filtros/               # App para filtros y búsquedas
├── blog/                  # App para blog y artículos
├── portal_mascotas/       # Configuración del proyecto
│   ├── settings.py        # Configuraciones
│   ├── urls.py            # URLs principales
│   └── wsgi.py            # Configuración WSGI
└── manage.py              # Script de administración de Django
```

## 🚀 Comandos Útiles

### Desarrollo
```bash
# Ejecutar servidor de desarrollo
python manage.py runserver

# Verificar configuración
python manage.py check

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate
```

### Administración
```bash
# Acceder al panel de administración
python manage.py runserver
# Luego ir a: http://127.0.0.1:8000/admin/

# Crear superusuario
python manage.py createsuperuser
```

## 📱 Apps del Proyecto

### 🐕 Registro de Mascotas
- Registro de mascotas
- Información detallada (edad, raza, tamaño, etc.)
- Galería de fotos
- Estado de adopción

### 🏠 Solicitud de Adopción
- Proceso de adopción
- Formularios de solicitud de adopción
- Seguimiento de adopciones
- Historial de adopciones

### 🔍 Filtros
- Búsqueda por raza
- Filtro por edad
- Filtro por tamaño
- Filtro por ubicación

### 📝 Blog
- Artículos sobre cuidado de mascotas
- Noticias del refugio
- Consejos veterinarios
- Historias de adopción exitosas

## 🔧 Configuración

### Variables de Entorno

Para producción, configura las siguientes variables:

```python
# En settings.py
DEBUG = False
ALLOWED_HOSTS = ['tu-dominio.com']
SECRET_KEY = 'tu-clave-secreta-aqui'
```

### Base de Datos

El proyecto está configurado para usar SQLite por defecto. Para producción, puedes cambiar a PostgreSQL o MySQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portal_mascotas',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👥 Autores

- **Tornadusk** - *Desarrollo inicial* - [GitHub](https://github.com/Tornadusk)

## 📞 Contacto

Si tienes preguntas o sugerencias, no dudes en contactarnos:

- GitHub: [@Tornadusk](https://github.com/Tornadusk)
- Email: [tu-email@ejemplo.com]

## 🙏 Agradecimientos

- Django Software Foundation
- Comunidad de Python
- Todos los contribuidores del proyecto

---

⭐ ¡No olvides darle una estrella al proyecto si te gusta!

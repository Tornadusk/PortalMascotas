# Portal de Mascotas 🐾

Un portal web desarrollado en Django para la gestión y adopción de mascotas.

## 📋 Descripción

Portal de Mascotas es una aplicación web que permite:
- **Gestión de mascotas**: Registro y administración de información de mascotas
- **Sistema de adopciones**: Proceso completo de adopción de mascotas
- **Filtros avanzados**: Búsqueda y filtrado de mascotas por diferentes criterios
- **Blog**: Artículos y noticias relacionadas con el cuidado de mascotas

### ✨ Características Principales

- **🔍 Sistema de Filtros Inteligente**: Búsqueda avanzada con múltiples criterios
- **💾 Filtros Guardados**: Los usuarios pueden guardar y reutilizar filtros personalizados
- **📊 Historial de Búsquedas**: Registro completo de todas las búsquedas realizadas
- **✅ Validaciones Automáticas**: Prevención de solicitudes duplicadas o inválidas
- **🎯 Constantes Centralizadas**: Sistema sin duplicación de datos
- **🔗 Relaciones Complejas**: Modelos interconectados con integridad referencial
- **📱 Interfaz Intuitiva**: Diseño centrado en la experiencia del usuario

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django 5.2.6
- **Base de datos**: SQLite (desarrollo)
- **Frontend**: HTML, CSS, JavaScript
- **Python**: 3.11+
- **Arquitectura**: Modelo-Vista-Template (MVT)
- **ORM**: Django ORM con relaciones complejas
- **Validaciones**: Validaciones automáticas en modelos
- **Sistema de constantes**: Centralización de opciones compartidas

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

## 🏗️ Arquitectura del Sistema

### 📊 Modelos de Datos

#### 🐕 Modelo Mascota (`registro_mascotas`)
```python
# Campos principales
- nombre: Nombre de la mascota
- tipo: Especie (perro, gato, otro)
- raza: Raza específica
- edad: Edad en meses
- sexo: Macho o hembra
- descripcion: Descripción detallada
- ubicacion: Ciudad o ubicación
- foto: Imagen de la mascota
- estado: Disponible, adoptado, reservado
- responsable: Usuario que registró la mascota
- fecha_registro: Fecha de registro

# Métodos de filtrado
- filtrar_por_especie(tipo)
- filtrar_por_edad(edad_min, edad_max)
- filtrar_por_ubicacion(ubicacion)
- filtrar_combinado(tipo, edad_min, edad_max, ubicacion)
```

#### 🏠 Modelo SolicitudAdopcion (`solicitud_adopcion`)
```python
# Campos principales
- usuario: Usuario que solicita la adopción
- mascota: Mascota a adoptar
- mensaje: Motivo de la adopción
- estado: Pendiente, aprobada, rechazada, cancelada
- fecha_solicitud: Fecha de la solicitud
- fecha_respuesta: Fecha de respuesta
- respuesta: Respuesta del responsable

# Validaciones automáticas
- Un usuario no puede solicitar la misma mascota dos veces
- Solo mascotas disponibles pueden ser solicitadas
- Un usuario no puede solicitar adoptar su propia mascota
```

#### 🔍 Modelo FiltroBusqueda (`filtros`)
```python
# Filtros disponibles
- tipo: Especie de mascota
- sexo: Sexo de la mascota
- edad_min/edad_max: Rango de edad
- ubicacion: Ubicación geográfica
- raza: Raza específica
- texto_busqueda: Búsqueda de texto
- incluir_descripcion: Incluir descripción en búsqueda

# Funcionalidades
- aplicar_filtro(): Ejecuta la búsqueda
- get_criterios_activos(): Muestra filtros aplicados
- Filtros favoritos y guardados
- Historial de búsquedas
```

### 🎯 Sistema de Constantes Centralizadas

El proyecto utiliza un sistema de constantes centralizadas en `portal_mascotas/constantes.py` para evitar duplicación de datos:

```python
# Tipos de mascotas
TIPOS_MASCOTA = [('perro', 'Perro'), ('gato', 'Gato'), ('otro', 'Otro')]

# Sexos
SEXOS = [('macho', 'Macho'), ('hembra', 'Hembra')]

# Estados de mascotas
ESTADOS_MASCOTA = [('disponible', 'Disponible'), ('adoptado', 'Adoptado'), ('reservado', 'Reservado')]

# Estados de solicitudes
ESTADOS_SOLICITUD = [('pendiente', 'Pendiente'), ('aprobada', 'Aprobada'), ('rechazada', 'Rechazada'), ('cancelada', 'Cancelada')]

# Rangos de edad comunes
RANGOS_EDAD = [(0, 6, 'Cachorro'), (6, 12, 'Joven'), (12, 24, 'Adulto joven'), (24, 84, 'Adulto'), (84, 999, 'Senior')]

# Ubicaciones comunes
UBICACIONES_COMUNES = ['Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena', ...]

# Razas comunes
RAZAS_PERROS = ['Labrador', 'Golden Retriever', 'Pastor Alemán', 'Bulldog', ...]
RAZAS_GATOS = ['Persa', 'Siamés', 'Maine Coon', 'British Shorthair', ...]
```

### 🔄 Relaciones entre Modelos

```
User (Django Auth)
├── mascotas_registradas (Mascota) → responsable
├── solicitudes_adopcion (SolicitudAdopcion) → usuario
├── filtros_busqueda (FiltroBusqueda) → usuario
└── historial_busquedas (HistorialBusqueda) → usuario

Mascota
├── solicitudes (SolicitudAdopcion) → mascota
└── Usado por FiltroBusqueda.aplicar_filtro()

FiltroBusqueda
└── historial_busquedas (HistorialBusqueda) → filtro_aplicado
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

### 🔍 Sistema de Filtros
- **Filtros básicos**: Por especie (perro, gato, otro), sexo, edad y ubicación
- **Filtros avanzados**: Por raza específica, búsqueda de texto en nombre/descripción
- **Filtros guardados**: Los usuarios pueden guardar y reutilizar filtros personalizados
- **Historial de búsquedas**: Registro de todas las búsquedas realizadas
- **Filtros combinados**: Aplicar múltiples criterios simultáneamente
- **Filtros favoritos**: Marcar filtros como favoritos para acceso rápido

### 📝 Blog
- Artículos sobre cuidado de mascotas
- Noticias del refugio
- Consejos veterinarios
- Historias de adopción exitosas

## 💡 Ejemplos de Uso

### 🔍 Uso del Sistema de Filtros

```python
from registro_mascotas.models import Mascota
from filtros.models import FiltroBusqueda

# Filtrar por especie
perros = Mascota.filtrar_por_especie('perro')
gatos = Mascota.filtrar_por_especie('gato')

# Filtrar por edad
cachorros = Mascota.filtrar_por_edad(edad_max=12)  # Menos de 1 año
adultos = Mascota.filtrar_por_edad(edad_min=12, edad_max=84)  # 1-7 años

# Filtrar por ubicación
mascotas_bogota = Mascota.filtrar_por_ubicacion('Bogotá')

# Filtro combinado
perros_jovenes_bogota = Mascota.filtrar_combinado(
    tipo='perro',
    edad_max=24,
    ubicacion='Bogotá'
)

# Crear y usar filtro personalizado
filtro = FiltroBusqueda.objects.create(
    nombre_filtro="Perros jóvenes en Bogotá",
    tipo='perro',
    edad_max=24,
    ubicacion='Bogotá',
    es_favorito=True
)

# Aplicar filtro guardado
resultados = filtro.aplicar_filtro()
print(f"Encontrados {resultados.count()} perros jóvenes en Bogotá")

# Ver criterios activos
criterios = filtro.get_criterios_activos()
print("Criterios:", criterios)
```

### 🏠 Gestión de Solicitudes de Adopción

```python
from solicitud_adopcion.models import SolicitudAdopcion

# Crear solicitud de adopción
solicitud = SolicitudAdopcion.objects.create(
    usuario=usuario,
    mascota=mascota,
    mensaje="Me encantaría adoptar esta mascota porque..."
)

# Aprobar solicitud
solicitud.estado = 'aprobada'
solicitud.respuesta = "¡Felicidades! Tu solicitud ha sido aprobada."
solicitud.fecha_respuesta = timezone.now()
solicitud.save()

# Cambiar estado de la mascota
mascota.estado = 'adoptado'
mascota.save()
```

### 📊 Consultas Avanzadas

```python
# Mascotas más populares (más solicitudes)
from django.db.models import Count
mascotas_populares = Mascota.objects.annotate(
    num_solicitudes=Count('solicitudes')
).order_by('-num_solicitudes')[:10]

# Usuarios más activos en adopciones
usuarios_activos = User.objects.annotate(
    num_solicitudes=Count('solicitudes_adopcion')
).order_by('-num_solicitudes')[:10]

# Estadísticas por tipo de mascota
from django.db.models import Count
estadisticas = Mascota.objects.values('tipo').annotate(
    total=Count('id'),
    disponibles=Count('id', filter=models.Q(estado='disponible'))
)
```

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

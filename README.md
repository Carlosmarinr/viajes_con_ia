# 🌋 Viajes por Venezuela

Bienvenido a **Viajes por Venezuela**, un blog web desarrollado en Python con Django para explorar destinos turísticos del país. La aplicación permite descubrir lugares emblemáticos, interactuar con otros usuarios, dejar comentarios, recomendar o no recomendar destinos, y gestionar publicaciones con autenticación y permisos.

![Django](https://img.shields.io/badge/Django-6.0.6-green)
![Python](https://img.shields.io/badge/Python-3.13-blue)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Características principales

- Blog temático sobre destinos turísticos de Venezuela
- CRUD completo para destinos
- Autenticación de usuarios con login y registro
- Permisos para editar y eliminar publicaciones
- Sistema de votos tipo “like” y “dislike”
- Comentarios por destino
- Diseño moderno con CSS y animaciones
- Carga de imágenes para publicaciones, reservada al usuario administrador
- Datos iniciales precargados para mostrar el proyecto al instante

---

## 🧱 Tecnologías utilizadas

- Python 3.13
- Django 6.0.6
- Pillow para manejo de imágenes
- SQLite como base de datos local
- HTML, CSS y Django Templates

---

## 📁 Estructura del proyecto

```text
viajes_IA/
│
├── blog/
│   ├── management/
│   │   └── commands/
│   │       └── seed_destinations.py
│   ├── migrations/
│   ├── static/
│   │   └── blog/
│   ├── templates/
│   │   └── blog/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── viajes_blog/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🚀 Requisitos previos

Asegúrate de tener instalado:

- Python 3.10 o superior
- pip
- Git (opcional, pero recomendado)

---

## 🛠️ Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd viajes_IA
```

### 2. Crear entorno virtual

En Windows:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

En Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Cargar datos iniciales

```bash
python manage.py seed_destinations
```

### 6. Ejecutar el servidor

```bash
python manage.py runserver
```

Abre tu navegador en:

```text
http://127.0.0.1:8000/
```

---

## 👤 Usuarios de prueba

El proyecto ya incluye un usuario administrador para pruebas:

- Usuario: `admin`
- Contraseña: `admin123`

También puedes crear usuarios nuevos desde la interfaz web.

---

## 🧪 Ejecutar pruebas

```bash
python manage.py test
```

---

## 🧩 Funcionalidades del sistema

### Destinos
- Crear, ver, editar y eliminar destinos
- Cada destino contiene:
  - título
  - resumen
  - descripción
  - ubicación
  - imagen (solo administrador)
  - estado destacado

### Interacción social
- Los usuarios pueden comentar en cada destino
- Los usuarios pueden votar si lo recomiendan o no
- El sistema evita votos duplicados por usuario

### Permisos
- Solo usuarios autenticados pueden crear y comentar
- Solo el autor, administrador o superusuario pueden editar o eliminar un destino

---

## 🖼️ Gestión de imágenes

Las imágenes pueden agregarse desde el panel administrativo o mediante formularios de creación de destinos.

Importante:
- Solo el usuario administrador puede subir imágenes
- Si un usuario normal crea un destino, la imagen se deja vacía por defecto

---

## 🎨 Diseño

La interfaz fue pensada con una estética visual inspirada en:

- paisajes naturales
- cielos atardecidos
- colores tierra, azul y naranja
- animaciones suaves para una experiencia más atractiva

---

## 📌 Notas adicionales

Este proyecto está pensado como una base sólida para un blog de viajes, pero puede ampliarse con:

- categorías por región
- buscador de destinos
- sistema de favoritos
- calendario de viajes
- panel administrativo más avanzado
- despliegue en producción

---

## 📝 Licencia

Este proyecto se distribuye con fines educativos y de demostración.

---

## 🤝 Contribuciones

Si deseas mejorar el proyecto, puedes hacer fork, trabajar en una rama nueva y enviar tus cambios mediante pull request.

---

Hecho con ❤️ para explorar Venezuela desde la web.

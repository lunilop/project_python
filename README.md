# Pet-Shop API 🐾

Este es un proyecto **Pet-Shop** desarrollado con **FastAPI** y **MongoDB**, diseñado para gestionar usuarios y productos. El proyecto implementa operaciones CRUD para usuarios y productos, así como autenticación (registro y login). Además, está preparado para futuras funcionalidades como la gestión de promociones y órdenes, actualmente comentadas.

## 🚀 Características

### Funcionalidades implementadas:
- **Gestión de Usuarios**:
  - Registro de usuarios con validación.
  - Inicio de sesión con autenticación JWT.
  - Edición y eliminación de usuarios.
  
- **Gestión de Productos**:
  - Creación, visualización, edición y eliminación de productos.
  
- **Autenticación segura**:
  - Manejo de JWT para proteger las rutas y recursos.

### Funcionalidades futuras:
- **Gestión de Promociones**: Implementación futura para descuentos y ofertas.
- **Gestión de Órdenes**: Funcionalidad planificada para manejar pedidos de clientes.

## 🛠️ Tecnologías utilizadas

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Base de datos**: [MongoDB](https://www.mongodb.com/)
- **Gestión de dependencias**: [Poetry](https://python-poetry.org/)
- **Validación de datos**: Pydantic
- **Autenticación**: FastAPI JWT
- **Servidor web**: Uvicorn

## 📂 Estructura del proyecto

```
pet_shop/
├── api/               # Rutas y lógica principal de la API
├── static/            # Archivos estáticos (CSS, JS, imágenes)
├── templates/         # Plantillas HTML (para vistas si es necesario)
├── main.py            # Punto de entrada de la aplicación
├── pyproject.toml     # Configuración de Poetry y dependencias
├── requirements.txt   # Alternativa de dependencias en formato pip
├── .env.example       # Ejemplo de configuración de variables de entorno
```

## ⚙️ Configuración del entorno

### 1. Clonar el repositorio
```bash
git clone git@github.com:lunilop/proyecto_python.git
cd proyecto_python
```

### 2. Configurar variables de entorno
Renombrar el archivo `.env.example` a `.env` y completar los valores necesarios:
```bash
cp .env.example .env
```

### 3. Instalar dependencias
Usa **Poetry** para instalar las dependencias del proyecto:
```bash
poetry install
```

Si prefieres usar `pip`, instala las dependencias desde el archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación
Inicia el servidor local con:
```bash
poetry run uvicorn main:app --reload
```

La API estará disponible en: `http://127.0.0.1:8000`.

## 📋 Endpoints principales

### Usuarios
- `POST /register`: Registrar un nuevo usuario.
- `POST /login`: Iniciar sesión y obtener un token JWT.
- `GET /users`: Listar usuarios (requiere autenticación).
- # Pet-Shop API 🐾

Este es un proyecto **Pet-Shop** desarrollado con **FastAPI** y **MongoDB**, diseñado para gestionar usuarios y productos. El proyecto implementa operaciones CRUD para usuarios y productos, así como autenticación (registro y login). Además, está preparado para futuras funcionalidades como la gestión de promociones y órdenes, actualmente comentadas.

## 🚀 Características

### Funcionalidades implementadas:
- **Gestión de Usuarios**:
  - Registro de usuarios con validación.
  - Inicio de sesión con autenticación JWT.
  - Edición y eliminación de usuarios.
  
- **Gestión de Productos**:
  - Creación, visualización, edición y eliminación de productos.
  
- **Autenticación segura**:
  - Manejo de JWT para proteger las rutas y recursos.

### Funcionalidades futuras:
- **Gestión de Promociones**: Implementación futura para descuentos y ofertas.
- **Gestión de Órdenes**: Funcionalidad planificada para manejar pedidos de clientes.

## 🛠️ Tecnologías utilizadas

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Base de datos**: [MongoDB](https://www.mongodb.com/)
- **Gestión de dependencias**: [Poetry](https://python-poetry.org/)
- **Validación de datos**: Pydantic
- **Autenticación**: FastAPI JWT
- **Servidor web**: Uvicorn

## 📂 Estructura del proyecto

```
pet_shop/
├── api/               # Rutas y lógica principal de la API
├── static/            # Archivos estáticos (CSS, JS, imágenes)
├── templates/         # Plantillas HTML (para vistas si es necesario)
├── main.py            # Punto de entrada de la aplicación
├── pyproject.toml     # Configuración de Poetry y dependencias
├── requirements.txt   # Alternativa de dependencias en formato pip
├── .env.example       # Ejemplo de configuración de variables de entorno
```

## ⚙️ Configuración del entorno

### 1. Clonar el repositorio
```bash
git clone git@github.com:lunilop/proyecto_python.git
cd proyecto_python
```

### 2. Configurar variables de entorno
Renombrar el archivo `.env.example` a `.env` y completar los valores necesarios:
```bash
cp .env.example .env
```

### 3. Instalar dependencias
Usa **Poetry** para instalar las dependencias del proyecto:
```bash
poetry install
```

Si prefieres usar `pip`, instala las dependencias desde el archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación
Inicia el servidor local con:
```bash
poetry run uvicorn main:app --reload
```

La API estará disponible en: `http://127.0.0.1:8000`.

## 📋 Endpoints principales

### Auth
- `POST /auth/register`: Registrar un nuevo usuario.
- `POST /auth/login`: Iniciar sesión y obtener un token JWT.

### Usuarios
- `POST /users`: Registrar un nuevo usuario.
- `GET /users`: Lista todos los usuarios.
- `GET /users/{id}`: Lista los usuarios por id.
- `DELETE /users/{id}`: Eliminar un usuario.

### Productos
- `POST /products`: Crear un nuevo producto.
- `GET /products`: Lista todos los productos.
- `GET /products/{id}`: Lista los productos por id.
- `PUT /products/{id}`: Actualizar un producto existente.
- `DELETE /products/{id}`: Eliminar un producto.

## 📝 Notas adicionales

- **Futuras funcionalidades**: El código incluye comentarios para funcionalidades planificadas como promociones y órdenes, que no están completamente implementadas.
- **Base de datos**: El proyecto utiliza MongoDB como base de datos. Asegúrate de que tu conexión esté configurada correctamente en el archivo `.env`.

## 🐾 Contribuciones
Si deseas contribuir al proyecto, por favor crea un fork, realiza tus cambios, y envía un pull request. Todas las contribuciones son bienvenidas.

## 📄 Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

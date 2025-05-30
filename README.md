
## 📄 Descripción breve

Aplicación web que simula un marketplace para gestionar productos. Permite crear, listar, editar y eliminar productos mediante una interfaz sencilla conectada a un backend en Flask y una base de datos SQLite.

## 🎯 Objetivo del ejercicio

El objetivo principal de este proyecto fue aplicar diferentes tipos de **pruebas de software** para asegurar el correcto funcionamiento del sistema. Se utilizaron enfoques como pruebas de humo, caja blanca, caja negra, caja gris y pruebas de estabilidad, además de una reflexión sobre arquitectura por capas.

## 🛠️ Herramientas y tecnologías usadas

- **Frontend**: HTML, CSS, animaciones, mockups
- **Backend**: Python + Flask
- **Base de datos**: SQLite
- **Pruebas**: Python (`requests`, `subprocess`, `sqlite3`)
- **Control de versiones**: Git + GitHub
- **Diseño visual y mockup**: Herramientas de diseño web (manual o externa)

## 🚀 Mejoras aplicadas

- Cambio completo de la gama de colores del sitio.
- Se añadió un banner con imagen centrada.
- Animaciones mejoradas en los botones (cambio de color e iluminación).
- Reformulación del listado de productos: ahora se muestran como tarjetas.
- Inclusión de íconos de redes sociales en el pie de página con animaciones visuales.

## 📦 Cómo clonar y ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/MiguelAngel-R/crud_productos.git
cd crud_productos
```

### 2. Crear entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
venv\Scripts\activate   # En Windows
```

### 3. Instalar dependencias

```bash
pip install flask
```

### 4. Ejecutar la aplicación

```bash
python backend.py
```

Abre tu navegador en: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 🧪 Pruebas implementadas

| Tipo de Prueba        | Descripción breve                                                                 |
|------------------------|----------------------------------------------------------------------------------|
| Prueba de humo         | Verifica que el servidor Flask levante correctamente.                           |
| Caja blanca            | Prueba directa sobre la base de datos (inserción y lectura con SQLite).         |
| Caja negra             | Prueba del comportamiento externo de la API (`POST`, `GET`).                    |
| Caja gris              | Prueba con conocimiento parcial para actualizar y eliminar productos.           |
| Estabilidad (stress)   | Inserta 100 productos para validar el comportamiento bajo carga.                |
| UI/UX (manual)         | Verificación visual de la interfaz y diseño responsivo.                         |

## 🙋 Créditos del autor

**Miguel Ángel Restrepo Saavedra**  
Estudiante de Ingeniería de Software II  
29 de mayo de 2025  

Repositorio original del proyecto:  
🔗 [https://github.com/MiguelAngel-R/crud_productos](https://github.com/MiguelAngel-R/crud_productos)

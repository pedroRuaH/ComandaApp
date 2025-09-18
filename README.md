# Comanda App

Aplicación para la gestión de órdenes en restaurantes.

## Integrantes

- Mario Quiñones
- Rafael Ramirez
- Jesus Gonzalez
- Pedro Rua

## Descripción

Comanda App es un proyecto de software enfocado en proveer una solución para restauranteros en la organización de sus órdenes. El sistema facilita la gestión de comandas (primer pedido) y notifica a todas las áreas involucradas para llevar a cabo el pedido de manera eficiente y ordenada.

## Características

- Gestión de órdenes y comandas
- Notificaciones internas para el flujo de pedidos
- Integración con base de datos en AWS

## Requisitos

- Python 3.8+
- PostgreSQL
- Entorno virtual de Python

## Instalación

1. **Clona el repositorio:**
   ```sh
   git clone <URL_DEL_REPOSITORIO>
   cd ComandaApp

2. **Crea y activa un entorno virtual:**

- En Windows:
python -m venv .venv
.\.venv\Scripts\activate

3. **Instala las dependencias:**

pip install -r requirements.txt

**Notas**
- El archivo .env no se comparte por seguridad. 
- Para probar con una base de datos local es necesario tener postgres instalado y crear una base de datos.
- Puedes remplazar la base de datos en settings si quieres probar con esta plantilla, solo copia y pega

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Nombre de mi DB',  
        'USER': 'postgres',  # Regularmente el usuario postgres por default
        'PASSWORD': 'tu contraseña',  
        'HOST': 'localhost',  # Localhost es default
        'PORT': '5432',  # Puerto default de postgres
    }
}
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
- Este archivo tiene integrado db.sqlite3 


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

4. **Comandos para migrar a BD**
- python manage.py makemigrations
- python manage.py migrate

5. **Agrega datos a la bd**
- cd comanda_app
- python manage.py createsuperuser
- python manage.py loaddata initial_data.json
- python manage.py loaddata items.json

si quieres borrar los datos usa el comando:
- python manage.py flush
solo requerda que este comando borra el superuser y hay que crearlo de nuevo

6. **Run Server**
localhost server http://127.0.0.1:8000/
- python manage.py runserver

- python manage.py runserver 0.0.0.0:8000


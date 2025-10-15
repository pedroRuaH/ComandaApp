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

## Uso de Blueprints

En Flask, los **blueprints** permiten organizar tu aplicación en componentes reutilizables y modulares.

### Crear un Blueprint

1. **Crea un archivo para tu blueprint** (por ejemplo, `products.py`):

    ```python
    from flask import Blueprint

    blueprint = Blueprint('products', __name__)

    @blueprint.route('/')
    def index():
        return "¡Hola desde el blueprint de productos!"
    ```

2. **Registra el blueprint en tu aplicación** (en `__init__.py`):

    ```python
    from src.api.products import blueprint as products_bp

    def _register_blueprints(app):
        app.register_blueprint(products_bp, url_prefix="/products")
    ```

3. **Accede a la ruta en tu navegador:**  
   [http://127.0.0.1:5000/products/](http://127.0.0.1:5000/products/)

---

## Comandos de Migración y Seed

### Inicializar y Migrar la Base de Datos

1. **Inicializar el entorno de migraciones** (solo la primera vez):

    ```sh
    flask db init
    ```

2. **Crear una migración** (cada vez que cambies tus modelos):

    ```sh
    flask db migrate -m "Descripción del cambio"
    ```

3. **Aplicar la migración a la base de datos:**

    ```sh
    flask db upgrade
    ```

### Poblar la Base de Datos con Datos Iniciales (Seed)

Tu proyecto incluye un comando CLI para poblar la base de datos con datos de ejemplo:

```sh
flask seed

## Diagrama de Base de Datos

```mermaid
erDiagram
    User {
        int id PK
        string username UK
        string password
    }

    Inventory {
        int id PK
        string product_name
        string unit
        int quantity
    }

    Movement {
        int id PK
        int product_id FK
        string movement_type
        int quantity
        datetime date
    }

    Product {
        int id PK
        string name
        string description
        float price
        string category
        bool available
        int inventory_id FK
    }

    Drink {
        int id PK
        string name
        string description
        float price
        string size
        bool available
    }

    Inventory ||--o{ Movement : "has movements"
    Inventory ||--o{ Product : "has products"


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
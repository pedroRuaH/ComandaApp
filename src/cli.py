# src/cli.py
from click import echo
from src.extensions import db
from src.models import User, Drink, Inventory, Movement, Product

def register_seed_command(app):
    @app.cli.command("seed")
    def seed():
        """Inserta datos de ejemplo iniciales en todas las tablas."""
        if User.query.first() or Product.query.first() or Drink.query.first():
            echo("Seed already applied.")
            return

        # ───────────────────────────────────────────────
        # USUARIOS
        users = [
            User(username="admin", password="admin123"),
            User(username="mesero1", password="mesa001"),
            User(username="cajero", password="caja123"),
        ]
        db.session.add_all(users)

        # ───────────────────────────────────────────────
        # BEBIDAS
        drinks = [
            Drink(name="Café americano", description="Café negro clásico", price=25.0, size="mediano"),
            Drink(name="Latte", description="Café con leche espumosa", price=35.0, size="grande"),
            Drink(name="Té verde", description="Té natural sin azúcar", price=20.0, size="chico"),
        ]
        db.session.add_all(drinks)

        # ───────────────────────────────────────────────
        # INVENTARIO
        inventory_items = [
            Inventory(product_name="Café en grano", unit="kg", quantity=5),
            Inventory(product_name="Leche entera", unit="L", quantity=10),
            Inventory(product_name="Azúcar refinada", unit="kg", quantity=3),
        ]
        db.session.add_all(inventory_items)
        db.session.flush()  # asegura IDs disponibles

        # ───────────────────────────────────────────────
        # PRODUCTOS
        products = [
            Product(name="Croissant", description="Pan francés con mantequilla", price=20.0, category="comida", available=True, inventory_id=inventory_items[0].id),
            Product(name="Galleta choco chip", description="Galleta con chispas de chocolate", price=15.0, category="postre", available=True, inventory_id=inventory_items[2].id),
            Product(name="Sandwich", description="Sandwich de jamón y queso", price=40.0, category="comida", available=True, inventory_id=None),
        ]
        db.session.add_all(products)
        db.session.flush()

        # ───────────────────────────────────────────────
        # MOVIMIENTOS DE INVENTARIO
        movements = [
            Movement(product_id=inventory_items[0].id, movement_type="entrada", quantity=2),
            Movement(product_id=inventory_items[1].id, movement_type="salida", quantity=1),
            Movement(product_id=inventory_items[2].id, movement_type="entrada", quantity=5),
        ]
        db.session.add_all(movements)

        # ───────────────────────────────────────────────
        db.session.commit()
        echo("Seed completed successfully 🎉")

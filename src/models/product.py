from __future__ import annotations

from sqlalchemy import JSON

from src.extensions import db

# Productos que se registran en el sistema (menú, ingredientes, etc.)
class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)   # Nombre del producto
    description = db.Column(db.String(200))            # Descripción opcional
    price = db.Column(db.Float, nullable=False)        # Precio de venta
    category = db.Column(db.String(50), nullable=True) # Ej: bebida, comida, postre
    available = db.Column(db.Boolean, default=True)    # Si está disponible

    # Relación con inventario
    inventory_id = db.Column(
    db.Integer,
    db.ForeignKey("inventory.id", name="fk_product_inventory_inventory"),
        nullable=True
    )
    inventory = db.relationship("Inventory", backref="products")
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "category": self.category,
            "available": self.available
        }


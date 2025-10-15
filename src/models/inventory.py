from __future__ import annotations

from sqlalchemy import JSON

from src.extensions import db

class Inventory(db.Model):
    __tablename__ = "inventory"

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    unit = db.Column(db.String(20), nullable=False)  # Ej: kg, piezas
    quantity = db.Column(db.Integer, default=0)

    movements = db.relationship("Movement", backref="inventory", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "product_name": self.product_name,
            "unit": self.unit,
            "quantity": self.quantity
        }


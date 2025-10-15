from __future__ import annotations

from sqlalchemy import JSON

from src.extensions import db

class Drink(db.Model):
    __tablename__ = "drinks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    price = db.Column(db.Float, nullable=False)
    size = db.Column(db.String(50), nullable=True)
    available = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "size": self.size,
            "available": self.available
        }
from __future__ import annotations

from sqlalchemy import JSON

from src.extensions import db

class Movement(db.Model):
    __tablename__ = "movements"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("inventory.id"), nullable=False)
    movement_type = db.Column(db.String(20), nullable=False)  # entrada o salida
    quantity = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, server_default=db.func.now())

    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "movement_type": self.movement_type,
            "quantity": self.quantity,
            "date": self.date.isoformat() if self.date else None
        }


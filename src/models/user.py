from __future__ import annotations
from src.extensions import db
from uuid import uuid4

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
        }

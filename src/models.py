from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Inventory(db.Model):
    __tablename__ = "inventory"

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    unit = db.Column(db.String(20), nullable=False)  # Ej: kg, piezas
    quantity = db.Column(db.Integer, default=0)

    # Relación con movimientos
    movements = db.relationship("Movement", backref="inventory", lazy=True)


class Entry(db.Model):
    __tablename__ = "entries"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("inventory.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, server_default=db.func.now())

    product = db.relationship("Inventory", backref="entries")


class Movement(db.Model):
    __tablename__ = "movements"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("inventory.id"), nullable=False)
    movement_type = db.Column(db.String(20), nullable=False)  # entrada o salida
    quantity = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, server_default=db.func.now())
    
    
class Drink(db.Model):
    _tablename_ = "drinks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)        # Nombre de la bebida (ej. Coca-Cola)
    description = db.Column(db.String(200))                 # Descripción opcional
    price = db.Column(db.Float, nullable=False)             # Precio de venta
    size = db.Column(db.String(50), nullable=True)          # Tamaño (ej. 355ml, 600ml, Litro)
    available = db.Column(db.Boolean, default=True)         # Si está disponible en el menú
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

class Movement(db.Model):
    __tablename__ = "movements"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("inventory.id"), nullable=False)
    movement_type = db.Column(db.String(20), nullable=False)  # entrada o salida
    quantity = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, server_default=db.func.now())
    
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
    inventory_id = db.Column(db.Integer, db.ForeignKey("inventory.id"), nullable=True)
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
       
class Drink(db.Model):
    _tablename_ = "drinks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)        # Nombre de la bebida (ej. Coca-Cola)
    description = db.Column(db.String(200))                 # Descripción opcional
    price = db.Column(db.Float, nullable=False)             # Precio de venta
    size = db.Column(db.String(50), nullable=True)          # Tamaño (ej. 355ml, 600ml, Litro)
    available = db.Column(db.Boolean, default=True)         # Si está disponible en el menú
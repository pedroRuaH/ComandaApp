from flask import Blueprint, render_template, request, redirect, url_for
from src.models import db, Inventory, Product, Movement

inventory_bp = Blueprint("inventory", __name__, url_prefix="/inventory")

# Página principal de inventario
@inventory_bp.route("/", methods=["GET"])
def show_inventory():
    items = Inventory.query.all()
    return render_template("inventory.html", items=items)

#  Registrar un nuevo producto
@inventory_bp.route("/add_product", methods=["POST"])
def add_product():
    name = request.form["name"]
    description = request.form.get("description", "")
    price = float(request.form["price"])
    category = request.form.get("category", "general")
    unit = request.form.get("unit", "pieza")

    # 1. Crear registro en Inventario
    inventory_item = Inventory(product_name=name, quantity=0, unit=unit)
    db.session.add(inventory_item)
    db.session.commit()

    # 2. Crear registro en Productos
    new_product = Product(
        name=name,
        description=description,
        price=price,
        category=category,
        available=True,
        inventory_id=inventory_item.id
    )
    db.session.add(new_product)
    db.session.commit()

    return redirect(url_for("inventory.show_inventory"))

# Registrar movimiento
@inventory_bp.route("/add_movement", methods=["POST"])
def add_movement():
    product_id = request.form["product_id"]
    quantity = int(request.form["quantity"])
    movement_type = request.form["movement_type"]

    new_movement = Movement(product_id=product_id, movement_type=movement_type, quantity=quantity)
    db.session.add(new_movement)

    product = Inventory.query.get(product_id)
    if movement_type == "entrada":
        product.quantity += quantity
    elif movement_type == "salida":
        product.quantity -= quantity

    db.session.commit()
    return redirect(url_for("inventory.show_inventory"))



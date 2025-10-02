from flask import Blueprint, render_template, request, redirect, url_for
from src.models import db, Inventory, Entry, Movement

inventory_bp = Blueprint("inventory", __name__, url_prefix="/inventory")

# Página principal de inventario
@inventory_bp.route("/", methods=["GET"])
def show_inventory():
    items = Inventory.query.all()
    return render_template("inventory.html", items=items)

# Registrar entrada
@inventory_bp.route("/add_entry", methods=["POST"])
def add_entry():
    product_id = request.form["product_id"]
    quantity = int(request.form["quantity"])

    # Crear entrada
    new_entry = Entry(product_id=product_id, quantity=quantity)
    db.session.add(new_entry)

    # Actualizar inventario
    product = Inventory.query.get(product_id)
    product.quantity += quantity

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



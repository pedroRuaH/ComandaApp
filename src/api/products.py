from flask import Flask, Blueprint, jsonify
from src.models import Product

blueprint = Blueprint('products', __name__)

products: list[Product] = [
    Product(
        id = 1,
        name = "Coca-Cola",
        description = "Bebida gaseosa de cola",
        price = 1.5,
        category = "bebida",
        available = True
    ),
    Product(
        id = 2,
        name = "Hamburguesa",
        description = "Hamburguesa con queso y lechuga",
        price = 5.0,
        category = "comida",
        available = True
    )
]

# Obtener todos los productos
@blueprint.route('/', methods=['GET'])
def get_products():
    return jsonify([product.to_dict() for product in products])

# Obtener un producto por ID
@blueprint.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p.id == product_id), None)
    if product:
        return jsonify(product.to_dict())
    return jsonify({"error": "Producto no encontrado"}), 404

# Agregar un nuevo producto
@blueprint.route('/', methods=['POST'])
def add_product():
    # Lógica para agregar un producto (omitir detalles por simplicidad)
    return jsonify({"message": "Producto agregado"}), 201

# Actualizar un producto existente
@blueprint.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((p for p in products if p.id == product_id), None)
    if product:
        # Lógica para actualizar el producto (omitir detalles por simplicidad)
        return jsonify({"message": "Producto actualizado"}), 200
    return jsonify({"error": "Producto no encontrado"}), 404

# Eliminar un producto
@blueprint.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = next((p for p in products if p.id == product_id), None)
    if product:
        products.remove(product)
        return jsonify({"message": "Producto eliminado"}), 200
    return jsonify({"error": "Producto no encontrado"}), 404
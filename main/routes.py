# routes.py
from flask import Blueprint, render_template

# Creamos un "blueprint" para las rutas
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "Bienvenido a ComandaApp "

@main.route('/menu')
def menu():
    return render_template('menu.html')  # Renderiza una plantilla HTML para el menú 

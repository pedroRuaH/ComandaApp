# __init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Importamos las rutas
    from .routes import main
    app.register_blueprint(main)

    return app

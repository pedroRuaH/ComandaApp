import click
from flask import Flask
from .models.product import Product
from .models.user import User
from .extensions import db, migrate


def create_app(config_object: str | None = None) -> Flask:
    """"Create a Flask application using the app factory pattern."""
    app = Flask(__name__)
    _load_config(app, config_object)
    _register_extensions(app)
    _register_blueprints(app)
    _register_error_handlers(app)
    _register_cli(app)
    return app



def _load_config(app: Flask, config_object: str | None) -> None:
    """Load default settings, optionally overriding with a named config."""
    app.config.from_mapping(
        SECRET_KEY="dev",
        JSON_SORT_KEYS=False,  # To keep the order of JSON responses as defined
    )
    if config_object:
        app.config.from_object(config_object)


def _register_extensions(app: Flask) -> None:
    """Register Flask extensions."""
    db.init_app(app)
    migrate.init_app(app, db)
    pass

def _register_blueprints(app: Flask) -> None:
    """Register Flask blueprints.
    Blueprints are a way to organize your Flask application into smaller and reusable components.
    """
    from src.api.products import blueprint as products_bp

    app.register_blueprint(products_bp, url_prefix="/products")


def _register_error_handlers(app: Flask) -> None:
    """Register error handlers."""
    pass

def _register_cli(app):
    @app.cli.command("seed")
    def seed():
        """Seed the database with initial data."""
        if User.query.first():
            click.echo("Database already seeded.")
            return

        # Example users
        user1 = User(username="admin", password="admin123")
        user2 = User(username="mario", password="mario123")

        # Example products
        product1 = Product(name="Coca-Cola", description="Bebida gaseosa de cola", price=1.5, category="bebida", available=True)
        product2 = Product(name="Hamburguesa", description="Hamburguesa con queso y lechuga", price=5.0, category="comida", available=True)

        db.session.add_all([user1, user2, product1, product2])
        db.session.commit()
        click.echo("Database seeded!")


from pathlib import Path
import os

# 
BASE_DIR = Path(__file__).resolve().parent.parent
# Instance dir is for configurations and local data that shouldn't be in version control
INSTANCE_DIR = BASE_DIR / "instance"

def _sqlite_uri(filename: str) -> str:
    """Construye la URI de SQLite dentro de la carpeta instance/."""
    return f"sqlite:///{INSTANCE_DIR / filename}"

class BaseConfig:
    SECRET_KEY = os.environ.get("SECTRET_KEY", "dev")
    JSON_SORT_KEYS = False  # To keep the order of JSON responses as defined
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # If using SQLAlchemy

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", _sqlite_uri("comanda.db")
    )

class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", _sqlite_uri("sqlite:///prod.db")
    )
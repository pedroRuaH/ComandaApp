import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///comanda.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
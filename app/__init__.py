from flask import Flask
from app.config import database_config,migrate_config
from app import routes


def create_app():
    app = Flask(__name__)
    database_config.init_app(app)
    migrate_config.init_app(app)
    routes.init_app(app)
    return app
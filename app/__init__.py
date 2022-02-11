from flask import Flask
from app import config
from app import routes


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    routes.init_app(app)
    return app
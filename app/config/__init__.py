from flask import Flask
from app.config import app_config,database_config,migrate_config

def init_app(app:Flask) -> None:
    app_config.init_app(app)
    database_config.init_app(app)
    migrate_config.init_app(app)
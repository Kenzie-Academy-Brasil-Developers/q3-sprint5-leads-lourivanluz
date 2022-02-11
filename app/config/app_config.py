from flask import Flask


def init_app(app:Flask) -> None:
    app.config['JSON_SORT_KEYS'] = False
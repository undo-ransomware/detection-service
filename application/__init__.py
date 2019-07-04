from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        from application.routes.info_api import info_api
        from application.routes.file_operation_api import file_operation_api

        app.register_blueprint(info_api, url_prefix='/info')
        app.register_blueprint(file_operation_api, url_prefix='/file-operation')

        db.create_all()

        return app
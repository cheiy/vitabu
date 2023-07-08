# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

# local imports
from config import app_config

# database variable initialization
db = SQLAlchemy()

login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config = True)
    """
    Load config from instance/config.py
    """
    app.config.from_object(app_config[config_name])
    """
    Load config from config.py
    """
    app.config.from_pyfile('config.py')
    """
    Create db object
    """
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page"
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)

    from app import models

    return app

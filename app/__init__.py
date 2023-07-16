# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

import os
# local imports
from config import app_config

# database variable initialization
db = SQLAlchemy()

login_manager = LoginManager()

def create_app(config_name):
    if os.getenv('FLASK_CONFIG') == "production":
        app = Flask(__name__)
        app.config.update(SECRET_KEY=os.getenv('SECRET_KEY'),
                SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
                )
    else:
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

    Bootstrap(app)

    from app import models

    """ Register Blueprints """
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .products import products as products_blueprint
    app.register_blueprint(products_blueprint)

    return app

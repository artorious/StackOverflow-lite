#!/usr/bin/env python3
""" Initialization file - App factory"""
from flask import Flask
from instance.config import app_config
from app.api.v1.database_model import DatabaseManager


def create_app(config_mode=None):
    """ Init the app """
    app = Flask(__name__, instance_relative_config=True)
    # Load from config file
    app.config.from_object(app_config[config_mode])
    app.config.from_pyfile("config.py")
    # Import views
    from app.api.v1 import auth_views
    # Register Blueprints
    app.register_blueprint(auth_views.auth_bp_v1)
    # create database tables
    with app.app_context():
        db = DatabaseManager()
        db.create_tables()
    return app

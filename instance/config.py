#!/usr/bin/env python3
""" Application Configuration file """
import os


class BaseConfig:
    """ Base/Parent Configuration class """
    DEBUG = False
    SECRET = os.getenv("SECRET")
    DATABASE_URI = os.getenv("DATABASE_URL")


class DevelopmentConfig(BaseConfig):
    """ Cofigurations for app development """
    DEBUG = True


class TestingConfig(BaseConfig):
    """ Configurations for testing the app """
    TESTING = True
    DATABASE_URI = os.getenv("TEST_DATABASE_URL")
    DEBUG = True


app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
}

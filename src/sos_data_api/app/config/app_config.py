import os
from flask import Flask


class Config(object):
    HOST = '0.0.0.0'
    MONGODB_SETTINGS = {
        "db": " ",
        "host": "mongodb+srv://sos_data:d51gY76reBVaOkIS@maincluster.pysta.mongodb.net/stackoverservices?retryWrites=true&w=majority",
        # 'username': "sos_data",
        # "password": "d51gY76reBVaOkIS"
    }

    @staticmethod
    def init_app(app: Flask):
        pass


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


evn_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

from flask_cors import CORS
from flask_restful import Api, Resource
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine
from mongoengine import Document, StringField, IntField

from .config.app_config import evn_config
from .web.resources.technology import Technology, TechnologyList


def create_app(config_name: str):
    """TODO docstring"""

    app = Flask(__name__)
    app.config.from_object(evn_config[config_name])
    evn_config[config_name].init_app(app)
    CORS(app)

    api = Api(app)
    db = MongoEngine(app)

    api.add_resource(Technology, '/tech/save')
    api.add_resource(TechnologyList, '/tech/list')

    return app

# coding: utf-8
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from config.config import config


app = Flask(__name__)
db = SQLAlchemy()
redis_client = FlaskRedis(app)
CORS(app)


def create_app(config_name):
    app.config.from_object(config[config_name])

    db.init_app(app)
    redis_client.init_app(app)

    from .api_v1 import api as api_v1_blueprint
    app.register_blueprint(api_v1_blueprint, url_prefix='/api/v1')

    return app

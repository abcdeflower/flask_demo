# -*- coding:utf-8 -*-
import os
import json

configs = json.load(open('config.json'))
for key in configs:
    os.environ[key] = configs[key]


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SSL_DISABLE = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQL_URI')
    REDIS_URL = os.environ.get('REDIS_URL')


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQL_URI')
    REDIS_URL = os.environ.get('REDIS_URL')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}

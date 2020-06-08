# coding:utf-8
from flask import Blueprint


api = Blueprint('api_v1', __name__)


from . import job

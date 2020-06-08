# coding:utf-8
from flask import jsonify


class SystemStatusCode():
    @staticmethod
    def code_200_err(status=-1, data=None, message=None):
        response = jsonify(
            {'status': status, 'data': data, 'message': message}
        )
        response.status_code = 200
        return response

    @staticmethod
    def code_200_ok(status=0, data=None, message=None):
        response = jsonify(
            {'status': status, 'data': data, 'message': message}
        )
        response.status_code = 200
        return response

    @staticmethod
    def code_500(status=-1, data=None, message=None):
        response = jsonify(
            {'status': status, 'data': data, 'message': message}
        )
        response.status_code = 500
        return response

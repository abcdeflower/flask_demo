# coding:utf-8
from flask import request
from log.logger import ErrorLogger


class JudageContentType():
    def get_params(self, content_type):
        func_name = str(content_type)
        method = getattr(self, func_name, self.content_other)
        return method

    def application_json(self):
        try:
            params = request.get_json()
        except Exception as e:
            ErrorLogger.error(e)
            params = {}
        for key in params.keys():
            if isinstance(params[key], str):
                params[key] = params[key].strip()
        return params

    def content_other(self):
        try:
            params = request.values.to_dict()
        except Exception as e:
            ErrorLogger.error(e)
            params = {}
        for key in params.keys():
            if isinstance(params[key], str):
                params[key] = params[key].strip()
        return params


def request_params():
    ct = JudageContentType()
    try:
        tp = request.headers['Content-Type'].lower()
    except Exception as e:
        ErrorLogger.error(e)
        tp = 'x'
    tp = tp.replace('/', '_')
    params = ct.get_params(tp)()
    return params

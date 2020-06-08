# coding:utf-8
config = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(filename)s - %(message)s',
        },
        'error': {
            'format': '%(asctime)s - %(filename)s - %(lineno)d - %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple'
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'logging.log',
            'level': 'DEBUG',
            'formatter': 'simple'
        },
        'errorfile': {
            'class': 'logging.FileHandler',
            'filename': 'error.log',
            'level': 'ERROR',
            'formatter': 'error'
        },
    },
    'loggers': {
        'StreamLogger': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'FileLogger': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
        'ErrorLogger': {
            'handlers': ['errorfile'],
            'level': 'ERROR'
        },
    }
}

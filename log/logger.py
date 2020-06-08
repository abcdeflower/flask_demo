# coding:utf-8
import logging.config
from config.logger import config


logging.config.dictConfig(config)
StreamLogger = logging.getLogger("StreamLogger")
FileLogger = logging.getLogger("FileLogger")
ErrorLogger = logging.getLogger('ErrorLogger')

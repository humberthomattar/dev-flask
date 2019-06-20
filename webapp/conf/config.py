#!/usr/bin/python
# encoding: iso-8859-1

""" Filename:     config.py
    Purpose:      Este arquivo  externaliza as configuracoes da aplicacao.
                  Separando os ambientes por classes
                  BaseConfig = PRODUCAO - as demais classes herdam e
                  sobreescrem os atributos de PRODUCAO..
    Requirements:
    Author:       humbertho mattar
"""
import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    APP_NAME = 'skeleton_flask'
    VERSION = '0.0.1'
    HOST = '0.0.0.0'
    PORT = int(os.environ.get("PORT", 5000))
    LOG_FILENAME = 'webapp/logs/log_%s.log' % APP_NAME
    LOG_LEVEL = 'INFO'  # DEBUG OR INFO
    HELLO_MESSAGE = 'It Works!'
    
class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    HOST = '0.0.0.0'
    PORT = int(os.environ.get("PORT", 5000))
    LOG_LEVEL = 'DEBUG'  # DEBUG OR INFO
    

# Other example: class TestingConfig(BaseConfig):

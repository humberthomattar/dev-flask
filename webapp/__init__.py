#!/usr/bin/python
# coding: utf-8
""" Filename:     __init__.py
    Purpose:      This file is required to structure the web service as a
                  package, to be able to define routes in multiple modules.
                  This is the most basic design pattern for multiple files
                  Flask apps: http://flask.pocoo.org/docs/patterns/packages/
    Requirements: 
    Author:       Cédric Beuzit
"""
import yaml
import logging
from flask import Flask
from logging.config import fileConfig

app = Flask(__name__)

# application wide global variables and config parameters must be defined here
# (not in `run.py`) for being able to import them in the beginning of the
# views files but we can perfectly imagine a smarter config procedure
#app.config['HELLO_WORLD'] = 'Hello Flask!'

def setup_logging(loggername, path, default_level='DEBUG'):
    import coloredlogs
    global logger
    try:
        with open(path, 'rt') as f:    
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
            logger = logging.getLogger(loggername)
            coloredlogs.install(logger=logger, level=logger.level)
            logger.debug('Logger configurado corretamente. => log level: ' +  
                str(logger.level) + ' ' + str(path))
    except Exception as e:
        print(str(e) + '=> Erro na configuracao do Log. Usando configuracao padrao')
        logging.basicConfig(level=default_level)
        logger = logging.getLogger(loggername)
        coloredlogs.install(level=default_level)
    return


def get_conf(file):
    try:
        logger.debug('Recuperando as configuracoes da rotina => ' + str(file))
        with open(file, 'r') as ymlfile:
            cfg = yaml.safe_load(ymlfile)
        app.config.update(cfg)
        logger.debug('Configuracoes recuperadas com sucesso. => ' + str(cfg))
    except Exception as e:
        logger.error('get_conf: ' + str(e))
    return


setup_logging(loggername='app', path='./webapp/conf/logging.yaml')
get_conf('./webapp/conf/config.yaml')

logger.debug(str(app.config['HELLO']))

# The views modules that contain the application's routes are imported here
# Importing views modules MUST BE in the end of the file to avoid problems
# related to circular imports http://flask.pocoo.org/docs/patterns/packages
import webapp.views
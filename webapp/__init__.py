#!/usr/bin/python
# coding: utf-8
""" Filename:     __init__.py
    Purpose:      This file is required to structure the web service as a
                  package, to be able to define routes in multiple modules.
                  This is the most basic design pattern for multiple files
                  Flask apps: http://flask.pocoo.org/docs/patterns/packages/
    Requirements: see requirements.txt 
    Author:             Humbertho Mattar      
"""
import os
import logging
from flask import Flask
from logging.config import dictConfig
from webapp.conf.logging import logging_config


app = Flask(__name__)

# application wide global variables and config parameters must be defined here
# (not in `run.py`) for being able to import them in the beginning of the
# views files but we can perfectly imagine a smarter config procedure

# Set log configurations
try:
    dictConfig(logging_config)
    logger = logging.getLogger('app')
    logger.debug('Logger configurado corretamente. => log level: ' +  str(logger.level))
except Exception as e:
    logging.basicConfig(level='DEBUG')
    logger = logging.getLogger()

#  set general configurations
#  export FLASK_ENV=development && export FLASK_APP=webapp
if os.environ.get("FLASK_ENV") == 'development':
    app.config.from_object('webapp.conf.config.DevelopmentConfig')
    logger.debug('Utilizando configuracoes do ambiente de DESENVOLVIMENTO')
else:
    app.config.from_object('webapp.conf.config.BaseConfig')
    logger.debug('Utilizando configuracoes do ambiente de PRODUCAO')


# The views modules that contain the application's routes are imported here
# Importing views modules MUST BE in the end of the file to avoid problems
# related to circular imports http://flask.pocoo.org/docs/patterns/packages
import webapp.controllers
#!/usr/bin/python
# coding: utf-8
""" Filename:     controllers.py
    Purpose:      This file is one of the controllers file that can contain the
                  routes for the application
    Requirements: 
    Author:       Humbertho Mattar
"""
import json
from webapp import logger
from webapp import app


# importing application wide parameters and global variables that have been
# defined in __init__.py

@app.route('/', methods=['GET', 'HEAD'])
def webapp():
    message = app.config['HELLO_MESSAGE']
    return message


@app.route('/info/', methods=['GET', 'HEAD'])
def info():
    mensagem = {
        'nome da aplicacao': app.config['APP_NAME'],
        'versao': app.config['VERSION']
    }
    logger.debug('Informação enviada com sucesso!')
    return json.dumps(mensagem)


@app.errorhandler(400)
def bad_request(e):
    mensagem = {
        'status code': 400,
        'message': 'bad request'
    }
    return json.dumps(mensagem), 400


@app.errorhandler(500)
def internal_server_error(e):
    mensagem = {
        'status code': 500,
        'message': 'internal server error'
    }
    return json.dumps(mensagem), 500


@app.errorhandler(404)
def page_not_found(e):
    mensagem = {
        'status code': 404,
        'message': 'page not found'
    }
    return json.dumps(mensagem), 404
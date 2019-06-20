#!/usr/bin/python
# coding: utf-8
""" Filename:     run.py
    Purpose:      This file runs the Flask application service
    Requirements: Flask
    Author:       Humbertho Mattar
"""
from webapp import app



# TODO: External host and port
if __name__ == '__main__':
    app.run(
        host=app.config.get('HOST', '0.0.0.0'),
        port=app.config.get('PORT', 5000)
    )
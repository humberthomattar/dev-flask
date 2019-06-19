#!/usr/bin/python
# coding: utf-8
""" Filename:     run.py
    Purpose:      This file runs the Flask application service
    Requirements: Flask
    Author:       Cédric Beuzit
"""
from webapp import app


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
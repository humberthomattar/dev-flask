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
from flask import Flask

app = Flask(__name__)

# application wide global variables and config parameters must be defined here
# (not in `run.py`) for being able to import them in the beginning of the
# views files but we can perfectly imagine a smarter config procedure
app.config['HELLO_WORLD'] = 'Hello Flask!'



# The views modules that contain the application's routes are imported here
# Importing views modules MUST BE in the end of the file to avoid problems
# related to circular imports http://flask.pocoo.org/docs/patterns/packages
import webapp.views
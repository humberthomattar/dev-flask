#!/usr/bin/python
# coding: utf-8
""" Filename:     views.py
    Purpose:      This file is one of the views file that can contain the
                  routes for the application
    Requirements: 
    Author:       Cédric Beuzit
"""
from webapp import app

# importing application wide parameters and global variables that have been
# defined in __init__.py
#message = app.config['HELLO_WORLD']

@app.route('/')
def webapp():
    return message
#!/usr/bin/env python
from distutils.core import setup


url = 'https://github.com/Bystroushaak/httpkie'
long_description = """
Documentation can be found in README.creole, or at project pages at github: 
""" + url

setup(
    name         = 'httpkie',
    version      = '1.1.0',
    py_modules   = ['httpkie'],

    author       = 'Bystroushaak',
    author_email = 'bystrousak@kitakitsune.org',

    url          = url,
    description  = 'Easy to use web scrapper with cookies and proxy support.',
    license      = 'CC BY',

    long_description=long_description,

    classifiers=[
        "License :: Public Domain",

        "Programming Language :: Python :: 2.7",

        "Topic :: Software Development :: Libraries",
        "Topic :: Internet :: WWW/HTTP"
    ],
)

#!/usr/bin/env python
import os
from distutils.core import setup


def dirToLinks(directory):
	return map(lambda x: directory + "/" + x, os.listdir(directory))


url = 'https://github.com/Bystroushaak/httpkie'

setup(
	name         = 'httpkie',
	version      = '1.0.0',
	py_modules   = ['httpkie'],

	author       = 'Bystroushaak',
	author_email = 'bystrousak@kitakitsune.org',

	url          = url,
	description  = 'Easy to use web scrapper with cookies and proxy support.',
	license      = 'CC BY',

	long_description = """Documentation can be found in README.creole, or at
project pages at github: """ + url,

	classifiers=[
		"License :: Public Domain",

		"Programming Language :: Python :: 2.7",

		"Topic :: Software Development :: Libraries",
		"Topic :: Internet :: WWW/HTTP"
	],

	data_files=[
		('others', ['README.creole', "__init__.py"]),
	]
)

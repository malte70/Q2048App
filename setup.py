#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

def file_get_contents(filename):
	f        = open(filename, "r")
	contents = f.read()
	f.close()
	return contents

setup(
	name             = "Q2048App",
	version          = "0.0.1",
	description      = "Gabriele Cirulli's famous 2048, wrapped in a minimal Qt5 desktop application",
	author           = "Malte Bublitz",
	author_email     = "malte70@tuta.io",
	url              = "https://github.com/malte70/Q2048App",
	license          = "License :: OSI Approved :: BSD License",
	py_modules       = ["Q2048App"],
	classifiers      = [
		"Development Status :: 4 - Beta",
		"Environment :: Console",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: BSD License",
	],
	long_description = file_get_contents("README.md")
)



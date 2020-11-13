"""Builds boilerplate as a package

"""
from distutils import util

import setuptools

version = dict()
path = util.convert_path("src/bierproductie_api/core/version.py")
with open(path) as file:
    exec(file.read(), version)

setuptools.setup(version=version["__version__"])

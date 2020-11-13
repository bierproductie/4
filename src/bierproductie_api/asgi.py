"""This module is used by Gunicorn to run our APP"""
from bierproductie_api import create_app

app = create_app()

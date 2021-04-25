""" Module to initialize Flask server """

from flask import Flask

app = Flask(__name__)

from app import views

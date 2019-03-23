""" The Python Flask Server """
from flask import Flask, render_template

APP = Flask(__name__,
            static_folder='../../Front_End/React/build/static',
            template_folder='../../Front_End/React/build/')

@APP.route('/')
def serve():
    """ Serve React App """
    return render_template('index.html')

@APP.route('/health')
def health():
    """ Serve React App """
    return "Hello World!"

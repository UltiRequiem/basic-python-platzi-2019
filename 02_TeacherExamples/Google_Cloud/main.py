# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hola():
    return 'Â¡Hola, alumnos de platzi!'


if __name__ == '__main__':
    app.run()

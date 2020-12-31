# -*- coding: utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hola():
    return render_template('contact_book.html')


if __name__ == '__main__':
    app.run()

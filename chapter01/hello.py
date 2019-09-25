# encoding: utf-8
from flask import Flask

app = Flask(__name__)


@app.route('/greet')
@app.route('/greet/<name>')
def index(name="programer"):
    return '<h1>Hello, %s !</h1>' % name


from flask import Flask, url_for
from markupsafe import escape
from flask import request
from flask import render_template

app = Flask(__name__)


def do_the_login():
    return '<p>logged in<p>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return do_the_login()


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return 


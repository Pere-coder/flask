from flask import Flask, url_for
from markupsafe import escape
from flask import request
from flask import render_template

app = Flask(__name__)


def do_the_login():
    return '<p>logged in<p>'

def valid_login(username, password):
    if username == 'pere' and password =='1234':
        return username , password

@app.route('/login', methods=['GET', 'POST'])
def login():
    error=None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return render_template('hello.html', name = request.form['username'])
        else:
            error = 'Invalid username/password'
    return render_template('hello.html', error=error)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)


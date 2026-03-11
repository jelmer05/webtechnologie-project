import sqlite3
from flask import Flask, render_template, g
app = Flask(__name__)

def get_db():
    """get database contenction"""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/<userId>')
def login_page(userId):
    return render_template('login.html', person = userId)
     




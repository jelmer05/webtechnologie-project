from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/<userId>')
def login_page(userId):
    return render_template('login.html', person = userId)
     




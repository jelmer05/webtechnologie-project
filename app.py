import os
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)

class User(db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    naam= db.Column(db.Text)

    def __init__(self,naam):
        self.naam = naam

    def __repr__(self):
        return f"Naam van User: {self.naam}"

@app.route("/")
def indexRoute():
    return render_template('index.html')

@app.route("/aanmelden")
def aanmelden():

    return render_template('aanmelden.html')

@app.route("/add")
def add_user():
    user = User("jelmer")
    db.session.add(user)
    db.session.commit()
    print(User.query.all())
    return render_template('add.html')
    

@app.route("/list")
def list_user():
    users = User.query.all()
    return render_template('toon_users.html', users=users)

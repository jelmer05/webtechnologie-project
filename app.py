from webtech import app, db
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from webtech.models import User

from flask_migrate import Migrate


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

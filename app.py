from webtech import app, db
from flask import Flask, render_template, url_for, redirect, flash, request
from flask_sqlalchemy import SQLAlchemy
from webtech.models import User
from webtech.form import RegistrationForm,LoginFrom
from flask_migrate import Migrate
from flask_login import login_user, login_required, logout_user


@app.route("/")
def indexRoute():
    return render_template('index.html')

@app.route("/dashboard")
@login_required
def dashboard():
    users = User.query.all()
    return render_template("toon_users.html", users=users) 

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('je bent nu uitgelogd')
    return redirect(url_for('indexRoute'))


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginFrom()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('login is gelukt')
            next = request.args.get('next')

            if next is None or not next[0]=='/':
                next = url_for('dashboard')
            return redirect(next)
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                username=form.username.data,
                password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("dank voor registratie, je kan nu inloggen")
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

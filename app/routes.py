# app/routes.py

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User
from app.forms import LoginForm

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/users')
@login_required
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            print(f"User {user.username} logged in successfully.")
            print(f"Current user: {current_user.is_authenticated}")
            next_page = request.args.get('next')
            print(f"Next page: {next_page}")
            return redirect(next_page or url_for('main.users'))
        else:
            flash('Invalid username or password')
            print("Invalid username or password")
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@main.route('/status')
def status():
    return f"Authenticated: {current_user.is_authenticated}, User: {current_user}"

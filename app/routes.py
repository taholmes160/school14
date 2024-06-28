# app/routes.py

from flask import Blueprint, render_template
from app.models import User

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

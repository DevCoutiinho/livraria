from flask import Blueprint, render_template

auth_pages_bp = Blueprint('auth_pages', __name__)

@auth_pages_bp.get('/register')
def register_form():
    return render_template('auth/register.html')

@auth_pages_bp.get('/login')
def login_form():
    return render_template('auth/login.html')


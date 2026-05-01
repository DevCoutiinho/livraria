from flask import (Blueprint, flash, request, redirect, url_for, session)
from app.controllers import auth_controller

auth_bp = Blueprint('auth_routes', __name__, url_prefix='/auth')

@auth_bp.post('/register')
def register():
    data = request.form
    auth_controller.register(data)
    flash('Usuário cadastrado com sucesso!', 'success')
    return redirect(url_for('auth_pages.login_form'))

@auth_bp.post('/login')
def login():
    pass

@auth_bp.get('/logout')
def logout():
    pass

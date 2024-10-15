from flask import (
    Blueprint,
    render_template, request, redirect, url_for, flash, session, g
    )
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from todor import db 
import locale 
from datetime import datetime

bp = Blueprint('auth', __name__, url_prefix='/auth')

locale.setlocale(locale.LC_TIME, 'es_ES')

@bp.route('/register', methods = ('GET','POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        nombre = request.form['nombre']
        ape = request.form['ape']
        now = datetime.now()
        fechaIngreso = now.strftime("%Y-%m-%d %H:%M:%S")

        error = None 
        user = User(username, generate_password_hash(password), email, nombre, ape, fechaIngreso)
        user_name = User.query.filter_by(username=username).first()

        if user_name == None:
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('auth.login'))
        else:
            error = f'El usuario {username} ya esta registrado'
        
        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods = ('GET','POST'))

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        error = None 
        user = User.query.filter_by(username=username).first()

        if user == None:
            error = 'El usuario y/o contraseña incorrectos'
        elif not check_password_hash(user.password, password):
            error = 'El usuario y/o contraseña incorrectos'
        
        if error is None:
            session.clear()
            session['user_id']= user.id
            return redirect(url_for('todo.home'))
        
        flash(error)

        #return redirect(url_for('auth.login'))

    #return render_template('auth/login.html')
    return render_template('login/rms-login.html')

# Proceso para verificar si se ha iniciado sesion
@bp.before_app_request
def load_logged_in_user():
	user_id = session.get('user_id')
	
	if user_id is None:
		g.user = None
	else:
	    g.user = User.query.get_or_404(user_id)

# Proceso de cierre de sesion
@bp.route('/logout')
def logout():
     session.clear()
     return redirect(url_for('todo.index'))


#Proceso de verificacion de inicio o cierre de seion

import functools

def login_required(view):
     @functools.wraps(view)
     def wrapped_view(**kwargs):
          if g.user is None:
               return redirect(url_for('auth.login'))
          return view(**kwargs)
     return wrapped_view
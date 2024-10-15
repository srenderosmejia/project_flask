from flask import (
    Blueprint,
    render_template, request, redirect, url_for, flash, session, g
    )
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from todor import db 

bp = Blueprint('alerts', __name__, url_prefix='/alerts')

@bp.route('/', methods = ('GET','POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        nombre = request.form['nombre']
        ape = request.form['ape']

        error = None 
        user = User(username, generate_password_hash(password), email, nombre, ape)
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
            return redirect(url_for('alertas.alertas'))
        
        flash(error)

        #return redirect(url_for('auth.login'))

    return render_template('auth/login.html')

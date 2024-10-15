from flask import (
    Blueprint,
    render_template, request, redirect, url_for, flash, session, g
    )
from sqlalchemy import text
from werkzeug.security import generate_password_hash, check_password_hash
#from .models import Alertas
from .model_alertas import Alertas, AMLHistorialAlertsV2
from todor import db
import locale
from datetime import datetime
from .auth import load_logged_in_user


bp = Blueprint('todo', __name__, url_prefix='/todo')

from todor.auth import login_required

@bp.route('/home')
@login_required
def home():   
    return render_template('menu-collapsible.html')

"""
@bp.route('/index')
def index():   
    return render_template('index.html')
"""

@bp.route('/listalerts')
@login_required
def index_alertas():

    locale.setlocale(locale.LC_TIME, 'es_ES')

    """ 
    fecha1 = datetime(1,12,2023) #fecha1 = "01/12/2023" 
    fecha2 = datetime(31,12,2023) # fecha2 = "31/12/2023" 
    
    fecha_inicio = fecha1.strftime('%d/%m/%Y')
    fecha_fin = fecha2.strftime('%d/%m/%Y')

    """

    # Fechas en formato DD/MM/YYYY
    fecha1 = "01/12/2023"
    fecha2 = "31/12/2023"

# Convertir las fechas a objetos datetime
    fecha_inicio = datetime.strptime(fecha1, '%d/%m/%Y')
    fecha_fin = datetime.strptime(fecha2, '%d/%m/%Y')

# Convertir las fechas a cadenas en formato YYYY-MM-DD
    fecha_inicio_str = fecha_inicio.strftime('%Y-%m-%d')
    fecha_fin_str = fecha_fin.strftime('%Y-%m-%d')

# Consulta SQL con parámetros
    txtsql = text("SELECT * FROM AMLHistorialAlertsV2 WHERE dfecsis BETWEEN :fecha_inicio AND :fecha_fin")
    params = {'fecha_inicio': fecha_inicio_str, 'fecha_fin': fecha_fin_str}

    resultados = db.session.execute(txtsql, params).fetchall()
    registros = len(resultados)
    #return str(resultados)
    
    return render_template('alertas/list_alertas.html', resultados=resultados, registros=registros)

@bp.route('/segalertas')
@login_required
def segalertas():
    segalertas = Alertas.query.all()
    return render_template('alertas/segalertas.html', segalertas=segalertas)


@bp.route('/create', methods=('POST','GET'))
@login_required
def create_alertas():
    if request.method == 'POST':
        desAlerta = request.form['desAlerta']
        fechaAlerta = request.form['fechaAlerta']

        comentario = request.form['comentario']
        idTipoAlerta = int(request.form['idTipoAlerta'])
        usuarioCreacion = g.user.username
        now = datetime.now()
        fechaCreacion = now.strftime("%Y-%m-%d %H:%M:%S")

        alerta = Alertas(desAlerta, fechaAlerta, comentario, idTipoAlerta, usuarioCreacion, fechaCreacion)

        db.session.add(alerta)
        db.session.commit()

        return redirect(url_for('todo.segalertas'))

    return render_template('alertas/create_alertas.html')

@bp.route('/catalertas')
@login_required
def catalertas():

    txtsql = text("SELECT * FROM AMLAlertV2")
    
    resul_alertas = db.session.execute(txtsql).fetchall()
    registros = len(resul_alertas)
    
    return render_template('alertas/catalertas.html', resul_alertas=resul_alertas, registros=registros)
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


bp = Blueprint('clientes', __name__, url_prefix='/clientes')

from todor.auth import login_required

@bp.route('/clientes')
#@login_required
def clientes():   
    
    locale.setlocale(locale.LC_TIME, 'es_ES')

    """ 
    fecha1 = datetime(1,12,2023) #fecha1 = "01/12/2023" 
    fecha2 = datetime(31,12,2023) # fecha2 = "31/12/2023" 
    
    fecha_inicio = fecha1.strftime('%d/%m/%Y')
    fecha_fin = fecha2.strftime('%d/%m/%Y')



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
    txtsql = text("SELECT top 100 * FROM climide")
    #params = {'fecha_inicio': fecha_inicio_str, 'fecha_fin': fecha_fin_str}

    clientes = db.session.execute(txtsql).fetchall()
    registros = len(clientes)
        """
    return render_template('clientes/ingresoClientes.html') #, clientes=clientes, registros=registros)


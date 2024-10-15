from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeField, SubmitField
from wtforms.validators import DataRequired
from sqlalchemy import inspect
import urllib
from flask import Blueprint, render_template

bp = Blueprint('alertas', __name__, url_prefix='/alertas')


@bp.route('/add')
def register():
    return render_template('alertas/add_alerta.html')

@bp.route('/editar')
def login():
    return render_template('alertas/edit_alerta.html')


app = Flask(__name__)

# Configuración de la base de datos para SQL Server
params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=PAVILION\SQLEXPRESS;"
    "DATABASE=FOSOFAMILIA;"
    "UID=sa;"
    "PWD=Todoesposible2024$"
)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mssql+pyodbc:///?odbc_connect={params}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)

class Alertas(db.Model):
    idalerta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    desAlerta = db.Column(db.String(100), nullable=False)
    fechaAlerta = db.Column(db.DateTime, nullable=False)
    Comentario = db.Column(db.Text, nullable=True)
    idTipoAlerta = db.Column(db.Integer, nullable=False)
    usuarioCreacion = db.Column(db.String(25), nullable=False)
    fechaActualizacion = db.Column(db.DateTime, nullable=True)

class AlertaForm(FlaskForm):
    desAlerta = StringField('Descripción de la Alerta', validators=[DataRequired()])
    fechaAlerta = DateTimeField('Fecha de la Alerta', validators=[DataRequired()])
    Comentario = TextAreaField('Comentario')
    idTipoAlerta = StringField('ID Tipo de Alerta', validators=[DataRequired()])
    usuarioCreacion = StringField('Usuario de Creación', validators=[DataRequired()])
    fechaActualizacion = DateTimeField('Fecha de Actualización')
    submit = SubmitField('Submit')

@app.before_request
def create_tables():
    inspector = inspect(db.engine)
    if not inspector.get_table_names():
        db.create_all()

@app.route('/alertas')
def index():
    alertas = Alertas.query.all()
    return render_template('alertas/alertas.html', alertas=alertas)

@app.route('/add', methods=['GET', 'POST'])
def add_alerta():
    form = AlertaForm()
    if form.validate_on_submit():
        new_alerta = Alertas(
            desAlerta=form.desAlerta.data,
            fechaAlerta=form.fechaAlerta.data,
            Comentario=form.Comentario.data,
            idTipoAlerta=form.idTipoAlerta.data,
            usuarioCreacion=form.usuarioCreacion.data,
            fechaActualizacion=form.fechaActualizacion.data
        )
        db.session.add(new_alerta)
        db.session.commit()
        return redirect(url_for('alertas'))
    return render_template('alertas/add_alerta.html', form=form)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_alerta(id):
    alerta = Alertas.query.get_or_404(id)
    form = AlertaForm(obj=alerta)
    if form.validate_on_submit():
        alerta.desAlerta = form.desAlerta.data
        alerta.fechaAlerta = form.fechaAlerta.data
        alerta.Comentario = form.Comentario.data
        alerta.idTipoAlerta = form.idTipoAlerta.data
        alerta.usuarioCreacion = form.usuarioCreacion.data
        alerta.fechaActualizacion = form.fechaActualizacion.data
        db.session.commit()
        return redirect(url_for('alertas'))
    return render_template('alertas/edit_alerta.html', form=form)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_alerta(id):
    alerta = Alertas.query.get_or_404(id)
    db.session.delete(alerta)
    db.session.commit()
    return redirect(url_for('alertas'))

if __name__ == '__main__':
    app.run(debug=True)

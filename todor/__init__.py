from flask import Flask, render_template, session, send_from_directory
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
import urllib
from datetime import timedelta
import os


db = SQLAlchemy()

def create_app():

    
    app = Flask(__name__)

    # Cambiar permisos de un archivo
    #os.chmod('./assets', 0o644)
    # Permisos de lectura y escritura para el propietario, solo lectura para otros

    # Configuración de la base de datos para SQL Server

    """
    params = urllib.parse.quote_plus(
        "DRIVER={SQL Server Native Client 11.0};"
        "SERVER=192.168.5.156\SQLEXPRESS;"
        "DATABASE=FOSO_SIG;"
        "UID=sa;"
        "PWD=foso2024$12"
    )
    """
    params = urllib.parse.quote_plus(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=PAVILION\SQLEXPRESS;"
        "DATABASE=FOSOFAMILIA;"
        "UID=sa;"
        "PWD=Todoesposible2024$"
    )

    app.config['SQLALCHEMY_DATABASE_URI'] = f"mssql+pyodbc:///?odbc_connect={params}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)  # Tiempo de inactividad de 30 minutos
    app.config['SESSION_PERMANENT'] = True

    Session(app)

    @app.before_request
    def make_session_permanent():
        session.permanent = True
        app.permanent_session_lifetime = timedelta(minutes=30)

    #app.config['SECRET_KEY'] = 'your_secret_key'
 
    db.init_app(app)

    # Configuracion del proyecto
    
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'dev',
    )

    # Registrar Blueprint
    from . import clientes
    app.register_blueprint(clientes.bp)

    from . import todo 
    app.register_blueprint(todo.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def inicio():
        return render_template('base.html')
      
    with app.app_context():
        db.create_all()

    """ 
    def cambiar_permisos(ruta):
        for root, dirs, files in os.walk(ruta):
            for d in dirs:
                os.chmod(os.path.join(root, d), 0o755)
            for f in files:
                os.chmod(os.path.join(root, f), 0o644)

    cambiar_permisos('./assets/')
    """


    if __name__ == '__main__':
        app.run(debug=True)
        
    return app



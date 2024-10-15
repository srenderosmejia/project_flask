from datetime import datetime
from todor import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    nombre = db.Column(db.String(40))
    ape = db.Column(db.String(40))
    fechaIngreso = db.Column(db.DateTime, nullable=True)

    def __init__(self, username, password, email, nombre, ape, fechaIngreso):
        self.username = username
        self.password = password
        self.email = email
        self.nombre = nombre
        self.ape = ape
        self.fechaIngreso = fechaIngreso

    def __repr__(self):
        return f'<User {self.username}>'

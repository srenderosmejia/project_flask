from datetime import datetime
from todor import db

class Alertas(db.Model):
    idalerta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    desAlerta = db.Column(db.String(150), nullable=False)
    fechaAlerta = db.Column(db.DateTime, nullable=False)
    comentario = db.Column(db.Text)
    idTipoAlerta = db.Column(db.Integer, nullable=False)
    usuarioCreacion = db.Column(db.String(25), nullable=False)
    fechaActualizacion = db.Column(db.DateTime, nullable=True)

    def __init__(self, desAlerta, fechaAlerta, comentario, idTipoAlerta, usuarioCreacion, fechaActualizacion):
        self.desAlerta = desAlerta
        self.fechaAlerta = fechaAlerta
        self.comentario = comentario
        self.idTipoAlerta = idTipoAlerta
        self.usuarioCreacion = usuarioCreacion
        self.fechaActualizacion = fechaActualizacion
    
    def __repr__(self):
        return f'<Alertas {self.desAlerta}>'

class AMLHistorialAlertsV2(db.Model):
    idAlerta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ccodcta = db.Column(db.String(18), nullable=True)
    ccodcli = db.Column(db.String(12), nullable=True)
    cnomcli = db.Column(db.String(150), nullable=True)
    numalert = db.Column(db.String(5), nullable=True)
    nalart = db.Column(db.Text)
    monto = db.Column(db.Numeric(12, 2), nullable=True)
    ctippag = db.Column(db.String(40), nullable=True)
    dfecsis = db.Column(db.DateTime, nullable=True)

    def __init__(self, ccodcta, ccodcli, cnomcli, numalert, nalart, monto,ctippag, dfecsis):
        self.ccodcta = ccodcta
        self.ccodcli = ccodcli
        self.cnomcli = cnomcli
        self.numalert = numalert
        self.nalart = nalart
        self.monto = monto
        self.ctippag = ctippag
        self.dfecsis = dfecsis
    
    def __repr__(self):
        return f'<Alertas {self.cnomcli}>'


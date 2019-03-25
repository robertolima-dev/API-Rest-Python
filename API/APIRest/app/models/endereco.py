from app import db
from app import manager

class Endereco(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    logradouro = db.Column(db.String(100))
    numero = db.Column(db.Integer)
    bairro = db.Column(db.String(50))

db.create_all()
manager.create_api(Endereco, methods=['GET', 'POST', 'PUT', 'DELETE'])

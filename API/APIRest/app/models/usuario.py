from app import db
from app import manager

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    nascimento = db.Column(db.DateTime)
    rg = db.Column(db.String(20))
    email = db.Column(db.String(20), unique=True)

    endereco_id = db.Column(db.Integer, db.ForeignKey('endereco.id'))
    endereco = db.relationship('Endereco')

db.create_all()
manager.create_api(Cliente, methods=['POST', 'GET', 'PUT', 'DELETE'])

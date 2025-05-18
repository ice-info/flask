# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Shoe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    brand = db.Column(db.String(50))
    price = db.Column(db.Float)
    size = db.Column(db.String(10))
    stock = db.Column(db.Integer)

    def __repr__(self):
        return f'<Shoe {self.name}>'


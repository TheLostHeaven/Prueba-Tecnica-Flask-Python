from src.utils.db import db
import datetime

class Tours(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120),  nullable=False)
    date = db.Column(db.DateTime, default= datetime.datetime.now, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    reserves = db.relationship('Reserves', backref='tour', lazy=True)

    def __init__(self, name, date, description, price):
        self.name = name
        self.description = description
        self.date = date
        self.price = price

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'date': self.date,
            'price': self.price
        }
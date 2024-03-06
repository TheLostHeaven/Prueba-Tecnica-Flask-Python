from src.utils.db import db
from src.models.tours import Tours
from src.utils.dicts import STATUS_DICT

class Reserves(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, unique=True, nullable=False)
    people = db.Column(db.Integer, nullable=False)
    tours_id = db.Column(db.Integer, db.ForeignKey('tours.id'))
    status = db.Column(db.Integer, default=1)

    def __init__(self, user_id, tours_id, date, people, status):
        self.user_id = user_id
        self.tours_id = tours_id
        self.date = date
        self.people = people
        self.status = status

    @property
    def status_description(self):
        return STATUS_DICT.get(self.status, 'Estado desconocido')

    @property
    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'date': self.date.strftime('%Y-%m-%d'),
            'people': self.people,
            'tours_id': self.tours_id,
            'status': self.status,
            'status_description': self.status_description
        }

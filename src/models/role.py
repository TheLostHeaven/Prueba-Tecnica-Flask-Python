from src.utils.db import db
from src.models.user import User

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    code = db.Column(db.String(20), unique=True, nullable=False)

def __init__(self, name, code):
    self.name = name
    self.code = code

    @property
    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'code': self.code,
        }
    
from src.utils.db import db
from src.models.user import User

class RoleTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

def __init__(self, user_id, role_id):
    self.user_id = user_id,
    self.role_id = role_id
    

    @property
    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'code': self.code,
        }
    
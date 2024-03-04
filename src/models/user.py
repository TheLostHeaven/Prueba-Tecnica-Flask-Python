from src.utils.db import db
import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    fullname = db.Column(db.String(50),)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, default= datetime.datetime.now)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    reserves = db.relationship('Reserves', backref='user', lazy=True, cascade="all,delete")


    def __init__(self, username, fullname, email, password, role_id):
        self.username = username
        self.fullname = fullname
        self.email = email
        self.password = password
        self.role_id = role_id  


    @property
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'fullname': self.fullname,
            'email': self.email,
            'date': self.date,
            'role_id': self.role_id,
        } 
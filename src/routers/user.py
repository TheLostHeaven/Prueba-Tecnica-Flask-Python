from flask import Blueprint, request, jsonify, current_app
from src.models.user import User
from src.models.role import Role
from src.utils.db import db
from src.utils.checkrole import admin_required
from werkzeug.security import generate_password_hash
import jwt

user = Blueprint('user', __name__)

#GetUser
@user.route('/dashboard/users', methods=['GET'])
@admin_required
def get_users():
    try: 
        users = User.query.all()
        return jsonify([user.serialize for user in users])
    except Exception as err:
        return jsonify(err=str(err)), 500
    
#GetForID
@user.route('/dashboard/users/<int:id>', methods=['GET'])
@admin_required
def get_users_id(id):
    try:
        user = User.query.get(id)
        if user is None:
            return jsonify({'message': 'user not found'}), 404
        return jsonify(user.serialize)
    except Exception as err:
        return jsonify(err=str(err)),500

#Create
@user.route('/dashboard/users/', methods=['POST'])
@admin_required
def create_user():
    try:
        data = request.get_json()
        if request.method == 'POST':
            username = data['username']
            fullname = data['fullname']
            email = data['email']
            password = data['password']

            user_exist = User.query.filter_by(username=username).first()
            email_exist = User.query.filter_by(email=email).first()
            if user_exist:
                return 'User exists in the DataBase'
            if email_exist:
                return 'User exists in the DataBase'
        admin_role_id = 1


        new_user = User(username=data['username'], fullname=data['fullname'], email=data['email'], password=generate_password_hash(password), role_id=admin_role_id)
        db.session.add(new_user)
        db.session.commit()
        token = jwt.encode({'username': username}, current_app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token}), 201
    except Exception as err:
        return jsonify(err=str(err)),500
    

#Delete
@user.route('/dashboard/users/<int:id>', methods=['DELETE'])
@admin_required
def delete_users(id):
    try:
        user = User.query.get(id)
        if user is None:
            return jsonify({'message': 'user not found'}), 404
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User delete to DB!'})
    except Exception as err:
        return jsonify(err=str(err)),500
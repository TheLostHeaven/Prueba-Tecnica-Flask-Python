#jsonify 
from flask import Blueprint, request, redirect, jsonify, current_app
from src.models.user import User
from src.utils.db import db
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

auth = Blueprint('auth', __name__)

#Register
@auth.route('/register', methods=['GET', 'POST'])
def auth_register():
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
        
            new_user = User(username=username, fullname=fullname, email=email, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()

            token = jwt.encode({'username': username}, current_app.config['SECRET_KEY'], algorithm='HS256')
            return jsonify({'token': token}), 201

    except Exception as err:
        return jsonify(err=str(err)),500


#Login
@auth.route('/login', methods=['GET', 'POST'])
def auth_login():
    try:
        if request.method == 'POST':
            data = request.get_json()
            login = data['login']
            password = data['password']

            user = User.query.filter((User.username == login) | (User.email == login)).first()

            if user and check_password_hash(user.password, password):
                token = jwt.encode({'username': user.username}, current_app.config['SECRET_KEY'], algorithm='HS256')

                return jsonify({'token': token}), 200
            else:
                return jsonify({'message': 'Credenciales incorrectas. Inténtalo de nuevo.'}), 401
        
        return jsonify({'message': 'Método no permitido'}), 405
    
    except Exception as err:
        return jsonify({'error': str(err)}), 500


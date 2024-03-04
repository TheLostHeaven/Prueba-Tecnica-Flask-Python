from src.utils.db import db
from src.models.role import Role
from src.models.user import User
from flask import Flask, jsonify
from config import username,email,fullname,password_admin, role_id
from werkzeug.security import generate_password_hash
import os 

#Create Roles for Users
def create_roles():
    try:
    # Crea los roles si no existen
        admin_role = Role.query.filter_by(code='admin').first()
        user_role = Role.query.filter_by(code='user').first()

        if admin_role is None:
            admin_role = Role(name='Admin', code='admin')
            db.session.add(admin_role)

        if user_role is None:
            user_role = Role(name='User', code='user')
            db.session.add(user_role)

        db.session.commit()

    except Exception as err:
        return jsonify(err=str(err)),500


#Create User Admin in DB
def create_admin_user():
    try:
    # Verifica si el usuario administrador ya existe
        admin_user = User.query.filter_by(username=username).first()
        if admin_user is None:
            password_admin = os.getenv('ADMIN_PASSWORD')
            if password_admin is None:
                print("Not found admin password in the enviroment")
                return
            
        # Crea un nuevo usuario administrador
            hashed_password = generate_password_hash(password_admin)
            new_admin = User(
                username=username,
                fullname=fullname,
                email=email,
                password=hashed_password,
                role_id=role_id
            )
            db.session.add(new_admin)

        db.session.commit()

    except Exception as err:
        print(f"Error to create admin user: {err}")


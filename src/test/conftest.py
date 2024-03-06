import pytest
from src.utils.db import db
from app import app_create
import time
from src.utils.rolecreate import create_roles
from sqlalchemy import text
from config import DATABASE_CONNECTION_URI_TEST

@pytest.fixture(scope='session')
def app():
    app = app_create()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI_TEST
    with app.app_context():
        db.create_all()
        create_roles()
        yield app
        db.session.remove()
        time.sleep(20)
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def cleanup_database(app):
    print("Limpiando la base de datos...")
    with app.app_context():
        time.sleep(20)
        with db.session.begin():
            db.session.execute(text("SET foreign_key_checks = 0"))
            db.session.execute(text("DELETE FROM user"))

            db.session.execute(text("SET foreign_key_checks = 1"))
        db.session.commit()
    print("Limpieza de la base de datos completada")
import pytest
from flask import url_for
from app import app_create

#Register
@pytest.fixture
def client():
    app = app_create()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_register(client):
    data = {'email':'correo@gmail2.com', 'fullname':'nombreee2', 'password': 'contrasena_test', 'username': 'usuario_test2'}
    print("Datos enviados:", data) 
    response = client.post('/register', json=data)
    json_data = response.get_json()

    assert response.status_code == 201
    assert json_data['token'] is not None


#Login
def test_login(client):
    data = {'password': 'contrasena_test', 'login': 'usuario_test2'}
    print("Datos enviados:", data) 
    response = client.post('/login', json=data)
    json_data = response.get_json()

    assert response.status_code == 200
    assert json_data['token'] is not None
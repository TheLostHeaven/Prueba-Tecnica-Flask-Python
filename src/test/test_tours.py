from src.models.tours import Tours
from src.utils.db import db

#CREATE
def test_create_tour(client):
    response = client.post('/tours', json={
        'name': 'Tour1',
        'date': '2024-03-05',
        'description': 'Descripción del tour',
        'price': 100
    })
    assert response.status_code == 201 
    assert Tours.query.count() == 1     
    db.session.commit()

#GET
def test_get_tours(client):
    response = client.get('/tours')
    assert response.status_code == 200  
    assert len(response.json) == 1

#UPDATE
def test_update_tour(app, client):
    with app.app_context():
        test_id = 1
        updated_tour_data = {
            "name": "Tour por argentina",
            "date": "2016-02-02",
            "description" : "aaaaaa",
            "price" : 500
        }

        response = client.put(f'/tours/{test_id}', json=updated_tour_data)

        data = response.get_json()

        assert response.status_code == 200
        assert 'name' in data
        assert data['name'] == updated_tour_data['name']
        assert str(data['date']) == str(updated_tour_data['date'])
        assert data['description'] == updated_tour_data['description']
        assert data['price'] == updated_tour_data['price']



#DELETE
def test_delete_tour(app, client):
    with app.app_context():

        tour_id = 1

        response = client.delete(f'/tours/{tour_id}')

        assert response.status_code == 200
        assert 'message' in response.json
        assert response.json['message'] == 'Tour Successfully Eliminated!'
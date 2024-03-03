from flask import Blueprint, request, jsonify
from src.models.tours import Tours
from src.utils.db import db
from src.utils.checktoken import token_required
from src.utils.checkrole import admin_required

tours = Blueprint('tours', __name__)

#Create
@tours.route('/tours', methods=['POST'])
@admin_required
def create_tour():
    try:
        data = request.get_json()
        new_tour = Tours(name=data['name'], date=data['date'], description=data['description'], price=data['price'])
        db.session.add(new_tour)
        db.session.commit()
        return jsonify({'message': 'Tour creado exitosamente!'}), 201
    except Exception as err:
        return jsonify(err=str(err)),500

#Get
@tours.route('/tours', methods=['GET'])
@token_required
def get_tours(current_user):
    try:
        tours = Tours.query.all()
        return jsonify([tour.serialize for tour in tours])
    except Exception as err:
        return jsonify(err=str(err)),500

#GetForID
@tours.route('/tours/<int:id>', methods=['GET'])
@token_required
def get_tour(current_user, id):
    try:
        tour = Tours.query.get(id)
        if tour is None:
            return jsonify({'message': 'Tour no encontrado'}), 404
        return jsonify(tour.serialize)
    except Exception as err:
        return jsonify(err=str(err)),500

#UpdateForID
@tours.route('/tours/<int:id>', methods=['PUT'])
@admin_required
def update_tour(id):
    try:
        data = request.get_json()
        tour = Tours.query.get(id)
        if tour is None:
            return jsonify({'message': 'Tour no encontrado'}), 404
        tour.name = data['name']
        tour.date = data['date']
        tour.description = data['description']
        tour.price = data['price']
        db.session.commit()
        return jsonify({'message': 'Tour actualizado exitosamente!'})
    except Exception as err:
        return jsonify(err=str(err)),500
    
#DeleteForID
@tours.route('/tours/<int:id>', methods=['DELETE'])
@admin_required
def delete_tour(id):
    try:
        tour = Tours.query.get(id)
        if tour is None:
            return jsonify({'message': 'Tour no encontrado'}), 404
        db.session.delete(tour)
        db.session.commit()
        return jsonify({'message': 'Tour eliminado exitosamente!'})
    except Exception as err:
        return jsonify(err=str(err)),500
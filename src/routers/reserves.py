from flask import Blueprint, request, jsonify
from src.utils.checktoken import token_required
from src.models.reserves import Reserves
from src.utils.db import db
from src.utils.dicts import STATUS_DICT

reserve = Blueprint('reserve', __name__)

#Create
@reserve.route('/reserve', methods=['POST'])
@token_required
def createReserve(current_user):
    try:
        data = request.get_json()
        status = data.get('status', 1)
        new_reserve = Reserves(user_id=current_user.id, tours_id=data['tours_id'], date=data['date'], people=data['people'], status=status)
        db.session.add(new_reserve)
        db.session.commit()
        return jsonify({'message': 'Reserva creada exitosamente!'}), 201
    except Exception as err:
        return jsonify(err=str(err)),500

#Get
@reserve.route('/reserve', methods=['GET'])
@token_required
def get_reserve(current_user):
    try:
        reserves = Reserves.query.all()
        return jsonify([reserve.serialize for reserve in reserves])
    except Exception as err:
        return jsonify(err=str(err)), 500

#Update

# @reserve.route
@reserve.route('/reserve/<int:id>', methods=['PUT'])
@token_required
def updateReserve(current_user, id):
    try:
        data = request.get_json()
        reserve = Reserves.query.get(id)
        if not reserve:
            return jsonify({'message': 'Reserva no encontrada'}), 404

        # Lista de campos permitidos para actualizar
        allowed_fields = ['date', 'people', 'status']

        for key, value in data.items():
            if key in allowed_fields:
                if key == 'status' and value not in STATUS_DICT:
                    return jsonify({'message': 'Estado no válido'}), 400
                setattr(reserve, key, value)

        db.session.commit()
        return jsonify({'message': 'Reserva actualizada exitosamente!'}), 200
    except Exception as err:
        return jsonify(err=str(err)),500
from flask import request, jsonify, current_app
import jwt
from src.models.user import User
from functools import wraps


def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token-admin')
        if not token:
            return jsonify({'message': 'Token Not Provided'}), 403
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms='HS256')
            if data['role_id'] != 1:
                return jsonify({'message': 'Required administrater rol'}), 403
        except:
            return jsonify({'message': 'Invalid Token'}), 403
        return f(*args, **kwargs)
    return decorated
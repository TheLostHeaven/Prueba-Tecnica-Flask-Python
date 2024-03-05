from flask import request, jsonify, current_app
import jwt
from src.models.user import User
from functools import wraps


def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Si estamos en un entorno de prueba, permitimos el paso sin verificar el token de administrador
        if current_app.config.get('TESTING'):
            return f(*args, **kwargs)
        
        token = request.headers.get('x-access-token-admin')
        if not token:
            return jsonify({'message': 'Token Not Provided'}), 403
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms='HS256')
            if data['role_id'] != 1:
                return jsonify({'message': 'Required administrator role'}), 403
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid Token'}), 403
        return f(*args, **kwargs)
    return decorated

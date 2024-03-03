import jwt
from datetime import datetime, timedelta
from config import jwtKey

def generate_jwt(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(days=1)
    }
    secret_key = jwtKey
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token
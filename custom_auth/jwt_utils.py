import jwt
from datetime import datetime, timedelta
from django.conf import settings

def create_access_token(user_id: int) -> str:
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow(),
        'key': 'k3jkdn1njnjdsn1n2jn31njnj2'
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

def decode_access_token(token) -> list:
    return jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
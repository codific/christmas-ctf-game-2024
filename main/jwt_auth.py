from ninja.security import HttpBearer
from custom_auth.jwt_utils import decode_access_token


class JWTAuth(HttpBearer):
    def authenticate(self, request, token):
        if self.validate_jwt(token):
            return True
        return None

    def validate_jwt(self, token):
        try:
            decoded = decode_access_token(token)
            return 'user_id' in decoded
        except Exception:
            return False
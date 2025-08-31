from django.contrib.auth import get_user_model, authenticate
from django.http import HttpRequest
from ninja import Router
from ninja.responses import JsonResponse
from .schemas import LoginSchema, TokenSchema
from .jwt_utils import create_access_token

User = get_user_model()
router = Router()


@router.post("/login", response={200: TokenSchema, 401: dict})
def login(request: HttpRequest, credentials: LoginSchema):
    user = authenticate(username=credentials.username, password=credentials.password)
    if user is None:
        return JsonResponse({"detail": "Invalid credentials"}, status=401)

    access_token = create_access_token(user.id)
    return JsonResponse({"access_token": access_token, "token_type": "bearer"}, status=200)

import shlex
import subprocess
from typing import Optional

from ninja import NinjaAPI, Router, Query
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from ninja.errors import HttpError
from ninja.responses import Response
from main.schemas import UserOut, PasswordSchema, UserSchema
from main.jwt_auth import JWTAuth

router = Router()
api = NinjaAPI()
User = get_user_model()


@api.get("/users/{user_id}", response=UserOut)
def get_user(request, user_id: int):
    user = get_object_or_404(User, id=user_id)
    return user


@api.get('/user/info', auth=JWTAuth())
def user_info(request):
    return {"url": '/api/secret-panel'}


@api.get('/secret-panel', auth=JWTAuth(), include_in_schema=False)
def user_info(request):
    return {"secret": 'TDJGd2FTOWxibU52WkdWa0xYVnliQT09'}


@api.get('/encoded-url', auth=JWTAuth(), include_in_schema=False)
def user_info(request):
    response = Response(
        {
            "message": "01001101 01100001 01111001 00100000 01110100 01101000 01100101 00100000 01100110 01101111 01110010 01100011 01100101 00100000 01100010 01100101 00100000 01110111 01101001 01110100 01101000 00100000 01111001 01101111 01110101 00101100 00100000 01100001 01101100 01110111 01100001 01111001 01110011"},
        headers={
            "Cache-Control": "/api/cached-url"
        }
    )
    return response


@api.get('/cached-url', auth=JWTAuth(), include_in_schema=False)
def user_info(request, key: Optional[str] = Query(None)):
    if key != "k3jkdn1njnjdsn1n2jn31njnj2":
        return {"message": "No key supplied in URL query string. I won't decode it myself"}
    return {"message": "/api/non-cached-url"}


@api.get('/non-cached-url', auth=JWTAuth(), include_in_schema=False)
def user_info(request):
    return {
        "message": "Send me the password in JSON via POST. TIP: You you don't know it. {'password': '...'}"}


@api.post('/non-cached-url', auth=JWTAuth(), include_in_schema=False)
def user_info(request, payload: PasswordSchema):
    password = "noodles"
    if payload.password == password:
        return {"message": "/api/almost-done-url"}
    raise HttpError(400, 'Invalid password')


@api.get('/almost-done-url', auth=JWTAuth(), include_in_schema=False)
def user_info(request):
    return {"message": "User object needs to be created via POST"}


@api.post('/almost-done-url', auth=JWTAuth(), include_in_schema=False)
def user_info(request, payload: UserSchema):
    result = ""
    if payload.avatar is not None:
        try:
            command_list = shlex.split(payload.avatar)
            result = subprocess.run(command_list, capture_output=True, text=True).stdout
        except Exception:
            result = payload.avatar
    return {"message": "User created. Avatar content: " + result}

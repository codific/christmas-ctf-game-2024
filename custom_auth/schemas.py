from ninja import Schema

class LoginSchema(Schema):
    username: str
    password: str

class TokenSchema(Schema):
    access_token: str
    token_type: str
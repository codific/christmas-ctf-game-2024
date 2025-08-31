from ninja import Schema
from pydantic import EmailStr
from typing import Optional

class UserOut(Schema):
    id: int
    username: str
    avatar: Optional[str]
    email: EmailStr

class PasswordSchema(Schema):
    password: str

class UserSchema(Schema):
    username: str
    password: str
    is_admin: bool
    firstname: str
    lastname: str
    city: str
    avatar: Optional[str] = None



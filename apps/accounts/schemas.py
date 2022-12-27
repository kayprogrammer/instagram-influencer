from pydantic import BaseModel, validator
from typing import Optional
import re

from . models import User

class RegisterSchema(BaseModel):
    email: str
    username: str
    password1: str
    password2: str
    followers_count: int
    bio: Optional[str]

    class Config:
        orm_mode = True

    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password1' in values and v != values['password1']:
            raise ValueError('Passwords do not match')
        return v

    @validator('email')
    def validate_email(cls, v):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if not re.fullmatch(regex, v):
            raise ValueError("Invalid email")
        return v

    @validator('bio')
    def validate_bio(cls, v):
        if len(bio) > 100:
            raise ValueError('Bio must not exceed 100 characters')
        return v

class DisplayUsersSchema(BaseModel):
    username: str
    email: str
    bio: Optional[str]
    followers_count: int

    class Config:
        orm_mode = True
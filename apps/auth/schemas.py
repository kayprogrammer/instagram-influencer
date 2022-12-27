from pydantic import BaseModel, validator
from typing import Optional
import re

class UserSchema(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True

    
    @validator('email')
    def validate_email(cls, v):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if not re.fullmatch(regex, v):
            raise ValueError("Invalid email")
        return v

class RefreshTokenSchema(BaseModel):
    refresh: str

    class Config:
        orm_mode = True
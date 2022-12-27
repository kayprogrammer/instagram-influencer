from fastapi import Request, APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import List

from . schemas import UserSchema, RefreshTokenSchema
from . models import User, Jwt
from . hashers import Hasher
from . utils import get_access_token, get_refresh_token, verify_token, decodeJWT

from setup.database import get_db

authrouter = APIRouter(tags=['auth'])

oauth = OAuth2PasswordBearer(tokenUrl = "/login", scheme_name="JWT")

async def get_current_user(token: str = Depends(oauth), db: Session = Depends(get_db)):
    user = decodeJWT(db, token) # check access token validity. returns user object or None
    if not user:
        raise HTTPException(status_code = 401, detail='Signature invalid or expired')

    return user

@authrouter.post('/register')
async def register(request: Request, user: UserSchema, db: Session = Depends(get_db), status_code = status.HTTP_201_CREATED):
    try:
        new_user = User.create_user(db=db, **user.dict()) # create user based on defined method in UserManager class in managers.py file
    except Exception as e: # return any possible exception
        print(e)
        raise HTTPException(status_code=400, detail=str(e))
    return {'user': user, 'message': 'Registration successful'}

@authrouter.post('/login')
async def login(request: Request, user: UserSchema, db: Session = Depends(get_db), status_code = status.HTTP_201_CREATED):
    user_obj = db.query(User).filter_by(email=user.email).first() # get user object from db based on email
    if not user_obj:
        raise HTTPException(status_code=400, detail='Invalid Credentials')
    password_check = Hasher.verify_password(user.password, user_obj.password) 
    if password_check == False:
        raise HTTPException(status_code=400, detail='Invalid Credentials')

    db.query(Jwt).filter_by(user_id=user_obj.id).delete() # delete existing jwt objects of that user before creating a new one 

    # create new tokens
    access = get_access_token({"user_id": user_obj.id})
    refresh = get_refresh_token()

    jwt = Jwt(user_id=user_obj.id, access=access, refresh=refresh)
    db.add(jwt)
    db.commit()
    return {'access': access, 'refresh': refresh}

@authrouter.post('/refresh')
async def refresh(request: Request, token: RefreshTokenSchema, db: Session = Depends(get_db), status_code = status.HTTP_201_CREATED):
    active_jwt = db.query(Jwt).filter_by(refresh=token.refresh).first() # gets jwt object from db
    if not active_jwt:
        raise HTTPException(status_code=400, detail='refresh token not found')

    token_valid = verify_token(token.refresh) # returns true or false

    if not token_valid:
        raise HTTPException(status_code=400, detail='refresh token is invalid or expired')

    # create new tokens

    access = get_access_token({'user_id': active_jwt.user_id})
    refresh = get_refresh_token()

    active_jwt.access = access
    active_jwt.refresh = refresh
    db.commit()

    return {'access': access, 'refresh': refresh}

@authrouter.get('/logout')
async def logout(request: Request, db: Session = Depends(get_db), user: User = Depends(get_current_user), status_code = status.HTTP_200_OK):
    # delete existing jwts
    db.query(Jwt).filter_by(user_id = user.id).delete()
    db.commit()
    return {'message': 'Logged out successfully'}

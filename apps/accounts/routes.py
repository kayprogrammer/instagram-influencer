from fastapi import Request, APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . schemas import RegisterSchema, DisplayUsersSchema
from . models import User

from setup.database import get_db

accountsrouter = APIRouter(tags=['accounts'])

@accountsrouter.post('/register')
async def register(request: Request, user: RegisterSchema, db: Session = Depends(get_db), status_code = status.HTTP_201_CREATED):
    try:
        new_user = User.create_user(db=db, **user.dict())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {'user': user, 'message': 'Registration successful'}

@accountsrouter.post('/register')
async def login(request: Request, user: RegisterSchema, db: Session = Depends(get_db), status_code = status.HTTP_201_CREATED):
    try:
        new_user = User.create_user(db=db, **user.dict())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {'user': user, 'message': 'Registration successful'}


@accountsrouter.get('/register2', response_model = List[DisplayUsersSchema])
async def register2(request: Request, db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

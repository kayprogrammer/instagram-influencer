from fastapi import Depends
from setup.database import get_db
from sqlalchemy.orm import Session
from . hashers import Hasher

class UserManager(object):
    @classmethod
    def create_user(cls, db: Session , **kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password1')
        existing_user = db.query(cls).filter_by(email=email).first()

        if existing_user:
            raise ValueError('Email address already registered')

        kwargs['password'] = Hasher.get_password_hash(password)
        kwargs.pop('password1', None)
        kwargs.pop('password2', None)

        obj = cls(**kwargs)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        obj.password = None
        return obj


from sqlalchemy import Column, Integer, DateTime, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from setup.database import Base
from datetime import datetime

from . managers import UserManager

class User(UserManager, Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    username = Column(String(), nullable=True, unique=True)
    email = Column(String(), nullable=False, unique=True)
    password = Column(String(), nullable=False)
    followers_count = Column(Integer(), default=0, nullable=True)
    bio = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'{self.username}'

class Jwt(Base):
    __tablename__ = 'jwt'
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.id', ondelete='CASCADE'), unique=True)
    access = Column(Text())
    refresh = Column(Text())
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Access - {self.access} | Refresh - {self.refresh}'
from sqlalchemy import Column, Integer, DateTime, String, Text
from setup.database import Base
from datetime import datetime

from . managers import UserManager

class User(UserManager, Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    username = Column(String(), nullable=False)
    email = Column(String(), nullable=False, unique=True)
    password = Column(String(), nullable=False)
    followers_count = Column(Integer(), default=0, nullable=False)
    bio = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'{self.name}'
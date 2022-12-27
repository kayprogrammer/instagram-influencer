from fastapi import Request, APIRouter
from setup.database import get_db

searchrouter = APIRouter(tags=['search'])

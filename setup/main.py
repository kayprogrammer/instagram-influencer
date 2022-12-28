from fastapi import FastAPI
from fastapi.testclient import TestClient

from . database import engine
from . database import Base
from . settings import *

from apps.auth.routes import authrouter
from apps.influencers.routes import influencersrouter

app = FastAPI()

client = TestClient(app=app)

Base.metadata.create_all(bind=engine)

app.include_router(authrouter, prefix='/api/v1/auth')
app.include_router(influencersrouter, prefix='/api/v1/influencers')


from fastapi import FastAPI
from . database import engine
from . database import Base
from . settings import *

from apps.accounts.routes import accountsrouter
from apps.search.routes import searchrouter

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(accountsrouter, prefix='/api/v1/accounts')
app.include_router(searchrouter, prefix='/api/v1/search')


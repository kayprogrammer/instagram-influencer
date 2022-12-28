from decouple import config # for getting variables from .env file
from pathlib import Path

SECRET_KEY = config('SECRET_KEY')

# Postgres Database details
DATABASES = {
    "DB_NAME": config("POSTGRES_DB"),
    "USER": config("POSTGRES_USER"),
    "PASSWORD": config("POSTGRES_PASSWORD"),
    "HOST": config("PG_HOST"),
    "PORT": config("PG_PORT"),
}

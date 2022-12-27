from decouple import config
from pathlib import Path

SECRET_KEY = config('SECRET_KEY')

DATABASES = {
    "DB_NAME": config("POSTGRES_DB"),
    "USER": config("POSTGRES_USER"),
    "PASSWORD": config("POSTGRES_PASSWORD"),
    "HOST": config("PG_HOST"),
    "PORT": config("PG_PORT"),
}

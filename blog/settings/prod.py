from .settings import *
from dotenv import load_dotenv, find_dotenv
import os

_ = load_dotenv(find_dotenv())

SECRET_KEY = os.getenv("SECRET_KEY")

ALLOWED_HOSTS = [os.getenv("ALLOWED_HOST1")]

DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE"),
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}


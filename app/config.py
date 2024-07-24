import os

from dotenv import load_dotenv


load_dotenv()


class Config:
    SITE_PORT = int(os.environ['SITE_PORT'])
    POSTGRES_HOST = os.environ['POSTGRES_HOST']
    POSTGRES_PORT = int(os.environ['POSTGRES_PORT'])
    POSTGRES_DB = os.environ['POSTGRES_DB']
    POSTGRES_USER = os.environ['POSTGRES_USER']
    POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
    AUTH_SECRET = os.environ['AUTH_SECRET']
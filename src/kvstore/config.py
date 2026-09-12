"""Responsible for the database configuration"""

import os

from dotenv import load_dotenv

load_dotenv()


def get_database_url():
    database_url = os.getenv("DATABASE_URL")
    if database_url is None:
        raise RuntimeError("DATABASE_URL is not set")
    return database_url

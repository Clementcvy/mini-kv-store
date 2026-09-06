"""Responsible for the database connection"""

import psycopg
from kvstore.config import Config


def get_connection():
    return psycopg.connect(Config.DATABASE_URL)

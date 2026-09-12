"""Responsible for the database connection"""

import psycopg

from kvstore.config import get_database_url


def get_connection():
    return psycopg.connect(get_database_url())

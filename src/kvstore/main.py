import logging

from fastapi import FastAPI, HTTPException
from psycopg import Error

from kvstore.db import get_connection
from kvstore.logging_config import setup_logging
from kvstore.repository import Repository
from kvstore.schemas import KeyValueResponse, SetValueRequest
from kvstore.service import (
    InvalidKeyError,
    InvalidValueError,
    KeyNotFoundError,
    Service,
)

setup_logging()

logger = logging.getLogger(__name__)

logger.info("event=application_started")


app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.put("/v1/kv/{key}", status_code=200, response_model=KeyValueResponse)
def put(key, body: SetValueRequest):
    try:
        with get_connection() as conn:
            repo = Repository(conn)
            serv = Service(repo, conn)
            serv.set_value(key, body.value)
    except InvalidKeyError:
        logger.warning("event=invalid_key_error key=%s", key)
        raise HTTPException(status_code=400, detail="Bad Request")
    except InvalidValueError:
        logger.warning("event=invalid_value_error key=%s", key)
        raise HTTPException(status_code=400, detail="Bad Request")
    except Error:
        logger.exception("event=database_error operation=set key=%s", key)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    logger.info("event=kv_set key=%s", key)
    return KeyValueResponse(key=key, value=body.value)


@app.get("/v1/kv/{key}", status_code=200, response_model=KeyValueResponse)
def get(key):
    try:
        with get_connection() as conn:
            repo = Repository(conn)
            serv = Service(repo, conn)
            read_value = serv.get_value(key)
    except InvalidKeyError:
        logger.warning("event=invalid_key_error key=%s", key)
        raise HTTPException(status_code=400, detail="Bad Request")
    except KeyNotFoundError:
        logger.warning("event=key_not_found key=%s", key)
        raise HTTPException(status_code=404, detail="Not Found")
    except Error:
        logger.exception("event=database_error operation=get key=%s", key)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    logger.info("event=kv_get key=%s", key)
    return KeyValueResponse(key=key, value=read_value)


@app.delete("/v1/kv/{key}", status_code=204)
def delete(key):
    try:
        with get_connection() as conn:
            repo = Repository(conn)
            serv = Service(repo, conn)
            serv.delete_value(key)
    except InvalidKeyError:
        logger.warning("event=invalid_key_error key=%s", key)
        raise HTTPException(status_code=400, detail="Bad Request")
    except KeyNotFoundError:
        logger.warning("event=key_not_found key=%s", key)
        raise HTTPException(status_code=404, detail="Not Found")
    except Error:
        logger.exception("event=database_error operation=delete key=%s", key)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    logger.info("event=kv_delete key=%s", key)

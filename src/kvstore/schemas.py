from pydantic import BaseModel


class SetValueRequest(BaseModel):
    value: str


class KeyValueResponse(BaseModel):
    key: str
    value: str

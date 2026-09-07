class InvalidKeyError(ValueError):
    pass


class InvalidValueError(ValueError):
    pass


class KeyNotFoundError(ValueError):
    pass


class Service:
    def __init__(self, repository, conn):
        self.repository = repository
        self.conn = conn

    def set_value(self, key, value):
        if key is None:
            raise InvalidKeyError("Key cannot be None")
        if len(key) > 128:
            raise InvalidKeyError("Key too long")
        if value is None:
            raise InvalidValueError("Value cannot be None")
        if len(value) > 4096:
            raise InvalidValueError("Value too long")
        with self.conn.transaction():
            return self.repository.set(key, value)

    def get_value(self, key):
        if key is None:
            raise InvalidKeyError("Key cannot be None")
        with self.conn.transaction():
            row = self.repository.get(key)
            if row is None:
                raise KeyNotFoundError("Key not found")
            _, value, _, _ = row
            return value

    def delete_value(self, key):
        if key is None:
            raise InvalidKeyError("Key cannot be None")
        with self.conn.transaction():
            row = self.repository.delete(key)
            if row is None:
                raise KeyNotFoundError("Key not found")
            return row

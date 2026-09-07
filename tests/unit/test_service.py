from unittest.mock import MagicMock

import pytest

from kvstore.service import (
    InvalidKeyError,
    InvalidValueError,
    KeyNotFoundError,
    Service,
)


def test_set_value_rejects_none_key():
    repo = MagicMock()
    conn = MagicMock()
    service = Service(repo, conn)
    with pytest.raises(InvalidKeyError):
        service.set_value(None, "test")


def test_set_value_rejects_too_long_key():
    repo = MagicMock()
    conn = MagicMock()
    service = Service(repo, conn)
    with pytest.raises(InvalidKeyError):
        key = "a" * 1000
        service.set_value(key, "value")


def test_set_value_rejects_none_value():
    repo = MagicMock()
    conn = MagicMock()
    service = Service(repo, conn)
    with pytest.raises(InvalidValueError):
        service.set_value("test", None)


def test_set_value_rejects_too_long_value():
    repo = MagicMock()
    conn = MagicMock()
    service = Service(repo, conn)
    with pytest.raises(InvalidValueError):
        value = "a" * 5000
        service.set_value("test", value)


def test_get_value_rejects_none_key():
    repo = MagicMock()
    conn = MagicMock()
    service = Service(repo, conn)
    with pytest.raises(InvalidKeyError):
        service.get_value(None)


def test_get_value_raises_when_key_is_missing():
    repo = MagicMock()
    conn = MagicMock()
    # Mock the repository to simulate a missing key
    repo.get.return_value = None
    service = Service(repo, conn)
    with pytest.raises(KeyNotFoundError):
        service.get_value("test")


def test_get_value_returns_the_good_value():
    repo = MagicMock()
    conn = MagicMock()
    # Mock the repository to simulate an existing key
    repo.get.return_value = ("test", "value", None, None)
    service = Service(repo, conn)
    assert service.get_value("test") == "value"


def test_delete_value_rejects_none_key():
    repo = MagicMock()
    conn = MagicMock()
    service = Service(repo, conn)
    with pytest.raises(InvalidKeyError):
        service.delete_value(None)


def test_delete_value_raises_when_key_is_missing():
    repo = MagicMock()
    conn = MagicMock()
    # Mock the repository to simulate a missing key
    repo.delete.return_value = None
    service = Service(repo, conn)
    with pytest.raises(KeyNotFoundError):
        service.delete_value("test")

import pytest

from exceptions import ApiError, NotFoundError
from safe_divide import safe_divide


def test_hierarchy():
    assert issubclass(ApiError, Exception)
    assert issubclass(NotFoundError, ApiError)


def test_can_raise_and_catch_not_found():
    with pytest.raises(NotFoundError):
        raise NotFoundError("missing")


def test_catch_as_api_error():
    with pytest.raises(ApiError):
        raise NotFoundError("missing")


def test_safe_divide_ok():
    assert safe_divide(10, 2) == 5


def test_safe_divide_zero():
    with pytest.raises(ZeroDivisionError):
        safe_divide(1, 0)

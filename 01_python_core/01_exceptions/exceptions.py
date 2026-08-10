"""Свои исключения для API (блок 1.2)."""


class ApiError(Exception):
    var = None
class NotFoundError(ApiError):
    var = None
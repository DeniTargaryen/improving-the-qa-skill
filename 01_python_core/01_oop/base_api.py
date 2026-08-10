"""Упрощённый BaseApi для тренировки наследования (блок 1.1)."""


class BaseApi:
    def __init__(self, base_url: str):
        self.base_url = base_url

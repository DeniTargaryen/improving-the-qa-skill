"""Блок 1.1 — наследник BaseApi."""

from base_api import BaseApi


class JsonPlaceholderApi(BaseApi):
    def __init__(self):
        super().__init__("https://jsonplaceholder.typicode.com")

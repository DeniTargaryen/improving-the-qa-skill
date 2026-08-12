"""HTTP-клиент блока 3.1. GET уже готов (не трогай) — допиши POST/PUT/PATCH/DELETE
по TASK.md. Самодостаточная копия, независимая от 00_week0_sprint.

Файл называется crud_api.py, а не base_api.py — в репозитории уже есть
несколько модулей с именем base_api (01_python_core/01_oop, другие блоки
недели 3), и без пакетов с __init__.py общий прогон pytest по всему репо
закэшировал бы только первый импортированный base_api и подставил его
во всех остальных местах (тихий баг). Класс внутри всё равно называется
BaseApi — это просто имя файла, не имя класса.
"""
import requests


class BaseApi:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, path: str, expected_status: int = 200) -> dict:
        full_url = self.base_url + path
        r = requests.get(
            url=full_url,
            headers={"User-Agent": "Mozilla/5.0", "content-type": "application/json"},
        )
        assert r.status_code == expected_status, f"Ожидали статус код {expected_status}, пришёл {r.status_code}"
        return r.json()

    def post(self, path: str, json: dict, expected_status: int = 201) -> dict:
        raise NotImplementedError

    def put(self, path: str, json: dict, expected_status: int = 200) -> dict:
        raise NotImplementedError

    def patch(self, path: str, json: dict, expected_status: int = 200) -> dict:
        raise NotImplementedError

    def delete(self, path: str, expected_status: int = 200) -> None:
        raise NotImplementedError

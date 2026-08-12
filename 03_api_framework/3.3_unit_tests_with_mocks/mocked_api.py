"""Готовый референсный клиент для блока 3.3 — не переписывай.
Цель блока — тестирование через моки, а не переизобретение клиента.

Файл называется mocked_api.py, а не base_api.py — в репозитории уже
несколько модулей с именем base_api (1.1, другие блоки недели 3), и без
пакетов с __init__.py общий прогон pytest по всему репо закэшировал бы
только первый импортированный base_api и подставил его везде (тихий баг).
Класс внутри всё равно называется BaseApi.
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

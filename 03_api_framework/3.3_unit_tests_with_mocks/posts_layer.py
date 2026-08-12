"""Готовые эндпоинт-функции для блока 3.3 — не переписывай.
Твоя задача — покрыть их unit-тестами на моках (см. TASK.md).

Файл называется posts_layer.py, а не posts.py — чтобы не конфликтовать с
одноимённым модулем в 00_week0_sprint при общем прогоне pytest по всему
репозиторию (тот использует пакетный импорт src.api.posts, но лучше не
рисковать вторым совпадением флэт-имени).
"""
from mocked_api import BaseApi

posts_client = BaseApi("https://jsonplaceholder.typicode.com")


def get_post(post_id: int) -> dict:
    return posts_client.get(path=f"/posts/{post_id}")


def get_posts() -> list:
    return posts_client.get(path="/posts/")

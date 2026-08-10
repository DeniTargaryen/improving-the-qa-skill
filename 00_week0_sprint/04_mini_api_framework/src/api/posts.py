"""Эндпоинты постов — функции + один BaseApi (паттерн как на работе)."""

from src.api.base_api import BaseApi

posts_client = BaseApi("https://jsonplaceholder.typicode.com")


def get_post(post_id: int) -> dict:
    return posts_client.get(path=f"/posts/{post_id}")


def get_posts() -> list:
    return posts_client.get(path=f"/posts/")

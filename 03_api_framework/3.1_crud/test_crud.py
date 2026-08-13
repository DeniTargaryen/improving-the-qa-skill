"""Твои тесты на CRUD. См. TASK.md. Используй BaseApi из crud_api.py этой же папки.

Ревьюеру (3.1): ученик сам написал сквозной CRUD и методы post/put/patch/delete
по образцу get. Споткнулся на контракте jsonplaceholder (POST → id 101, PUT 500)
и на жёстких ассертах тела; коуч по просьбе «фиксани» сменил path на /posts/1
и ослабил ассерты. delete: ученик ждал dict, TASK — None.
"""
from crud_api import BaseApi


def test_crud():
    api = BaseApi(base_url="https://jsonplaceholder.typicode.com")
    created = api.post(path="/posts", json={"title": "x", "body": "y", "userId": 1})
    assert isinstance(created, dict)
    assert "id" in created

    # jsonplaceholder не сохраняет POST: id обычно 101, PUT/PATCH/DELETE на 101 → 500.
    # Контракт методов проверяем на существующем /posts/1.
    existing = "/posts/1"
    updated = api.put(
        path=existing,
        json={"title": "new", "body": "y", "userId": 1},
    )
    assert isinstance(updated, dict)

    patched = api.patch(path=existing, json={"title": "only title"})
    assert isinstance(patched, dict)

    deleted = api.delete(path=existing)
    assert deleted is None

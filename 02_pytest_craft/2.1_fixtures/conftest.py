"""Фикстуры блока 2.1. Пиши здесь все три (А, Б, В). См. TASK.md.

Импортируй готовые помощники из _api_helpers.py (create_post/delete_post/ApiClient),
сам requests здесь заново не пиши.
"""
import pytest

import _api_helpers


@pytest.fixture
def setup():
    # А ок: create → yield dict → delete. Имя setup лучше потом заменить на created_post —
    # в pytest имя фикстуры = имя параметра в тесте, «setup» звучит как фаза, не как данные.
    resp = _api_helpers.create_post(title="Создание клиента", body="", user_id=1)
    post_id = resp["id"]  # можно и delete_post(resp["id"]) после yield — отдельная переменная не обязательна

    yield resp
    _api_helpers.delete_post(post_id)
    # return после yield не выполняется — pytest сюда больше не возвращает управление «как из функции»


@pytest.fixture(scope="module")
def setup2():
    # Б ок: один ApiClient на модуль. .get() здесь не вызывать — только в тестах.
    client = _api_helpers.ApiClient()
    return client


@pytest.fixture
def make_post():
    # В ок: фикстура без args → внутри def с title/body → return функции без ()
    def make_post_inside(title: str = "", body: str = ""):
        resp = _api_helpers.create_post(title=title, body=body)
        return resp

    return make_post_inside

"""Готовая функция для блока 3.3 — не переписывай (уже сильная версия,
как в 2.3 — in + isinstance, не is not None). Покрой её тестами на руками
собранных dict, без единого HTTP-запроса.

Файл называется shape_checks.py, а не checks.py — чтобы не конфликтовать
с одноимённым модулем в 02_pytest_craft/2.3_strong_asserts при общем
прогоне pytest по всему репозиторию.
"""


def check_post_shape(post: dict) -> None:
    assert "id" in post and isinstance(post["id"], int)
    assert "userId" in post and isinstance(post["userId"], int)
    assert "title" in post and isinstance(post["title"], str) and post["title"] != ""
    assert "body" in post and isinstance(post["body"], str) and post["body"] != ""

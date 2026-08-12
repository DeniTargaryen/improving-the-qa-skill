"""Блок 2.3. Реализуй check_post_shape по TASK.md.

Самодостаточно: dict здесь собирается руками в тестах, реального похода в
сеть в этом блоке нет вообще — не нужно тянуть week0 или requests.

Файл называется post_shape.py, а не checks.py, чтобы не конфликтовать с
одноимённым модулем в 03_api_framework/3.3_unit_tests_with_mocks при общем
прогоне pytest по всему репозиторию (оба модуля были бы "checks" без пакетов
с __init__.py — Python закэшировал бы только первый импортированный и отдавал
его во всех остальных местах).
"""

keys = ["id", "userId", "title", "body"]

def check_post_shape(post: dict) -> None:
    for key in keys:
        assert key in post, f"Ключа {key} нет в словаре"
        if key in ["id", "userId"]:
            assert isinstance(post[key], int), f"Ключ {key} должен отдавать тип int, факт = {type(post[key])}"
        else:
            assert isinstance(post[key], str), f"Ключ {key} должен отдавать тип str, факт = {type(post[key])}"
            assert post[key] != ''
    return None

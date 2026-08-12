"""Упражнение Б — твои тесты. См. TASK.md, часть Б.

Пишешь parametrize с ids= (валидные посты) и негативный parametrize
(невалидные посты -> ожидаем AssertionError). Используй check_post_shape
из checks.py (та же функция, что и в части А).
"""
import pytest

from post_shape import check_post_shape

#user_data = {"id": 1, "userId": 1, "title": "Заголовок", "body": "Тело"}
@pytest.mark.parametrize(
    "user_data",
    [
        {"id": 1, "userId": 1, "title": "Заголовок", "body": "Тело"},
        {"id": 99, "userId": 99, "title": "Заголовок", "body": "Тело"},
        {"id": 2, "userId": 2, "title": "Заголовок", "body": "Телоооооооооооооооооооо"}
    ]
,
ids = ["minimal", "maximum", "long body"])
def test_check_user_data(user_data: dict):
    check_post_shape(user_data)


@pytest.mark.parametrize(
    "user_data",
    [
        {"id": "1", "userId": 1, "title": "Заголовок", "body": "Тело"},
        {"id": 1, "userId": "1", "title": "Заголовок", "body": "Тело"},
        {"id": 1, "userId": 1, "title": 1, "body": "Тело"},
        {"id": 1, "userId": 1, "title": "Заголовок", "body": 1}
    ],
ids = [
    "not_valid_id",
    "not_valid_userId",
    "not_valid_Заголовок",
    "not_valid_body"
]
)
def test_negative_check_user_data(user_data: dict):
    with pytest.raises(AssertionError):
        check_post_shape(user_data)
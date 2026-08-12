"""Track A: тесты уже готовы, не трогай. Пиши только checks.py. См. TASK.md, часть А."""
import pytest

from post_shape import check_post_shape


def test_valid_post_passes_silently():
    post = {"id": 1, "userId": 10, "title": "Заголовок", "body": "Текст"}
    assert check_post_shape(post) is None


def test_missing_title_key_raises():
    post = {"id": 1, "userId": 10, "body": "Текст"}
    with pytest.raises(AssertionError):
        check_post_shape(post)


def test_empty_string_title_is_caught():
    """Ключевой момент блока: раньше `is not None` пропускал бы это —
    пустая строка не None, но по смыслу это всё равно битые данные."""
    post = {"id": 1, "userId": 10, "title": "", "body": "Текст"}
    with pytest.raises(AssertionError):
        check_post_shape(post)


def test_wrong_type_title_raises():
    post = {"id": 1, "userId": 10, "title": 12345, "body": "Текст"}
    with pytest.raises(AssertionError):
        check_post_shape(post)


def test_wrong_type_id_raises():
    post = {"id": "1", "userId": 10, "title": "Заголовок", "body": "Текст"}
    with pytest.raises(AssertionError):
        check_post_shape(post)


def test_zero_user_id_is_valid():
    """userId == 0 — это валидное число (например, системный пользователь),
    не «пустое» значение. Хорошая проверка не должна путать 0 с отсутствием данных."""
    post = {"id": 1, "userId": 0, "title": "Заголовок", "body": "Текст"}
    assert check_post_shape(post) is None

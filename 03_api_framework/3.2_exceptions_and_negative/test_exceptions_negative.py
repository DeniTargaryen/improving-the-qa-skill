"""Твои тесты. См. TASK.md.

Ревьюеру (3.2): ученик сам написал ApiError/NotFoundError, raise в get, живой 404.
Кейс 500: ~30 мин на unittest.mock.patch (не зря — jsonplaceholder не отдаёт 500;
живой /post это 404, NotFoundError ⊂ ApiError → ложный зелёный без мока).
Коуч сначала путал жаргоном и кидал patch без импорта/построчного разбора;
итог ученика: patch("negative_api.requests.get") + return_value.status_code=500.
Внутри patch повторно создаёт BaseApi — лишнее, на смысл не влияет.
"""
import pytest
from unittest.mock import patch
from negative_api import BaseApi
from api_errors import ApiError, NotFoundError


def test_negative_api():
    api = BaseApi(base_url="https://jsonplaceholder.typicode.com")


    with pytest.raises(NotFoundError):
        api.get("/posts/9999999")
    with patch("negative_api.requests.get") as mock_get:
        mock_get.return_value.status_code = 500
        with pytest.raises(ApiError):
            api = BaseApi(base_url="https://jsonplaceholder.typicode.com")
            api.get("/post")

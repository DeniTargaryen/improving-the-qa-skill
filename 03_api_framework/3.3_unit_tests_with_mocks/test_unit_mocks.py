"""Твои тесты. См. TASK.md. mocked_api.py/posts_layer.py/shape_checks.py уже
готовы — твоя работа — тесты, которые покрывают их без реальной сети.

Ревьюеру (3.3): ученик сам дошёл до patch("posts_layer.posts_client.get"),
отдельный return_value dict для get_post и list для get_posts, равенство == k.
Трудности: сначала мокал requests.get / сами get_post (ложный зелёный в сеть);
путал этаж «ответ HTTP» (status_code) и этаж «клиент уже вернул dict».
Строка status_code перед return_value = k ничего не делает (объект выкидывается).
Можно лучше: assert_called с path=/posts/2 и /posts/ (TASK просил; на однострочнике
почти не ломается); pytest.raises(AssertionError) вместо голого Exception;
убрать мёртвый status_code и закомментированный BaseApi.
"""
import pytest

#from mocked_api import BaseApi
from posts_layer import get_post, get_posts
from shape_checks import check_post_shape
from unittest.mock import patch

def test_unit_tests_with_mocks():
    #api = BaseApi("https://jsonplaceholder.typicode.com")

    k = {"id": 1,"userId": 1,"title": "1","body": "1"}
    not_valid_k = {"id": "2","userId": "2","title": 2,"body": 2}
    check_post_shape(post=k)

    with pytest.raises(Exception):
        check_post_shape(post=not_valid_k)

    with patch("posts_layer.posts_client.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value = k
        result_post  = get_post(post_id=2)
        mock_get.return_value = [k]
        result_posts = get_posts()
        assert isinstance(result_posts, list)
        assert isinstance(result_post, dict)
        assert result_posts == [k]
        assert result_post == k


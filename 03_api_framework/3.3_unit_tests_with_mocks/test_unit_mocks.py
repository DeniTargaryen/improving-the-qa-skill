"""Твои тесты. См. TASK.md. mocked_api.py/posts_layer.py/shape_checks.py уже
готовы — твоя работа — тесты, которые покрывают их без реальной сети.

Ревьюеру (3.3): ученик сам дошёл до patch("posts_layer.posts_client.get"),
отдельный return_value dict для get_post и list для get_posts, равенство == k.
Попыток «проверь» с красным: 2. (1) мокал mocked_api.requests.get + .json на функции,
не на return_value, звал api.get а не get_post. (2) патчил сами get_post/get_posts
(ложный зелёный ~1.3s в сеть; импорт from posts_layer уже обошёл патч).
+1 промежуточное ревью без слова «проверь»: уже posts_client.get, но один dict k
на get_posts (isinstance list красный) + мёртвый status_code.
Путаницы: requests.get vs get_post vs posts_client.get; HTTP-ответ (status_code)
vs клиент уже вернул dict; патч функции под тестом vs зависимости под ней.
Можно лучше: assert_called path=/posts/2 и /posts/; raises(AssertionError);
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


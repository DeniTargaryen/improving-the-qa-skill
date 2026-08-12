"""Твои тесты. См. TASK.md. mocked_api.py/posts_layer.py/shape_checks.py уже
готовы — твоя работа — тесты, которые покрывают их без реальной сети."""
from unittest.mock import patch

from posts_layer import get_post, get_posts
from shape_checks import check_post_shape

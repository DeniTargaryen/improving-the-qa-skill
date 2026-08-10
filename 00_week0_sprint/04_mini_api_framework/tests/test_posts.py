"""Тесты: вызывай get_post / get_posts + checks. См. TASK.md."""

import pytest

from src.api.posts import get_post, get_posts
from src.checks.posts_checks import check_post_shape, check_post_id


@pytest.mark.smoke
def test_get_post_one():

    req_get = get_post(post_id=1)
    check_post_id(expected_id=1, post=req_get)
    check_post_shape(post=req_get)

@pytest.mark.parametrize(
    "expected_id",
    [1, 2, 3])
@pytest.mark.smoke
def test_get_post_param(expected_id: int) -> None:

    req_get = get_post(post_id=expected_id)
    check_post_id(expected_id=expected_id, post=req_get)
    check_post_shape(post=req_get)
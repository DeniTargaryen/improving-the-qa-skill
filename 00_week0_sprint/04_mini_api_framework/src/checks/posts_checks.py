"""Проверки ответа поста. Реализуй по TASK.md."""


def check_post_shape(post: dict) -> None:
    assert post["title"] is not None
    assert post["body"] is not None
    assert post["userId"] is not None
    assert post["id"] is not None

def check_post_id(post: dict, expected_id: int) -> None:
    assert post["id"] == expected_id
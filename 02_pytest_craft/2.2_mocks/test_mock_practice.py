from unittest.mock import Mock

import pytest


@pytest.mark.smoke
def test_get_post_one():
    client = Mock()

    client.get.return_value = {"one": 1}
    req_get = client.get(post_id=1)
    assert req_get == {"one": 1}

"""Track A: тест уже готов, не трогай. Пиши только fetcher.py. См. TASK.md, часть А."""
from unittest.mock import Mock

from fetcher import fetch_data


def test_fetch_data_calls_client_and_returns_result():
    client = Mock()
    client.get.return_value = {"id": 1, "title": "mocked"}

    result = fetch_data(client, "/posts/1")

    client.get.assert_called_once_with("/posts/1")
    assert result == {"id": 1, "title": "mocked"}


def test_fetch_data_returns_whatever_client_returns():
    client = Mock()
    client.get.return_value = "любая другая строка, не только dict"

    assert fetch_data(client, "/anything") == "любая другая строка, не только dict"


def test_fetch_data_does_not_call_real_network(monkeypatch):
    """Доказательство идеи мока: если бы fetch_data сама лезла в requests,
    этот тест бы не запретил ей это явно — но раз она принимает client
    аргументом и вызывает только его, реальной сети здесь вообще нет
    ни одной строчки кода requests/urllib."""
    client = Mock()
    client.get.return_value = {"ok": True}

    fetch_data(client, "/no-network-here")

    assert client.get.called

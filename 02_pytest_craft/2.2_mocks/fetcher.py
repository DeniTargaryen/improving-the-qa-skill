"""Блок 2.2-А. Реализуй fetch_data по TASK.md.

Тест уже готов в test_fetcher_mock.py — не трогай его, это Track A.
"""


def fetch_data(client, path):
    #resp = client.get(path)
    #return resp
    return client.get(path)
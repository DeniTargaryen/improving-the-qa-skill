"""Демо 2.2: patch под хелпером (коуч написал целиком).

Устный разбор — кто кого:
1) Тест вызывает get_order(7) — как ты на работе зовёшь хелпер, НЕ BaseApi.
2) get_order внутри делает _client.get(path="/orders/7").
3) patch подменяет demo_helpers.HttpClient.get на время теста.
4) Реальный HTTP не вызывается. Проверяем: хелпер вернул то, что «отдала» подставка,
   и что get вызвали с нужным path.

Почему patch на demo_helpers.HttpClient.get, а не «где-то в другом модуле»:
патчат там, ГДЕ имя используется при вызове (этот модуль держит _client).
"""
from unittest.mock import patch

from demo_helpers import get_order


def test_get_order_without_real_http():
    fake_body = {"id": 7, "status": "ok"}

    # Подмена метода get у класса HttpClient в ЭТОМ же пакете демо.
    with patch("demo_helpers.HttpClient.get") as mock_get:
        mock_get.return_value = fake_body  # «сеть» отвечает вот этим dict

        result = get_order(7)  # твой обычный вызов хелпера

        assert result == fake_body
        mock_get.assert_called_once_with(path="/orders/7")


# --- твой черновик test_mock_practice.py оставляем как есть (история) ---
# Он тестировал Mock сам на себя — это как раз «мок ради мока», без хелпера.

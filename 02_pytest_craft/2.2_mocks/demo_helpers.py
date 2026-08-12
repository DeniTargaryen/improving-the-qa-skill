"""Самодостаточный мини-слой для демо 2.2 (коуч). Без импортов из week0.

Цепочка как у тебя на работе по смыслу:
  тест → get_order (хелпер/эндпоинт-функция) → HttpClient.get → (в проде был бы requests)

В тесте с patch подменяем HttpClient.get, хелпер не переписываем.
"""


class HttpClient:
    """Условный API-клиент. В проде внутри был бы requests.get."""

    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, path: str) -> dict:
        # В учебном демо реальную сеть не зовём — если дошли сюда без мока, тест сломан.
        raise RuntimeError(
            f"Реальный HTTP запрещён в демо. Вызвали get({self.base_url}{path})"
        )


# Один клиент на модуль — как posts_client в week0
_client = HttpClient("https://example.test")


def get_order(order_id: int) -> dict:
    """Хелпер, который ты вызываешь из теста. Path собирается ЗДЕСЬ."""
    return _client.get(path=f"/orders/{order_id}")

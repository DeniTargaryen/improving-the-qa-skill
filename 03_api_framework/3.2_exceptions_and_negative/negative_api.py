"""HTTP-клиент блока 3.2. Рефактори get() по TASK.md — вместо assert кидать
свои исключения из api_errors.py. Самодостаточная копия, не week0.

Импорт классов ошибок (from api_errors import ApiError, NotFoundError)
добавь сам сюда, когда напишешь их в api_errors.py и начнёшь рефакторинг —
специально не добавлен заранее, чтобы этот файл не падал импортом до того,
как классы появятся.

Файл называется negative_api.py, а не base_api.py — в репозитории уже
несколько модулей с именем base_api (1.1, другие блоки недели 3), и без
пакетов с __init__.py общий прогон pytest по всему репо закэшировал бы
только первый импортированный base_api и подставил его везде (тихий баг).
Класс внутри всё равно называется BaseApi.
"""
import requests


class BaseApi:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, path: str) -> dict:
        full_url = self.base_url + path
        r = requests.get(
            url=full_url,
            headers={"User-Agent": "Mozilla/5.0", "content-type": "application/json"},
        )
        # Сейчас: голый assert, как в week0. Замени по TASK.md на raise NotFoundError/ApiError.
        assert r.status_code == 200, f"Ожидали статус код 200, пришёл {r.status_code}"
        return r.json()

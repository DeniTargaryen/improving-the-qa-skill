"""Уже готово — не переписывай.

Блок 2.1 учит фикстуры, а не HTTP-запросы (это уже было в Week 0).
Здесь — тонкие обёртки над jsonplaceholder, чтобы в TASK.md и в твоих
фикстурах не было раздражающего дублирования requests.post(...)/requests.get(...).

jsonplaceholder — фейковый API: ничего не сохраняет по-настоящему на сервере,
но честно проверяет форму запроса и всегда отвечает правдоподобным JSON.
Для тренировки паттерна "создали -> тест -> удалили" этого достаточно.
"""
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def create_post(title: str, body: str, user_id: int = 1) -> dict:
    """POST /posts.

    Возвращает: dict тела ответа (jsonplaceholder всегда добавляет "id",
    обычно 101, т.к. ничего реально не сохраняет).
    """
    r = requests.post(
        f"{BASE_URL}/posts",
        json={"title": title, "body": body, "userId": user_id},
    )
    assert r.status_code == 201, f"Ожидали 201, пришёл {r.status_code}"
    return r.json()


def delete_post(post_id: int) -> None:
    """DELETE /posts/{post_id}. Ничего не возвращает, только проверяет статус."""
    r = requests.delete(f"{BASE_URL}/posts/{post_id}")
    assert r.status_code == 200, f"Ожидали 200, пришёл {r.status_code}"


class ApiClient:
    """Простой клиент-пример для упражнения Б (scope="module").

    Специально свой, не `BaseApi` из 00_week0_sprint/01_oop — блок 2.1
    не должен зависеть от прошлых папок (независимое упражнение).

    `calls` — счётчик обращений. Если фикстура настоящая module-scope,
    один и тот же объект `ApiClient` увидят все тесты модуля, и `calls`
    будет расти между тестами (а не сбрасываться в 0 каждый раз).
    """

    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url
        self.calls = 0

    def get(self, path: str) -> dict:
        self.calls += 1
        r = requests.get(f"{self.base_url}{path}")
        assert r.status_code == 200, f"Ожидали 200, пришёл {r.status_code}"
        return r.json()

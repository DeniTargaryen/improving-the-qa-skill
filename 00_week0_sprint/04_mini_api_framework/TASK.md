# Блок 0.4 — Mini API (как на прошлой работе)

**Статус:** ▶️ упрощён после ревью  
**Паттерн:** один `BaseApi` + тонкие **функции**-эндпоинты (не класс PostsApi) + checks + fixture + тесты  
**API:** https://jsonplaceholder.typicode.com

На лайвкодинге «напиши PostsApi-класс» — **редко**. Чаще: pytest + вызов API/клиента + checks.  
Класс здесь один — `BaseApi` (как у тебя был).

---

## 1. `BaseApi` (`src/api/base_api.py`)

**`__init__(self, base_url: str)`**  
**Что возвращает:** ничего. Сохраняет `base_url` на объекте (`self.base_url = ...`).

**`get(self, path: str, expected_status: int = 200) -> dict`**

| | |
|--|--|
| **Вход** | `path` например `"/posts/1"`; ожидаемый статус |
| **Что возвращает** | `dict` — JSON тела |
| **Если статус не тот** | падает с `AssertionError` |
| **Как** | полный URL = base + path → `requests.get` → проверить код → `.json()` |

---

## 2. Функции постов (`src/api/posts.py`) — не класс

Сделай **модульный** клиент и функции (как `landing_start` на работе):

Идея:
- в модуле создать объект: `posts_client = BaseApi("https://jsonplaceholder.typicode.com")`
- функции вызывают `posts_client.get(...)`

**`get_post(post_id: int) -> dict`**

| | |
|--|--|
| **Что возвращает** | `dict` одного поста |
| Path | `"/posts/{post_id}"` |

**`get_posts() -> list`**

| | |
|--|--|
| **Что возвращает** | `list` словарей (все посты) |
| Path | `"/posts"` |

Имена `get_post` / `get_posts` — про **ресурсы** «пост», это не HTTP POST.

---

## 3. Checks (`src/checks/posts_checks.py`)

**`check_post_shape(post: dict) -> None`**  
**Что возвращает:** ничего. Assert ключи: `userId`, `id`, `title`, `body`.

**`check_post_id(post: dict, expected_id: int) -> None`**  
**Что возвращает:** ничего. Assert `post["id"] == expected_id`.

---

## 4. Fixture (`conftest.py`)

Можно просто использовать функции из `posts.py` без fixture.  
Опционально: fixture, которая ничего сложного не делает, или маркер что клиент доступен — не обязателен класс.

Минимум для сдачи: тесты зовут `get_post` / `get_posts` напрямую.

---

## 5. Тесты (`tests/test_posts.py`)

1. `get_post(1)` → check shape + check id == 1  
2. Parametrize id `1, 2, 3`  
3. Один `@pytest.mark.smoke`

---

## Запуск

```bash
python -m pytest 00_week0_sprint/04_mini_api_framework -v
```

Нужен интернет.

## Сдача

Слои: BaseApi → функции → checks → тесты (без `requests` в тесте).  
**«готово, блок 0.4»**

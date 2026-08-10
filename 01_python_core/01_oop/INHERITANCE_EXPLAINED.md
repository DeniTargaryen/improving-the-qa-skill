# Наследование на примере JsonPlaceholderApi

Разбор **только этого задания**, не абстрактный OOP-учебник.

---

## Какие файлы участвуют

### `base_api.py` (уже дан, не ломай)

```python
class BaseApi:
    def __init__(self, base_url: str):
        self.base_url = base_url
```

Это «общий HTTP-клиент»: при создании ему **обязательно** говорят URL.

Пример, если бы вызывали родителя напрямую:

```text
client = BaseApi("https://jsonplaceholder.typicode.com")
# внутри сработало __init__, стало client.base_url = "https://..."
```

### `jsonplaceholder_api.py` (твоё задание)

Нужен класс, заточенный под один сайт. Тест делает так:

```text
api = JsonPlaceholderApi()
assert api.base_url == "https://jsonplaceholder.typicode.com"
```

Заметь: **в скобках пусто**. Значит, URL нельзя требовать снаружи.

---

## Строка 1: `class JsonPlaceholderApi(BaseApi):`

Читай как: «JsonPlaceholderApi **расширяет** BaseApi».

- Новый класс — **ребёнок**
- `BaseApi` — **родитель**

Ребёнок получает то, что умеет родитель. Здесь родитель умеет одно важное: в `__init__` записать `base_url`.

На работе та же идея: общий `BaseApi`, а под сервис можно сделать узкий класс/модуль с уже известным host.

---

## Строка 2–3: `def __init__(self):`

### Почему `__init__`?

`JsonPlaceholderApi()` = «создай объект».  
При создании Python вызывает `__init__`.  
Мы хотим в этот момент сразу проставить URL → пишем `__init__`.

### Почему нет второго аргумента `base_url`?

Потому что тест и смысл задания такие:

```text
JsonPlaceholderApi()   # не JsonPlaceholderApi("https://...")
```

URL зашит внутри класса. Снаружи его не передают.

`self` всё равно нужен — это создаваемый объект (как в Account).

---

## Строка: `super().__init__("https://jsonplaceholder.typicode.com")`

Разбей на куски:

| Кусок | Смысл |
|-------|--------|
| `super()` | «обратись к родителю (BaseApi), не копируй его код» |
| `.__init__(...)` | «выполни конструктор родителя» |
| `"https://jsonplaceholder.typicode.com"` | это и есть аргумент `base_url`, который ждёт `BaseApi.__init__` |

То есть ты **не** пишешь заново `self.base_url = ...` (хотя технически можно было бы).  
Ты просишь родителя сделать ту работу, которую он уже умеет.

Эквивалент по результату:

```text
создали JsonPlaceholderApi
  → внутри позвали BaseApi.__init__(этот_объект, "https://jsonplaceholder.typicode.com")
  → у объекта появилось поле base_url
```

---

## Что будет, если забыть `super().__init__(...)`?

Объект `JsonPlaceholderApi()` создастся, но **`base_url` не появится**  
(родительский конструктор не вызвали) → тест упадёт: нет атрибута / не тот URL.

---

## Что будет, если написать `def __init__(self, base_url):` как у родителя?

Тогда снаружи снова пришлось бы передавать URL:

```text
JsonPlaceholderApi("https://...")
```

А тест вызывает **без** аргументов. Значит, сигнатура — только `self`.

---

## Связь с тем, что ты уже понял на Account

| Account | JsonPlaceholderApi |
|---------|-------------------|
| `Account("Ann", 100)` — данные снаружи | `JsonPlaceholderApi()` — данных снаружи нет |
| `__init__` сохраняет owner/balance | `__init__` просит родителя сохранить base_url |
| поля живут на `self` | `base_url` тоже живёт на `self` (его записал родитель) |

---

## Копипаста без понимания

Строка с `super()` — не магия из чата. Это **вызов конструктора BaseApi** с фиксированным URL.  
После неё объект такой же по полям, как `BaseApi("https://jsonplaceholder.typicode.com")`, только тип класса — `JsonPlaceholderApi`.

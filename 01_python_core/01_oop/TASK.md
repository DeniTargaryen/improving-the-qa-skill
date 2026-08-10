# Блок 1.1 — OOP минимум для AQA

**Статус:** ▶️ открыт  
**Формат Track A:** тесты готовы → пишешь классы  
**Доки-разжёвки:** `OOP_EXPLAINED.md`, `RECTANGLE_HINT.md`, `MONEY_HINT.md`, `INHERITANCE_EXPLAINED.md`

---

## 1. `Account` (`account.py`) — уже сдавали

Объект «счёт»: поля `owner`, `balance`; методы `deposit` / `withdraw`.

---

## 2. `Rectangle` (`rectangle.py`) — уже сдавали

Объект с `width`/`height`; `area` возвращает произведение;  
`from_square` — фабрика квадрата; `is_valid` — проверка без объекта.

---

## 3. `Money` (`money.py`) — уже сдавали

Сравнение: при `Money(100, "RUB") == Money(100, "RUB")` слева `self`, справа `other`.  
`isinstance(other, Money)` + сравнение полей. `__repr__` → строка с суммой и валютой.

---

## 4. `JsonPlaceholderApi` (`jsonplaceholder_api.py`) — разжёвано

Читай обязательно: **`INHERITANCE_EXPLAINED.md`**.

### Зачем это задание

У тебя уже есть класс-родитель в `base_api.py`:

```python
class BaseApi:
    def __init__(self, base_url: str):
        self.base_url = base_url
```

Чтобы создать обычный клиент, нужно писать каждый раз:

```text
BaseApi("https://jsonplaceholder.typicode.com")
```

Задание: сделать **специальный** класс `JsonPlaceholderApi`, у которого этот URL уже «зашит».  
Создание в тесте выглядит так (смотри `test_oop.py`):

```text
api = JsonPlaceholderApi()
```

**Без** передачи URL снаружи. После этого у объекта должно быть:

```text
api.base_url == "https://jsonplaceholder.typicode.com"
```

### Что такое «наследует» одной фразой

```python
class JsonPlaceholderApi(BaseApi):
```

Значит: `JsonPlaceholderApi` — это **тот же BaseApi плюс настройки под jsonplaceholder**.  
Объект нового класса умеет всё, что умеет родитель (здесь — хранить `base_url`), и может добавить своё.

### Почему снова `__init__`?

Потому что при `JsonPlaceholderApi()` Python ищет, **как создать** объект.  
Мы хотим при создании сразу прописать нужный URL. Это работа конструктора → пишем свой `__init__`.

### Почему в скобках только `self`, без `base_url`?

Потому что **снаружи** URL передавать не нужно — тест вызывает `JsonPlaceholderApi()` пустыми скобками.  
URL известен заранее и задаётся **внутри** `__init__`.

Сравни:

| Создание | Кто передаёт URL |
|----------|------------------|
| `BaseApi("https://...")` | ты снаружи |
| `JsonPlaceholderApi()` | класс сам внутри |

### Что такое `super()`?

`super()` — способ сказать: «вызови код **родителя** (`BaseApi`), не копируй его руками».

Родитель умеет: принять URL и сделать `self.base_url = ...`.  
Нам нужно именно это — только с фиксированным адресом:

```text
super().__init__("https://jsonplaceholder.typicode.com")
```

Смысл по шагам:
1. `super()` — взять родителя относительно нашего класса  
2. `.__init__(...)` — вызвать его конструктор  
3. В скобках — тот URL, который родитель ждёт как `base_url`

После этого у объекта появляется `base_url`, как если бы сделали `BaseApi("https://jsonplaceholder.typicode.com")`.

### Что возвращает `__init__`

Ничего (как всегда у конструктора). «Результат» — готовый объект `api` в переменной слева: `api = JsonPlaceholderApi()`.

### Критерий сдачи этого пункта

```bash
python -m pytest 01_python_core/01_oop/test_oop.py::TestJsonPlaceholderApi -v
```

Ожидание: объект создаётся без аргументов, `base_url` равен `https://jsonplaceholder.typicode.com`.

---

## Запуск всего 1.1

```bash
python -m pytest 01_python_core/01_oop -v
```

Сдача блока: **«готово, блок 1.1»**.

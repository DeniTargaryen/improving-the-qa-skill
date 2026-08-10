# Устный мок-собес с Gemini — отчёт

**Дата сессии:** ~2026-08-06  
**Статус:** сохранить для глубокого разбора.  
**Sonnet 5:** смотреть **только по явному запросу** ученика (пул вопросов / зоны роста / правки плана).  
**Коуч:** может опираться на этот отчёт в обычном фидбеке без отдельного «запуска Sonnet».

---

## 1. Вопросы и эталонные ответы (от Gemini)

### Вопрос 1: Архитектура E2E API-фреймворка
**Вопрос:** Расскажи о своем последнем проекте и как концептуально была устроена архитектура вашего E2E API-фреймворка?

**Эталон (Gemini):** Layered Architecture — Client/BaseApi; Services/Endpoints; Models (Pydantic); Helpers/Checks; Fixtures/Tests; CI/CD & Reporting (xdist, Allure, Telegram).

### Вопрос 2: Валидация и Pydantic
**Вопрос:** Как проверяете корректность данных и структур ответов? Pydantic?

**Эталон:** `Model.model_validate(response.json())` — поля, типы, кастомные правила; иначе ValidationError.

### Вопрос 3: Mountebank + Redis / параллель
**Вопрос:** Как Mountebank и изоляция при xdist?

**Эталон:** стабы по заголовку; race condition при параллели; Redis + уникальный application_id/user_id в контексте.

### Вопрос 4: Fixtures + Faker
**Эталон:** yield setup/teardown; Faker для уникальных данных вместо hardcode.

### Вопрос 5: Session и Retries в BaseApi
**Эталон:** `requests.Session()`; `HTTPAdapter` + `urllib3.util.Retry` на 5xx.

### Вопрос 6: CI/CD + Allure
**Эталон:** lint → pytest в Docker → allure-results artifacts → Telegram.

### Вопрос 7: `__str__` / `__repr__`
**Эталон:** `__repr__` для дебага/логов; `__str__` для «человеческого» вида; в AQA важно для читаемых падений.

### Вопрос 8: Сетевые ошибки requests
**Эталон:** ловить RequestException/Timeout; логировать контекст; своё исключение или понятный fail.

### Вопрос 9: Parametrize
**Эталон:** один сценарий — много наборов данных (границы, invalid, reject reasons).

### Вопрос 10: Fixture scope
**Эталон:** function / class / module / session; session для тяжёлого (токен, клиент, Docker).

### Вопрос 11: Generators vs list comprehensions
**Эталон:** list — сразу в памяти O(n); generator — лениво O(1) по памяти.

---

## 2. Фидбек Gemini (кратко)

**Сильно:** мокер+Redis+xdist, слои, CI/Allure, Faker, аргументация.

**Зоны роста:** магические методы (`__repr__`/`__str__`); генераторы; Retry/HTTPAdapter; exception hierarchy requests; увереннее fixture scopes.

**Рекомендации:** mutability, OOP, генераторы; лайвкодинг BaseApi/парсер без ИИ.

---

## 3. Связь с нашим планом

Блок **1.1 OOP** (Account, Money/`__repr__`, наследование) — прямое закрытие зоны роста из этого отчёта.  
Дальше по плану Sonnet: исключения → декораторы → моки → CRUD/Retry.

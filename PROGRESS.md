# Прогресс

Легенда: 🔒 закрыто · ▶️ в работе · ✅ сдано · ⚠️ есть претензия ученика · 🔓 TASK готов, ждёт своей очереди по гейту

## Приоритеты трека (15.08.2026 вечер, полный пакет Sonnet 5 — заменяет неполный дневной пакет 15.08)

1. **Главное:** план `docs/superpowers/plans/2026-08-15-post-32-two-plus-weeks-plan.md` (пролонгация плана 12.08 — тот план не отменяется, недели 1–2 и 3.1/3.2 по нему сданы).
2. **Правка задним числом (важно):** дневной пакет 15.08 ошибочно писал «3.3 скип» / отмечал 3.3 как сделанное — **обе записи неверны**. 3.3 **активен, не сдан** (`test_unit_mocks.py` пустой), и статус вернулся на **обязательный** после рыночной проверки — реальные вакансии AQA Python 2026 (ИнфоТеКС, СберОС) прямо требуют «pytest (мок-объекты/mock)». Разбор: `docs/sonnet_reviews/2026-08-15-market-vs-student-feedback.md`.
3. **Активный блок: 3.4** — `03_api_framework/3.4_pydantic_schedule_check/TASK.md`. Дальше 3.5.
4. **Gemini-отчёт** — только устное; не подменяет план Sonnet.
5. Роли: Sonnet = план/темы/задания/ревью; коуч = ведёт по TASK + `CALENDAR.md` + `docs/sonnet_reviews/COACH_RECS_2026-08-15.md`.
6. Рыночное обоснование каждого блока — `docs/sonnet_reviews/2026-08-12-task-self-review-vs-real-interviews.md` (базовое) + `docs/sonnet_reviews/2026-08-15-market-vs-student-feedback.md` (правка по мокам).

## Роли

См. `COACHING.md`

## Week 0

| Блок    | Статус                      |
| ------- | --------------------------- |
| 0.1–0.4 | ✅                           |
| 0.5     | ✅ коуч-фидбек; Sonnet позже |

## Неделя 1 — python_core (план Sonnet)

| Блок                 | Статус                                                                                     |
| -------------------- | ------------------------------------------------------------------------------------------ |
| 1.1 OOP              | ✅ тесты; ⚠️ фидбек в `STUDENT_FEEDBACK_for_sonnet.md`                                      |
| 1.2 Исключения       | ✅; ⚠️ качество TASK — в фидбеке                                                            |
| 1.3 Декораторы       | ✅ тесты; ⚠️ **~2ч, очень тяжело**; худшее задание трека; новый вход на ту же тему — блок 3.5 |
| 1.4 Тривиа-drill     | ✅ код 7/7 + ANSWERS (теория слабовата — на ревью Sonnet) → `01_python_core/04_python_trivia/` |

**Гейт недели 1:** 1.1–1.4 сданы ✅.

## Неделя 2 — `02_pytest_craft`

| Блок | Тема | Статус |
|------|------|--------|
| 2.1  | Фикстуры (yield/teardown, scope=module, фабрика) | ✅ сдано 11.08 — `02_pytest_craft/2.1_fixtures/` |
| 2.2  | Моки (`unittest.mock`, mock вместо реальной сети) | ✅ 12.08: А сделана; Б/В **скип осознанно, подтверждено рыночным ревью 12.08** (это решение не пересматривается — только статус 3.3 ниже) |
| 2.3  | Сильные ассерты + parametrize | ✅ сдано 12.08 — `02_pytest_craft/2.3_strong_asserts/` |
| 2.4  | Маркеры/конфиг pytest | ✅ сдано 12.08 — маркер `regression` в `pytest.ini` + ANSWERS |

## Неделя 3 — `03_api_framework` (пакет 15.08 — 3.3 обязателен, добавлены 3.4/3.5)

| Блок | Тема | Статус |
|------|------|--------|
| **3.1**  | CRUD в `BaseApi` | ✅ сдано 13.08 |
| **3.2**  | Свои исключения + негативный тест | ✅ сдано 13.08 — `patch` на 500 нужен, не «мок ради мока» |
| **3.3**  | Unit-тесты слоёв на моках | ✅ сдано 15.08 — патч на `posts_client.get`, dict/list, `==`; path-assert нет (заметка в тесте) |
| **3.4**  | Pydantic-модель (`Entry`/`Schedule`) + `check_values` | ▶️ **активный** — `03_api_framework/3.4_pydantic_schedule_check/TASK.md` |
| **3.5**  | Тестирование retry-хелпера через мок | 🔓 **новый**, TASK готов — `03_api_framework/3.5_retry_helper_with_mock/TASK.md` |

## Неделя 4 — `04_interview_theory` (буфер, ОПЦИОНАЛЬНО)

| Блок | Тема | Статус |
|------|------|--------|
| 4.1  | Allure минимум | 🔓 TASK готов, опционален — `04_interview_theory/4.1_allure_minimum/TASK.md` |
| 4.2  | Live-coding под таймер | 🔓 TASK готов, опционален — `04_interview_theory/4.2_timer_drill/TASK.md` |
| 4.3  | Voice round 2 (+ Kafka/gRPC формулировки) | 🔓 TASK готов, опционален — `04_interview_theory/4.3_voice_round2/TASK.md` |

**Гейт недели 2:** 2.3–2.4 сданы → неделя 3.
**Гейт недели 3 (обновлён 15.08 вечером):** обязательны **3.1 + 3.2 + 3.3 + 3.4 + 3.5**. Неделя 4 — по желанию, не обязательна.

## Ссылки

- Промпт голоса: `voice_mock_prompt.md`
- Gemini (устное): `05_interview_voice/gemini_mock_interview_report.md`
- Фидбек методисту: `01_python_core/01_oop/STUDENT_FEEDBACK_for_sonnet.md`
- HR Ozon 13.08 (пробелы): `docs/sonnet_reviews/2026-08-13-ozon-hr-misses.md`
- Устный API 15.08 + спор 3.3 (исходный триггер): `docs/sonnet_reviews/2026-08-15-oral-api-and-3.3-mocks.md`
- Ревью кода недель 1–3 (15.08): `docs/sonnet_reviews/2026-08-15-week2-3-code-review.md`
- **Рыночная проверка отзыва ученика про моки (15.08, актуальный вердикт):** `docs/sonnet_reviews/2026-08-15-market-vs-student-feedback.md`
- **План-пролонгация 15.08 (актуальный):** `docs/superpowers/plans/2026-08-15-post-32-two-plus-weeks-plan.md`
- **Рекомендации коучу 15.08 (актуальные):** `docs/sonnet_reviews/COACH_RECS_2026-08-15.md`
- Разбор провала пакета 10.08 + вердикт по мокам (первая версия): `docs/sonnet_reviews/2026-08-12-package-failure-and-market-review.md`
- Рыночное саморевью TASK (12.08, базовое): `docs/sonnet_reviews/2026-08-12-task-self-review-vs-real-interviews.md`
- План ASAP 2–4 недели (12.08, базовый): `docs/superpowers/plans/2026-08-12-asap-two-plus-weeks-plan.md`
- Рекомендации коучу (12.08, базовые): `docs/sonnet_reviews/COACH_RECS_2026-08-12.md`
- Резюме — заметки: `docs/resume/RESUME_NOTES_2026-08-10.md`
- Календарь: `CALENDAR.md`
- Банк вопросов (внешний чат): `docs/sonnet_reviews/2026-08-15-dumb-chat-question-bank.md` + `2026-08-15-dumb-chat-question-bank-addendum.md`

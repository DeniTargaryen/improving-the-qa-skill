# Interview Prep Scaffold — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Создать каркас `interview_prep/` и открыть блок 0.1 (частоты / дубликаты / reverse) с падающими тестами на русском.

**Architecture:** Тренажёр рядом с архивом `tasks_tbank/`. Блоки Week 0 идут строго по порядку. Track A = готовые тесты + stub `solution.py`. Документация для ученика — на русском.

**Tech Stack:** Python 3.12+, pytest

---

### Task 1: Каркас interview_prep

**Files:**
- Create: `interview_prep/README.md`
- Create: `interview_prep/PROGRESS.md`
- Create: `interview_prep/resources.md`
- Create: `interview_prep/requirements.txt`
- Create: `interview_prep/pytest.ini`
- Create: `interview_prep/conftest.py`
- Modify: `README.md` (корневой — короткая отсылка)

- [ ] **Step 1:** Создать файлы каркаса (русский README, прогресс, ресурсы, deps)
- [ ] **Step 2:** Проверить, что `pytest` из `interview_prep` стартует без ошибок сбора (пока 0 тестов или только 0.1)

### Task 2: Блок 0.1 — задания

**Files:**
- Create: `interview_prep/00_week0_sprint/01_python_freq_dupes_reverse/TASK.md`
- Create: `interview_prep/00_week0_sprint/01_python_freq_dupes_reverse/solution.py`
- Create: `interview_prep/00_week0_sprint/01_python_freq_dupes_reverse/test_solution.py`

- [ ] **Step 1:** Stub-функции в `solution.py` с `raise NotImplementedError`
- [ ] **Step 2:** Полные тесты в `test_solution.py`
- [ ] **Step 3:** Запуск pytest — ожидаем FAIL (NotImplementedError / import ok)
- [ ] **Step 4:** Обновить PROGRESS.md — блок 0.1 = в работе

### Task 3: Заглушки следующих блоков (только папки + TASK «закрыто»)

**Files:**
- Create: `.../02_python_two_sum/LOCKED.md`
- Create: `.../03_pytest_craft/LOCKED.md`
- Create: `.../04_mini_api_framework/LOCKED.md`
- Create: `.../05_interview_voice/LOCKED.md`

- [ ] **Step 1:** Создать LOCKED.md «не открывать до прохождения предыдущего»

---

**После плана:** ученик работает только в 0.1; ревью до green; затем открываем 0.2.

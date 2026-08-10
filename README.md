# Improving the QA Skill

Тренажёр к AQA-интервью: Python, pytest и API-слои.

Репозиторий: [DeniTargaryen/improving-the-qa-skill](https://github.com/DeniTargaryen/improving-the-qa-skill)

## Правила

1. **Один активный блок.** Пока не сдан — дальше не идём.
2. **Решения без генеративного ИИ.** Не кидай `TASK.md` / тесты в ChatGPT с просьбой «реши».
3. Застрял → пиши коучу: что пробовал, какая ошибка. Подсказки ступенями.
4. Можно: docs.python.org, docs.pytest.org, REPL, поиск по *концепции* («dict get default»).

## Как сдавать

1. Реализуй код в файлах блока.
2. Запусти тесты (см. блок).
3. Напиши в чат: **«готово, блок X»**.
4. Коуч ревьюит. Правки → снова тесты → пока не PASS.

## Старт

Прогресс и текущий блок: `PROGRESS.md`.

```bash
python -m pip install -r requirements.txt
python -m pytest 01_python_core/04_python_trivia -v
```

Внешние ресурсы: `resources.md`. Спеки/планы: `docs/superpowers/`.

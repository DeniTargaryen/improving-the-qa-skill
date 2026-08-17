"""Блок 3.4. Твои Pydantic-модели — по TASK.md. Заготовка без решения:
поля и логика check_values — твоя работа, ничего не скопировать отсюда.

Сам сделал: Entry/Schedule + check_values (явный actual-dict / цикл по expected,
ранний return (False, msg), в конце (True, "")). Вызов Entry через
Entry.check_values(self.entries[i], **entries[i]) — работает; экземплярный
self.entries[i].check_values(**entries[i]) — то же.
Попыток «проверь» (ещё не то): 2. (1) check_values() без kwargs и == True/False;
(2) == (True, "") / (False, "") + NOT_VALID как негатив check_values.
+ промежуточные ревью по модели (не слово «проверь»): self[key]; Entry.check_values
без **; if not result на кортеже; for i in len; перезапись self.entries[i] expected-ом.
Конкретные путаницы: tuple[bool,str] vs bool; пустой check_values() vs сравнение;
ValidationError на создании (NOT_VALID, int vs str) vs check_values на живой модели;
Pydantic BaseModel vs свой check_values.
Можно лучше: actual = self.model_dump(); экземплярный вызов Entry; pytest.raises
на NOT_VALID отдельно. Тесты в test_schedule_model.py — вставка коуча после 2
кривых попыток, не его авторство.
Время/боль: «костыль», злость на кортеж вместо bool."""

Файл называется schedule_model.py, а не models.py — в репозитории уже
есть и будут модули models в разных блоках; без пакетов с __init__.py
общий прогон pytest по всему репо закэшировал бы только первый
импортированный models и подставил его везде (тихий баг, не твоя ошибка).
"""

from pydantic import BaseModel


class Entry(BaseModel):
    """Один месяц графика платежей. Допиши поля — раздел TASK.md '1. Entry'."""
    month: int
    status: str
    payment_total: str
    payment_debt: str

    def check_values(self, **expected_values) -> tuple[bool, str]:
        """Сравнивает свои поля с ожидаемыми. См. TASK.md таблицу 'Что возвращает'."""
        actual = {
            "month": self.month,
            "status": self.status,
            "payment_total": self.payment_total,
            "payment_debt": self.payment_debt,
        }
        # Легче, если поля добавятся: actual = self.model_dump()
        # Pydantic сам соберёт dict всех полей. Цикл ниже тот же.
        for key, value in expected_values.items():
            if actual[key] != value:
                return False, f"Значения ключа {key} невалидно, ожидаем {value}, получили {actual[key]}"
        return True, ""


class Schedule(BaseModel):
    """Весь график платежей. Допиши поля — раздел TASK.md '2. Schedule'."""
    contract_id: str
    entries: list[Entry]

    def check_values(self, entries: list[dict] | None = None, **expected_values) -> tuple[bool, str]:
        """Сравнивает поля графика и (опционально) каждый entry по позиции."""
        if entries is not None:
            for i in range(len(entries)):
                result = Entry.check_values(self.entries[i], **entries[i])
                if not result[0]:
                    return result

        actual = {
            "contract_id": self.contract_id,
        }

        for key, value in expected_values.items():
            if actual[key] != value:
                return False, f"Значения ключа {key} невалидно, ожидаем {value}, получили {actual[key]}"
        return True, ""

"""Блок 3.4. Твои Pydantic-модели — по TASK.md. Заготовка без решения:
поля и логика check_values — твоя работа, ничего не скопировать отсюда.

Файл называется schedule_model.py, а не models.py — в репозитории уже
есть и будут модули models в разных блоках; без пакетов с __init__.py
общий прогон pytest по всему репо закэшировал бы только первый
импортированный models и подставил его везде (тихий баг, не твоя ошибка).
"""

from pydantic import BaseModel


class Entry(BaseModel):
    """Один месяц графика платежей. Допиши поля — раздел TASK.md '1. Entry'."""

    # TODO: month: int
    # TODO: status: str
    # TODO: payment_total: str
    # TODO: payment_debt: str

    def check_values(self, **expected_values) -> tuple[bool, str]:
        """Сравнивает свои поля с ожидаемыми. См. TASK.md таблицу 'Что возвращает'."""
        raise NotImplementedError


class Schedule(BaseModel):
    """Весь график платежей. Допиши поля — раздел TASK.md '2. Schedule'."""

    # TODO: contract_id: str
    # TODO: entries: list[Entry]

    def check_values(self, entries: list[dict] | None = None, **expected_values) -> tuple[bool, str]:
        """Сравнивает поля графика и (опционально) каждый entry по позиции."""
        raise NotImplementedError

"""Твои тесты. См. TASK.md. raw_response.py готов — твоя работа — модели
в schedule_model.py и тесты здесь.

Тело теста — вставка коуча 17.08 после двух его попыток (пустой check_values
и NOT_VALID как негатив метода). Модели он написал сам. Не считать этот файл
доказательством, что он сам проектирует такие ассерты."""

from raw_response import RAW_SCHEDULE_RESPONSE
from schedule_model import Schedule

def test_schedule_model():
    schedule = Schedule(**RAW_SCHEDULE_RESPONSE)

    assert schedule.contract_id == "abc-123"
    assert schedule.entries[0].month == 1
    assert schedule.entries[0].status == "paid"

    ok, msg = schedule.check_values(contract_id="abc-123")
    assert ok is True

    ok, msg = schedule.check_values(contract_id="wrong")
    assert ok is False
    assert "wrong" in msg

    ok, msg = schedule.entries[0].check_values(month=1, status="paid")
    assert ok is True

    ok, msg = schedule.entries[0].check_values(month=99)
    assert ok is False
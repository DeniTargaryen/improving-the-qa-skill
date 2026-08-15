"""Синтетический ответ API с графиком платежей. Готово, не трогай.

Это НЕ данные с реальной работы — числа и поля придуманы для тренажёра,
чтобы блок 3.4 был самодостаточным и не тащил секреты/URL стендов.
"""

RAW_SCHEDULE_RESPONSE = {
    "contract_id": "abc-123",
    "entries": [
        {
            "month": 1,
            "status": "paid",
            "payment_total": "5000.00",
            "payment_debt": "0.00",
        },
        {
            "month": 2,
            "status": "planned",
            "payment_total": "5000.00",
            "payment_debt": "5000.00",
        },
        {
            "month": 3,
            "status": "planned",
            "payment_total": "5000.00",
            "payment_debt": "5000.00",
        },
    ],
}

"""Утилита для блока 0.3 — ГОТОВА, не меняй (кроме случая если тесты требуют уточнения — сначала спроси).

Нормализует телефон РФ к виду +7XXXXXXXXXX или бросает ValueError.
"""


def normalize_phone(raw: str) -> str:
    """Оставь только цифры; приведи к +7 и 11 цифрам после +.

    Примеры:
      '8 (999) 123-45-67' -> '+79991234567'
      '+7 999 123 45 67'  -> '+79991234567'
      '9991234567'        -> '+79991234567'  (10 цифр → дописываем 7)
    """
    if raw is None:
        raise ValueError("empty phone")

    digits = "".join(ch for ch in raw if ch.isdigit())
    if not digits:
        raise ValueError("empty phone")

    if len(digits) == 11 and digits[0] in ("7", "8"):
        digits = "7" + digits[1:]
    elif len(digits) == 10:
        digits = "7" + digits
    else:
        raise ValueError("invalid phone length")

    return f"+{digits}"

"""Retry-хелпер блока 3.5. Готово, не трогай — твоя работа — test_retry_helper.py.

По образцу того, как реально устроены retry-обёртки в промышленных
AQA-фреймворках: оборачивает вызов нестабильной операции (может упасть
от временной проблемы — сеть, сервис на секунду не готов), повторяет
до max_attempts раз с задержкой time.sleep между попытками.
"""

import time


class RetryError(Exception):
    """Кидается, если operation_func так и не отработала за max_attempts попыток."""


def retry_call(operation_func, max_attempts: int = 3, retry_delay: float = 2, **kwargs):
    last_error = None
    for attempt in range(1, max_attempts + 1):
        try:
            return operation_func(**kwargs)
        except Exception as e:
            last_error = e
            if attempt == max_attempts:
                raise RetryError(f"Не удалось за {max_attempts} попыток: {last_error}") from last_error
            time.sleep(retry_delay)

"""Твои тесты. См. TASK.md. retry_helper.py готов — твоя работа — тесты,
которые проверяют retry_call через мок, без реального time.sleep.

Сам сделал: три теста — side_effect-список (2 ошибки + ok), вечный ValueError
→ pytest.raises(RetryError) + call_count == max_attempts, return_value + count 1.
Попыток «проверь» (ещё не то): 2. (1) SyntaxError без «:» у with; always-fail как
result == "fail"; side_effect="pass" (итерация букв) и count==3 на первом успехе.
(2) assert call_count внутри pytest.raises после retry_call — мёртвый код, ложный зелёный.
Конкретные путаницы: return_value vs side_effect vs side_effect=строка (iterable);
RetryError vs текст ValueError; строки после кидка внутри raises не выполняются.
Можно лучше: patch sleep и в тесте «сразу ок» (не блокер: sleep там не вызывается);
пробелы вокруг =.
Время/боль: доёб «опять моки, база важнее» записан 19.08; сам спросил зачем sleep
в последнем — верно, в success-path sleep нет."""

from unittest.mock import Mock, patch

import pytest

from retry_helper import RetryError, retry_call

def test_retry_call_succeeds_on_third_attempt():
    flaky_op=Mock(side_effect=[ValueError(), ValueError(), "ok"])

    with patch("retry_helper.time.sleep"):
        result = retry_call(operation_func=flaky_op, max_attempts=3, retry_delay=1)

    assert result == "ok"
    assert flaky_op.call_count == 3


def test_retry_call_all_attempt_fails_on_fourth_attempt():
    flaky_op=Mock(side_effect=ValueError("fail"))

    with patch("retry_helper.time.sleep"):
        with pytest.raises(RetryError):
            retry_call(operation_func=flaky_op, max_attempts=4, retry_delay=1)
        assert flaky_op.call_count == 4


def test_retry_call_pass():
    flaky_op=Mock(return_value="pass")

    result = retry_call(operation_func=flaky_op, max_attempts=3, retry_delay=1)
    assert result == "pass"
    assert flaky_op.call_count == 1

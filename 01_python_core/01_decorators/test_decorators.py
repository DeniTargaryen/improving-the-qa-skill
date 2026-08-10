import time

import pytest

from retry import retry
from timeit_deco import timeit
from timer import Timer


def test_timeit_returns_same_value(capsys):
    @timeit
    def add(a, b):
        return a + b

    assert add(2, 3) == 5
    captured = capsys.readouterr().out
    assert captured  # что-то напечатали (время)


def test_timeit_preserves_exception(capsys):
    @timeit
    def boom():
        raise RuntimeError("x")

    with pytest.raises(RuntimeError, match="x"):
        boom()


def test_timer_elapsed():
    with Timer() as t:
        time.sleep(0.05)
    assert isinstance(t.elapsed, float)
    assert t.elapsed >= 0.04


def test_timer_enter_returns_self():
    t = Timer()
    assert t.__enter__() is t
    t.__exit__(None, None, None)


def test_retry_succeeds_after_failures():
    calls = {"n": 0}

    @retry(times=3)
    def flaky():
        calls["n"] += 1
        if calls["n"] < 3:
            raise ConnectionError("temporary")
        return "ok"

    assert flaky() == "ok"
    assert calls["n"] == 3


def test_retry_exhausted_reraises():
    calls = {"n": 0}

    @retry(times=2)
    def always_fail():
        calls["n"] += 1
        raise ValueError("nope")

    with pytest.raises(ValueError, match="nope"):
        always_fail()
    assert calls["n"] == 2


def test_retry_success_first_try():
    calls = {"n": 0}

    @retry(times=5)
    def stable():
        calls["n"] += 1
        return 10

    assert stable() == 10
    assert calls["n"] == 1

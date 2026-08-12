"""Демо-тесты для упражнения А. Не переписывай логику — только смотри маркеры.

Каждый тест абсолютно тривиален (просто assert 1 == 1). Смысл файла не в
логике тестов, а в том, что часть из них помечена @pytest.mark.smoke
(уже зарегистрирован в корневом pytest.ini), а часть — новым маркером,
который ты зарегистрируешь сам. См. TASK.md, часть А.
"""
import pytest


@pytest.mark.smoke
def test_login_smoke():
    assert 1 == 1


@pytest.mark.smoke
def test_create_order_smoke():
    assert 1 == 1


@pytest.mark.regression
def test_full_checkout_regression():
    assert 1 == 1


@pytest.mark.regression
def test_refund_flow_regression():
    assert 1 == 1


def test_no_marker_at_all():
    assert 1 == 1

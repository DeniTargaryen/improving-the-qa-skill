"""Блок 0.3 — тесты для normalize_phone."""

import pytest

from phone_utils import normalize_phone

@pytest.mark.smoke
def test_normalize_phone_basic():
    phone = normalize_phone("8 920 06264 14")
    assert phone == "+79200626414"


@pytest.mark.parametrize(
    "actual_phone, expected_phone",
    [
        ("8 920 062 64 14", "+79200626414"),
        ("8921 000 64 14", "+79210006414"),
        ("8020006204", "+78020006204"),
    ],
)
def test_normalize_phone_parametrized(actual_phone: str, expected_phone: str):
    assert normalize_phone(actual_phone) == expected_phone


@pytest.mark.parametrize("bad_phone", ["", "123"])
def test_normalize_phone_invalid(bad_phone):
    with pytest.raises(ValueError):
        normalize_phone(bad_phone)


# Пункты 4–5 (fixture + @pytest.mark.smoke) — пишешь ты ниже
def test_normalize_phone(valid_phone_raw):
    assert normalize_phone(valid_phone_raw) == "+79991234567", "no valid"
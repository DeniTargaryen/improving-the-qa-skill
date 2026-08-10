"""Общий conftest для тренажёра."""

import pytest


@pytest.fixture
def valid_phone_raw():
    return "8 (999) 123-45-67"

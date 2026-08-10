import pytest

from drill import count_frequencies, most_frequent


def test_count_basic():
    assert count_frequencies([1, 3, 3, 2]) == {1: 1, 3: 2, 2: 1}


def test_count_empty():
    assert count_frequencies([]) == {}


def test_most_clear_winner():
    assert most_frequent([1, 3, 3, 2, 1, 3]) == 3


def test_most_tie_first():
    assert most_frequent([1, 2, 1, 2]) == 1


def test_most_empty_raises():
    with pytest.raises(ValueError):
        most_frequent([])

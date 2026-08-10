import pytest

from solution import (
    count_frequencies,
    find_duplicates,
    most_frequent,
    reverse_string,
)


class TestCountFrequencies:
    def test_basic(self):
        assert count_frequencies([1, 3, 3, 2]) == {1: 1, 3: 2, 2: 1}

    def test_empty(self):
        assert count_frequencies([]) == {}

    def test_strings(self):
        assert count_frequencies(["a", "b", "a"]) == {"a": 2, "b": 1}


class TestFindDuplicates:
    def test_basic(self):
        assert find_duplicates([1, 2, 3, 2, 1, 7]) == [1, 2]

    def test_no_duplicates(self):
        assert find_duplicates([1, 2, 3]) == []

    def test_empty(self):
        assert find_duplicates([]) == []

    def test_all_same(self):
        assert find_duplicates([5, 5, 5]) == [5]


class TestMostFrequent:
    def test_clear_winner(self):
        assert most_frequent([1, 3, 3, 2, 1, 3]) == 3

    def test_tie_returns_first_seen(self):
        assert most_frequent([1, 2, 1, 2]) == 1

    def test_single_element(self):
        assert most_frequent([42]) == 42

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            most_frequent([])


class TestReverseString:
    def test_basic(self):
        assert reverse_string("Yandex") == "xednaY"

    def test_empty(self):
        assert reverse_string("") == ""

    def test_palindrome(self):
        assert reverse_string("aba") == "aba"

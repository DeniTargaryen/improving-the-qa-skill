import pytest

from trivia import add_item, call_with, clone_rows


def test_add_item_default_not_shared():
    first = add_item("a")
    second = add_item("b")
    assert first == ["a"]
    assert second == ["b"]
    assert first is not second


def test_add_item_uses_provided_bag():
    bag = []
    assert add_item("x", bag) is bag
    assert add_item("y", bag) == ["x", "y"]


def test_clone_rows_isolates_inner_lists():
    rows = [[1], [2]]
    cloned = clone_rows(rows)
    cloned[0][0] = 9
    assert rows[0][0] == 1
    assert cloned[0][0] == 9


def test_clone_rows_empty():
    assert clone_rows([]) == []


def test_call_with_positional():
    def add(a, b):
        return a + b

    assert call_with(add, 2, 3) == 5


def test_call_with_kwargs():
    def greet(name):
        return f"hi {name}"

    assert call_with(greet, name="Ann") == "hi Ann"


def test_call_with_preserves_exception():
    def boom():
        raise ValueError("nope")

    with pytest.raises(ValueError, match="nope"):
        call_with(boom)

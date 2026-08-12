"""Питон-тривиа — блок 1.4 (код к TASK Б/В/Г)."""
from copy import deepcopy


def add_item(item, bag=None) -> list:
    if bag is None:
        bag = []
        bag.append(item)
        return bag
    else:
        bag.append(item)
        return bag


def clone_rows(rows) -> list:
    if rows is None:
        return []
    else:
        return deepcopy(rows)


def call_with(fn, *args, **kwargs):
    c = fn(*args, **kwargs)
    return c

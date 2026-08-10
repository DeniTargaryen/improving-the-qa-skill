"""Drill 02: count_frequencies + most_frequent. Без подглядывания в блок 0.1."""
import operator


def count_frequencies(items: list) -> dict:
    seen ={}
    for item in items:
        if item not in seen:
            seen[item] = 1
        else:
            seen[item] += 1
    return seen


def most_frequent(items: list):
    seen = count_frequencies(items)
    if not items:
        raise ValueError
    max_num = 0
    max_cnt = 0
    for i in seen:
        if seen[i] > max_cnt:
            max_cnt = seen[i]
            max_num = i
    return max_num

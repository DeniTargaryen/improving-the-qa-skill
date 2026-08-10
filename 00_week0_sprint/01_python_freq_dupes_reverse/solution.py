"""Блок 0.1 — реализуй функции ниже. Тесты трогать не нужно."""


def count_frequencies(items: list) -> dict:
    """Верни словарь: элемент -> количество вхождений."""
    frequency_dict = {}
    for item in items:
        if item not in frequency_dict:
            frequency_dict[item] = 1
        else:
            frequency_dict[item] += 1
    return frequency_dict


def find_duplicates(items: list) -> list:
    """Верни отсортированный список элементов, встречающихся > 1 раза."""
    dupes = []
    frequency_dict=count_frequencies(items)
    for item in frequency_dict:
        if frequency_dict[item] > 1:
            dupes.append(item)
    return dupes


def most_frequent(items: list):
    """Верни самый частый элемент. При ничьей — тот, что раньше в списке.
    Пустой список → ValueError.
    """
    if len(items) == 0:
        raise ValueError
    frequency_dict = {}
    for item in items:
        if item not in frequency_dict:
            frequency_dict[item] = 1
        else:
            frequency_dict[item] += 1
    max_value = 0
    for key, value in frequency_dict.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key


def reverse_string(s: str) -> str:
    """Верни строку задом наперёд."""
    return s[::-1]

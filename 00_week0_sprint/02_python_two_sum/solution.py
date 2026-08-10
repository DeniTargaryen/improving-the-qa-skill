"""Блок 0.2 — Two Sum. Реализуй обе функции."""


def two_sum_brute(nums: list[int], target: int) -> tuple[int, int] | None:
    """Найди индексы пары через два цикла. Нет пары → None."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j
    return None


def two_sum_dict(nums: list[int], target: int) -> tuple[int, int] | None:
    """Найди индексы пары через словарь за один проход. Нет пары → None."""
    seen = {}
    for i in range(len(nums)):
        x = nums[i]
        need = target - x
        if need in seen:
            return seen[need], i
        seen[x] = i

    return None

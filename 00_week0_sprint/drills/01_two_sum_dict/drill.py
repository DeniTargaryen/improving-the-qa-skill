"""Drill: two_sum_dict с нуля. Сотри и напиши заново завтра. Не смотри блок 0.2."""


def two_sum_dict(nums: list[int], target: int) -> tuple[int, int] | None:
    seen = {}
    for i in range(len(nums)):
        x = nums[i]
        need = target - x
        if need not in seen:
            seen[x] = i
            print(f'seen[x]=')
            print(seen[x])
        else:
            return seen[need], i
    return None
from solution import two_sum_brute, two_sum_dict


def _check_pair(fn, nums, target, expect_none=False):
    result = fn(nums, target)
    if expect_none:
        assert result is None
        return
    assert result is not None
    i, j = result
    assert i != j
    assert nums[i] + nums[j] == target


class TestTwoSumBrute:
    def test_basic(self):
        _check_pair(two_sum_brute, [2, 7, 11, 15], 9)

    def test_duplicates(self):
        _check_pair(two_sum_brute, [3, 3], 6)

    def test_no_pair(self):
        _check_pair(two_sum_brute, [1, 2, 3], 100, expect_none=True)

    def test_empty(self):
        _check_pair(two_sum_brute, [], 0, expect_none=True)

    def test_single(self):
        _check_pair(two_sum_brute, [5], 5, expect_none=True)


class TestTwoSumDict:
    def test_basic(self):
        _check_pair(two_sum_dict, [2, 7, 11, 15], 9)

    def test_duplicates(self):
        _check_pair(two_sum_dict, [3, 3], 6)

    def test_later_pair(self):
        _check_pair(two_sum_dict, [1, 4, 5, 8], 13)

    def test_no_pair(self):
        _check_pair(two_sum_dict, [1, 2, 3], 100, expect_none=True)

    def test_negative(self):
        _check_pair(two_sum_dict, [-1, 5, 3], 2)

from drill import two_sum_dict


def test_basic():
    i, j = two_sum_dict([2, 7, 11, 15], 9)
    assert i != j
    assert [2, 7, 11, 15][i] + [2, 7, 11, 15][j] == 9


def test_duplicates():
    i, j = two_sum_dict([3, 3], 6)
    assert (i, j) == (0, 1)


def test_no_pair():
    assert two_sum_dict([0, 1, 2, 4, 5], 99) is None

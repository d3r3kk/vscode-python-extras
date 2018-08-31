import multiply


def test_times_100():
    multiplier = multiply.bind_multiply(100)

    assert multiplier(5) == 500
    assert multiplier(10) == 1000


def test_times_negative_1():
    multiplier = multiply.bind_multiply(-1)

    assert multiplier(3) == -3
    assert multiplier(7) == -7

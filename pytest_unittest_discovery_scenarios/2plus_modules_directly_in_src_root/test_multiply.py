import multiply


def test_times_10():
    multiplier = multiply.bind_multiply(10)

    assert multiplier(5) == 50
    assert multiplier(10) == 100


def test_times_2():
    multiplier = multiply.bind_multiply(2)

    assert multiplier(3) == 6
    assert multiplier(7) == 14

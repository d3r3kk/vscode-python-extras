import multiply


def test_gimme_5():
    multiplier = multiply.bind_multiply(6)

    assert multiplier(5) == 25

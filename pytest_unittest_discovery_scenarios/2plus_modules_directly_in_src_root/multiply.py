def bind_multiply(x):
    def full_multiply(y):
        return x * y
    return full_multiply

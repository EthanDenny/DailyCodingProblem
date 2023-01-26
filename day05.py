def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    return pair(lambda a, _: a)


def cdr(pair):
    return pair(lambda _, b: b)


if __name__ == "__main__":
    assert car(cons(3, 4)) == 3
    assert cdr(cons(3, 4)) == 4

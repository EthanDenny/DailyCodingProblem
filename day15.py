import random


class Stream():
    _count = 0

    def __init__(self, count):
        self._count = count
    
    def get(self):
        return random.randint(1, self._count)
    
    def __len__(self):
        return self._count


def f(elems):
    n = len(elems)
    while (e := elems.get()):
        n -= 1
        if random.randint(0, n) == 0:
            return e


if __name__ == "__main__":
    elems = Stream(1000)
    print(f(elems))

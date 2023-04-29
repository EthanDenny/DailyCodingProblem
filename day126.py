def f(list, k):
    for i in range(k):
        n = list.pop(0)
        list.append(n)

if __name__ == '__main__':
    list = [1, 2, 3, 4, 5, 6]
    f(list, 2)
    assert list == [3, 4, 5, 6, 1, 2]

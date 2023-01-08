def overlap(a, b):
    return a[1] > b[0] and a[0] < b[1]


def f(intervals):
    rooms = 0

    i = 0
    while i < len(intervals):
        j = i + 1
        while j < len(intervals):
            if overlap(intervals[i], intervals[j]):
                rooms += 1
            j += 1
        i += 1
    
    return rooms


if __name__ == "__main__":
    assert f([(30, 75), (0, 50), (60, 150)]) == 2

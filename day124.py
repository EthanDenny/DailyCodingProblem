def f(n):
    if n == 0:
        return -1
    else:
        return 1 + f(n // 2)

print(f(5))

def f(n):
    x = 1.0
    t = 1.0

    while round(x ** 2) != n:
        while x ** 2 < n:
            x += t
        x -= t
        t /= 10
    
    return x

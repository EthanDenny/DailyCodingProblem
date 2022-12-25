# Approximate the nth Fibbonaci number
def binets_formula(n):
    SQRT_5 = 2.23601
    PHI = (SQRT_5 + 1) / 2
    fib = round(PHI ** n / SQRT_5)
    return fib


def f(message):
    if len(message) <= 1: return 1

    ways = 1 # The number of ways the message can be decoded
    run = 0 # The number of consecutive two-letter combos (e.g. 111 -> 3, 131 -> 1, 121 -> 3, 229 -> 1)

    for i in range(len(message) - 1):
        ch = message[i]
        next_ch = message[i+1]
        if ch == '1' or (ch == '2' and int(next_ch) < 7):
            run += 1
        else:
            ways *= binets_formula(run + 2)
            run = 0
    ways *= binets_formula(run + 2)
    
    return ways


if __name__ == "__main__":
    assert f('111') == 3

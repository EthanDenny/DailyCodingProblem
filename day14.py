import math
import random


def monte_carlo_pi(points=1000, precision=None):
    n = 0 # Number of points in circle

    for i in range(points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 < 1: n += 1
    
    pi = n / points * 4

    if precision:
        pi = round(pi, precision)

    return pi


if __name__ == "__main__":
    pi = monte_carlo_pi(points=1000000, precision=3)
    print(pi)

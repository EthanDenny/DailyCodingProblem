import math


def get_combinations(N, X, up_to=None):
    combs = []

    if up_to == None:
        X = sorted(X)
        up_to = len(X)
    
    for i in range(up_to):
        x = X[i]
        if x == N:
            combs.append({x: 1})
        elif x < N:
            sub_combs = get_combinations(N - x, X, up_to=i+1)
            for comb in sub_combs:
                if x in comb: comb[x] += 1
                else: comb[x] = 1
                combs.append(comb)

    return combs


def get_permutations(combs):
    ways = 0
    for comb in combs:
        num = math.factorial(sum(comb.values()))
        den = math.prod([math.factorial(val) for val in comb.values()])
        ways += num // den
    return ways


def get_unique_ways(N, X):
    combs = get_combinations(N, X)
    perms = get_permutations(combs)
    return perms


if __name__ == "__main__":
    assert get_unique_ways(4, {1, 2}) == 5
    assert get_unique_ways(9, {1, 3, 5}) == 30

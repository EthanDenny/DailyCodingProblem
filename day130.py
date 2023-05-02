def f(prices, k):
    largest_diffs = [0]*k

    for i in range(len(prices)-1):
        diff = 0

        for j in range(i+1, len(prices)):
            diff = max(diff, prices[j] - prices[i])
        
        smallest_diff = min(largest_diffs)

        if smallest_diff < diff:
            largest_diffs.remove(smallest_diff)
            largest_diffs.append(diff)

    return sum(largest_diffs)

if __name__ == '__main__':
    prices = [5, 2, 4, 0, 1]
    assert f(prices, 2) == 3

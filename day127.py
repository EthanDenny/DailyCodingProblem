from collections import deque

def sum_list(list: deque) -> int:
    total = 0
    i = 0

    while list:
        n = list.popleft()
        total += n * (10 ** i)
        i += 1
    
    return total

def f(list_a: deque, list_b: deque) -> deque:
    total_deque = deque()

    total = sum_list(list_a) + sum_list(list_b)
    
    while total > 0:
        total_deque.append(total % 10)
        total //= 10

    return total_deque

if __name__ == '__main__':
    list_a = deque([9, 9])
    list_b = deque([5, 2])
    total_deque = f(list_a, list_b)
    assert total_deque == deque([4, 2, 1])

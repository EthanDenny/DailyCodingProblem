def f(nums, k):
    found_nums = {}

    for n in nums:
        found_nums[n] = 0
        if k - n in found_nums:
            return True
    
    return False


if __name__ == "__main__":
    nums = [10, 15, 3, 7]
    k = 17
    result = f(nums, k)
    print(result)

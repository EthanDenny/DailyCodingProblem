def f(nums):
    i = 0
    while i < len(nums):
        n = nums[i]

        if 0 < n < len(nums):
            temp = nums[n]
            nums[n] = nums[i]
            nums[i] = temp
            if n == temp:
                i += 1
        else:
            i += 1

    low = 1
    for n in nums:
        if low == n:
            low += 1
    return low


if __name__ == "__main__":
    nums = [3, 4, -1, 1]
    result = f(nums)
    print(result)

    nums = [2, 1, 0]
    result = f(nums)
    print(result)

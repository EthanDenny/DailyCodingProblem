def f(nums):
    for i in range(len(nums)):
        while 0 < (n := nums[i]) < len(nums):
            if nums[n - 1] == nums[i]: break
            nums[n - 1], nums[i] = nums[i], nums[n - 1]

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

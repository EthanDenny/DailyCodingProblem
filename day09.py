def f(nums):
    sum = 0

    i = 0
    while i < len(nums):
        remaining_len = len(nums) - i

        if remaining_len == 1:
            sum += nums[i]
            break
        elif remaining_len == 2:
            a = nums[i]
            b = nums[i+1]
            sum += max(a, b)
            break
        elif remaining_len == 3:
            a = nums[i] + nums[i+2]
            b = nums[i+1]
            sum += max(a, b)
            break
        else:
            a = nums[i] + nums[i+2]
            b = nums[i+1] + nums[i+3]

            if a >= b:
                sum += nums[i]
                i += 2
            else:
                sum += nums[i+1]
                i += 3
    
    return sum


if __name__ == "__main__":
    assert f([2, 4, 6, 2, 5]) == 13
    assert f([5, 1, 1, 5]) == 10

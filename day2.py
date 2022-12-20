def f(nums):
    superprod = 1
    for n in nums:
        superprod *= n

    products = [superprod // n for n in nums]

    return products


def f_no_div(nums):
    products = [1]

    for i in range(1, len(nums)):
        N = products[-1] * nums[len(products) - 1]
        
        for j in range(len(products)):
            products[j] *= nums[i]
        
        products.append(N)
    
    return products


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]

    result = f(nums)
    print(result)

    result = f_no_div(nums)
    print(result)

from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)

    prefix = [1] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] * nums[i]

    suffix = [1] * (n + 1)
    for i in range(n):
        suffix[i + 1] = suffix[i] * nums[n - i - 1]

    result = [1] * n
    for i in range(n):
        result[i] = prefix[i] * suffix[n - i - 1]
    return result

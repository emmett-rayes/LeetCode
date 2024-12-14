from typing import List


def permute_unique(nums: List[int]) -> List[List[int]]:
    if len(nums) == 0:
        return []

    if len(nums) == 1:
        return [nums]

    result = set()
    head = nums[0]
    tail = nums[1:]
    for sub_permutation in permute_unique(tail):
        for i in range(len(sub_permutation) + 1):
            permutation = sub_permutation[:i] + [head] + sub_permutation[i:]
            result.add(tuple(permutation))

    return [list(permutation) for permutation in result]

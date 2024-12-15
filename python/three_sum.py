from typing import List

def two_sum(nums:[int], exclude: int, target: int, ) -> List[List[int]]:
    result = []
    complements = {}
    for (i, n) in enumerate(nums):
        if i == exclude:
            continue
        if n in complements:
            result.append([complements[n], n])
        complements[target - n] = n
    return result

def three_sum(nums: List[int]) -> List[List[int]]:
    result = set()
    for (k, n) in enumerate(nums):
        ijs = two_sum(nums, exclude=k, target=-n)
        for ij in ijs:
            result.add(tuple(sorted(ij + [n])))
    return [list(t) for t in result]

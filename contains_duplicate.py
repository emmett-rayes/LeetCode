from typing import List


def contains_duplicate(nums: List[int]):
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1

    for n in freq:
        if freq[n] > 1:
            return True
    return False

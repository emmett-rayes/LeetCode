from typing import List


def longest_consecutive(nums: List[int]) -> int:
    maximal = []
    nums_set = set(nums)
    for n in nums_set:
        if not n + 1 in nums_set:
            maximal.append(n)

    max_seq = 0
    for m in maximal:
        k = m
        curr_seq = 0
        while k in nums_set:
            curr_seq += 1
            k -= 1
        max_seq = max(max_seq, curr_seq)
    return max_seq

from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1

    sorted_freq = [[] for _ in range(len(nums))]
    for n in freq:
        i = freq[n] - 1  # zero-indexed
        sorted_freq[i].append(n)

    result = []
    for bucket in reversed(sorted_freq):
        for n in bucket:
            result.append(n)
            if len(result) == k:
                return result

    return result  # not reachable if answer exists
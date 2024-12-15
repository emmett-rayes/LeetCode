from typing import List


def majority_element_hashmap(nums: List[int]) -> int:
    frequencies = {}
    for n in nums:
        frequencies[n] = frequencies.get(n, 0) + 1

    max_freq = 0
    result = nums[0]
    for (n, freq) in frequencies.items():
        if freq > max_freq:
            max_freq = freq
            result = n

    return result


# solved using Boyer-Moore
def majority_element_space_optimized(nums: List[int]) -> int:
    curr = nums[0]
    count = 0
    for n in nums:
        if count == 0:
            curr = n
        if n == curr:
            count += 1
        else:
            count -= 1
    return curr

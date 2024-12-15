from typing import List


def minimum_in_rotated_sorted_array(nums: List[int]) -> int:
    l = 0
    r = len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if nums[m] < nums[m - 1]:
            return nums[m]
        if nums[-1] < nums[m]:  # m is in rotated part
            l = m + 1
        else:
            r = m - 1
    return nums[l]

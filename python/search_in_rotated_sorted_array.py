from typing import List


def search_in_rotated_sorted_array(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        curr = nums[m]
        if curr == target:
            return m
        if curr > target:
            if curr > nums[-1]:  # curr in rotated list
                if target > nums[-1]:  # target would be in rotated list
                    r = m - 1
                else:
                    l = m + 1
            else:
                r = m - 1
        if curr < target:
            if curr > nums[-1]:  # curr in rotated list
                l = m + 1
            else:
                if target > nums[-1]:  # target would be in rotated list
                    r = m - 1
                else:
                    l = m + 1
    return -1

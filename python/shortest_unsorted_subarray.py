from typing import List


def shortest_unsorted_subarray(nums: List[int]) -> int:
    # find boundaries where there are sorting condition violations
    # the lower and upper bound will span a subarray that has to be sorted
    # this is because none of the found violations can remain after sorting
    # therefore they all belong to the spanning subarray
    l = 0
    r = 1
    bounds = []
    while r < len(nums):
        if nums[l] > nums[r]:
            bounds.append(l)
            bounds.append(r)
        l += 1
        r += 1

    if len(bounds) == 0:
        return 0

    l = bounds[0]
    r = bounds[-1]

    # find the minimum and maximum elements of the subarray
    # these elements are interesting because after sorting they will be on the edges
    # we need to make sure that they do not violate the sorting condition with their outside neighbors
    # to that end we keep extending the spanning subarray until it includes an element that is lower/higher
    # than the lower/upper bound
    # since the outside is sorted per definition the closest element to the subarray bounds we find is
    # the element that minimizes the subarray to be sorted
    minimal = nums[l]
    maximal = nums[l]
    for i in range(l, r + 1):
        minimal = min(minimal, nums[i])
        maximal = max(maximal, nums[i])

    while 0 <= l and nums[l] > minimal:
        l -= 1

    while r < len(nums) and nums[r] < maximal:
        r += 1

    return r - l - 1  # = (r - 1) - (l + 1) + 1

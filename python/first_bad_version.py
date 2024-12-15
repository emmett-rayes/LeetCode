def is_bad_version(version: int) -> bool:
    raise NotImplementedError()


def first_bad_version(n: int) -> int:
    left = 1
    right = n
    while left < right:
        curr = (left + right) // 2  # = left + (right - left) // 2
        if is_bad_version(curr):
            right = curr
        else:
            left = curr + 1
    return left

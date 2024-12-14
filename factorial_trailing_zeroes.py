def factorial_trailing_zeroes(n: int) -> int:
    result = 0
    fives = 5
    while fives <= n:
        result += n // fives
        fives *= 5
    return result

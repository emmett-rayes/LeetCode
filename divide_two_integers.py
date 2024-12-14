def divide(dividend: int, divisor: int) -> int:
    if dividend == 0:
        return 0
    if dividend == divisor:
        return 1

    positive = (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0)
    dividend = abs(dividend)
    divisor = abs(divisor)

    if divisor == 1:
        result = dividend
    elif divisor == -1:
        result = -dividend
    else:
        result = 0
        remainder = dividend
        while divisor <= remainder:
            factor = divisor
            counter = 0
            while factor <= remainder:
                factor = factor << 1
                counter += 1
            result += 1 << (counter - 1)
            remainder -= factor >> 1

    result = result if positive else -result
    upper_limit = (1 << 31) - 1
    lower_limit = - (1 << 31)
    if upper_limit < result:
        result = upper_limit
    if result < lower_limit:
        result = lower_limit

    return result

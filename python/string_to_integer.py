from typing import Optional


def char_to_digit(c: str) -> Optional[int]:
    if c == "0":
        return 0
    if c == "1":
        return 1
    if c == "2":
        return 2
    if c == "3":
        return 3
    if c == "4":
        return 4
    if c == "5":
        return 5
    if c == "6":
        return 6
    if c == "7":
        return 7
    if c == "8":
        return 8
    if c == "9":
        return 9
    else:
        return None


def my_atoi(s: str) -> int:
    # trim white space
    i = 0
    while i < len(s) and s[i] == " ":
        i += 1
    s = s[i:]

    # empty string is equivalent to 0
    if len(s) == 0:
        return 0

    # determine signedness
    if s[0] == "-":
        s = s[1:]
        sign = -1
    elif s[0] == "+":
        s = s[1:]
        sign = 1
    else:
        sign = 1

    # stop before non-digit characters
    i = 0
    while i < len(s) and char_to_digit(s[i]) is not None:
        i += 1
    s = s[:i]

    # skip leading zeroes
    i = 0
    while i < len(s) and s[i] == "0":
        i += 1
    s = s[i:]

    # empty string is equivalent to 0
    if len(s) == 0:
        return 0

    result = 0
    for i in range(len(s) - 1, -1, -1):
        exp = len(s) - 1 - i
        result += (10 ** exp) * char_to_digit(s[i])

        # stay within limit
        upper_limit = (1 << 31) - 1
        if sign * result > upper_limit:
            return upper_limit

        lower_limit = -(1 << 31)
        if sign * result < lower_limit:
            return lower_limit

    return sign * result


print(my_atoi("+-12"))

def add_binary(a: str, b: str) -> str:
    if len(a) < len(b):
        a = "0" * (len(b) - len(a)) + a
    elif len(b) < len(a):
        b = "0" * (len(a) - len(b)) + b

    carry = "0"
    result = ""
    for a0, b0 in zip(reversed(a), reversed(b)):
        if a0 == "0" and b0 == "0":
            r0 = carry
            carry = "0"
        elif a0 == "1" and b0 == "1":
            r0 = carry
            carry = "1"
        else:
            if carry == "0":
                r0 = "1"
            else:
                r0 = "0"
        result = r0 + result

    if carry == "1":
        return carry + result
    else:
        return result

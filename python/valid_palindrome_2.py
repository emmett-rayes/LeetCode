def is_palindrome(s: str, prefer_left: bool) -> bool:
    l = 0
    r = len(s) - 1
    violations = 1
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            if violations == 0:
                return False
            else:
                if prefer_left:
                    if s[l] == s[r - 1]:
                        violations -= 1
                        l += 1
                        r -= 2
                    elif s[l + 1] == s[r]:
                        violations -= 1
                        l += 2
                        r -= 1
                    else:
                        return False
                else:
                    if s[l + 1] == s[r]:
                        violations -= 1
                        l += 2
                        r -= 1
                    elif s[l] == s[r - 1]:
                        violations -= 1
                        l += 1
                        r -= 2
                    else:
                        return False
    return True


def valid_palindrome(s: str) -> bool:
    return is_palindrome(s, False) or is_palindrome(s, True)

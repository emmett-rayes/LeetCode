def rotate_string(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False

    l = len(s)
    for (i, a) in enumerate(s):
        for (j, b) in enumerate(goal):
            if a == b:
                # found a candidate for common starting point
                # compare all characters along the whole length
                ps = (i + 1) % l
                pg = (j + 1) % l
                for _ in range(l - 1):
                    if s[ps] != goal[pg]:
                        break
                    ps = (ps + 1) % l
                    pg = (pg + 1) % l
                else:
                    return True
    return False

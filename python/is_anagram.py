def frequencies(s: str) -> dict[str, int]:
    result = {}
    for c in s:
        result[c] = result.get(c, 0) + 1
    return result

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_freq = frequencies(s)
    t_freq = frequencies(t)
    return s_freq == t_freq

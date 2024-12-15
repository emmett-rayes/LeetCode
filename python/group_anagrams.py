from typing import List


def frequencies(s: str) -> frozenset[tuple[str, int]]:
    result = {}
    for c in s:
        result[c] = result.get(c, 0) + 1
    return frozenset(result.items())


def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups = {}
    for s in strs:
        freq = frequencies(s)
        groups[freq] = groups.get(freq, []) + [s]
    return list(groups.values())

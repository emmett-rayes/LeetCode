def word_pattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(words) != len(pattern):
        return False

    seen = set()
    lookup = {}
    for (p, w) in zip(pattern, words):
        if not p in lookup:
            if w in seen:
                return False
            seen.add(w)
            lookup[p] = w
        elif not lookup[p] == w:
            return False
    return True

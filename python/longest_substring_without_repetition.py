def longest_substring_without_repetition(s: str) -> int:
    seen = {}
    l = 0
    r = 0
    longest = 0
    while r < len(s):
        if s[r] in seen and seen[s[r]] >= l:
            l = seen[s[r]] + 1
        seen[s[r]] = r
        longest = max(longest, r - l + 1)
        r += 1

    return longest

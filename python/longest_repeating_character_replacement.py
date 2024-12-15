def longest_repeating_character_replacement(s: str, k: int) -> int:
    l = 0
    r = 0
    freq = {}
    max_freq = 0
    max_length = 0
    while r < len(s):
        freq[s[r]] = freq.get(s[r], 0) + 1
        max_freq = max(max_freq, freq[s[r]])
        while l < r and (r - l + 1) - max_freq > k:
            freq[s[l]] = freq[s[l]] - 1
            l += 1
        max_length = max(max_length, r - l + 1)
        r += 1
    return max_length

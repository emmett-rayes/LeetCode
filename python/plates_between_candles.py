from typing import List


def plates_between_candles(s: str, queries: List[List[int]]) -> List[int]:
    next_pipe = {}
    last_pipe = None
    i = len(s) - 1
    while 0 <= i:
        if s[i] == "|":
            last_pipe = i
        if last_pipe is not None:
            next_pipe[i] = last_pipe
        i -= 1

    items = {}
    current = 0
    count = 0
    counting = False
    for (i, c) in enumerate(s):
        if c == "|":
            current = count
            if not counting:
                counting = True
        else:
            if counting:
                count += 1
        items[i] = current

    result = []
    for [start, end] in queries:
        if start not in next_pipe:
            result.append(0)
        else:
            count = items[end] - items[next_pipe[start]]
            result.append(max(0, count))
    return result

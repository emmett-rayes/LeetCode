from collections import deque
from typing import List, Tuple


def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    def neighbors(r: int, c: int) -> List[Tuple[int, int]]:
        result = []
        if 0 <= r - 1:
            result.append((r - 1, c))
        if r + 1 < len(image):
            result.append((r + 1, c))
        if 0 <= c - 1:
            result.append((r, c - 1))
        if c + 1 < len(image[r]):
            result.append((r, c + 1))
        return result

    if image[sr][sc] == color:
        return image

    color_orig = image[sr][sc]
    visited = set()
    queue = deque()
    queue.appendleft((sr, sc))
    while len(queue) != 0:
        (r, c) = queue.pop()
        visited.add((r, c))
        image[r][c] = color
        for (nr, nc) in neighbors(r, c):
            if image[nr][nc] == color_orig and not (nr, nc) in visited:
                queue.appendleft((nr, nc))

    return image

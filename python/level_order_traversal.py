from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if root is None:
        return []

    todo = deque()
    todo.append(root)

    result = []
    level = []
    level_size = len(todo)
    while len(todo) != 0:
        curr = todo.popleft()
        level.append(curr.val)
        if curr.left is not None:
            todo.append(curr.left)
        if curr.right is not None:
            todo.append(curr.right)
        if len(level) == level_size:  # reached end of level
            result.append(level)
            level = []
            level_size = len(todo)
    return result

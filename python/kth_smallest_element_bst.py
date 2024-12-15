from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    def traverse(node: TreeNode) -> List[int]:
        result = []
        if node.left is not None:
            result.extend(traverse(node.left))
        result.append(node.val)
        if node.right is not None:
            result.extend(traverse(node.right))
        return result

    return traverse(root)[k - 1]

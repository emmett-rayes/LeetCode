from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    def rec(node: TreeNode) -> Optional[tuple[int, int]]:
        if node.left is None and node.right is None:
            return (node.val, node.val)

        valid_left = rec(node.left) if node.left else (node.val, node.val)
        valid_right = rec(node.right) if node.right else (node.val, node.val)

        if not valid_left or not valid_right:
            return None
        if node.left and node.val <= valid_left[1]:
            return None
        if node.right and valid_right[0] <= node.val:
            return None

        return (valid_left[0], valid_right[1])

    return False if root is None or rec(root) is None else True

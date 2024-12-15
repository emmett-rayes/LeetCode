from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return root
    left = invert_tree(root.right)
    right = invert_tree(root.left)
    root.left = left
    root.right = right
    return root

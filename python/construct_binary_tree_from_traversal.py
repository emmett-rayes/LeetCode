from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if len(preorder) == 0:
        return None

    root_val = preorder[0]
    i = 0
    while i < len(inorder) and inorder[i] != root_val:
        i += 1

    left_inorder = inorder[:i]
    right_inorder = inorder[i + 1:]
    left_preorder = preorder[1: len(left_inorder) + 1]
    right_preorder = preorder[len(left_preorder) + 1:]

    root = TreeNode(root_val)
    root.left = build_tree(left_preorder, left_inorder)
    root.right = build_tree(right_preorder, right_inorder)

    return root

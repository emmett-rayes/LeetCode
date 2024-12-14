from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sorted_array_to_bst(nums: List[int]) -> Optional[TreeNode]:
    if len(nums) == 0:
        return None

    if len(nums) == 1:
        return TreeNode(nums[0])
    else:
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = sorted_array_to_bst(nums[:mid])
        node.right = sorted_array_to_bst(nums[mid + 1:])
        return node

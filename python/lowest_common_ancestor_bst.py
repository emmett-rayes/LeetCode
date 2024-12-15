from typing import List, Union


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def compute_path(root: TreeNode, p: TreeNode, q: TreeNode) -> Union[TreeNode, List[TreeNode]]:
    path_p = []
    curr = root
    while curr is not None:
        if curr == p:
            break
        if curr == q:  # q is an ancestor of p
            return q
        path_p.append(curr)
        if p.val < curr.val:
            curr = curr.left
        else:
            curr = curr.right
    return path_p


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    path_p = compute_path(root, p, q)
    if isinstance(path_p, TreeNode):
        return path_p

    path_q = compute_path(root, q, p)
    if isinstance(path_q, TreeNode):
        return path_q

    s = set(path_p)
    for n in reversed(path_q):
        if n in s:
            return n


def lowest_common_ancestor_iter(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if p is None or q is None:
        return root

    curr = root
    while curr is not None:
        if max(p.val, q.val) < curr.val:  # p and q are in the left subtree
            curr = curr.left
        elif min(p.val, q.val) > curr.val:  # p and q are in the right subtree
            curr = curr.right
        else:  # p and q are in different subtrees which means curr is the LCA
            return curr

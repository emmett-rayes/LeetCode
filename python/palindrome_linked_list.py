from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome(head: Optional[ListNode]) -> bool:
    vals = []
    curr = head
    while curr is not None:
        vals.append(curr.val)
        curr = curr.next

    l = 0
    r = len(vals) - 1
    while l < r:
        if vals[l] != vals[r]:
            return False
        l += 1
        r -= 1
    return True

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

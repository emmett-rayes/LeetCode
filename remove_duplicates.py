from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None

    curr = head
    while curr is not None:
        lookahead = curr
        while lookahead is not None and lookahead.val == curr.val:
            lookahead = lookahead.next
        curr.next = lookahead
        curr = lookahead

    return head

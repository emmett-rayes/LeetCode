from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        vals = []
        curr = self
        while curr is not None:
            vals.append(curr.val)
            curr = curr.next
        return "[" + ",".join([str(val) for val in vals]) + "]"


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    last = None
    while head is not None:
        tmp = head
        head = head.next
        tmp.next = last
        last = tmp
    return last




print(reverse_list(ListNode(1, ListNode(2, ListNode(3)))))

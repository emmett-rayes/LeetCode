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


def merge_two_sorted_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    result = ListNode()
    curr = result
    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    if list1 is not None:
        curr.next = list1
    if list2 is not None:
        curr.next = list2
    return result.next

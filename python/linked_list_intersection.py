from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def linked_list_intersection_hashmap(head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
    visited = set()
    while head_a is not None or head_b is not None:
        if head_a == head_b:
            return head_a
        if head_a in visited:
            return head_a
        if head_b in visited:
            return head_b
        if head_a is not None:
            visited.add(head_a)
            head_a = head_a.next
        if head_b is not None:
            visited.add(head_b)
            head_b = head_b.next
    return None


def linked_list_intersection_space_optimized(head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
    curr_a = head_a
    curr_b = head_b
    while curr_a != curr_b:
        curr_a = curr_a.next if curr_a else head_b
        curr_b = curr_b.next if curr_b else head_a
    return curr_b

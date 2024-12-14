class ListNode:
    def __init__(self, key: int, value: int, prev: "ListNode" = None, next: "ListNode" = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.entries = {}
        self.start = None
        self.end = None

    def get(self, key: int) -> int:
        if key not in self.entries:
            return -1
        else:
            return self.use(key)

    def put(self, key: int, value: int) -> None:
        # update known entry
        if key in self.entries:
            self.entries[key].value = value
            self.use(key)
            return

        # otherwise add new entry
        node = ListNode(key, value)
        self.entries[key] = node

        # edge case: first entry added
        if self.start is None:
            self.start = node
        if self.end is None:
            self.end = node

        # mark new entry as recently used
        self.use(key)

        # remove least recently used if needed
        if len(self.entries) > self.capacity:
            self.entries.pop(self.start.key)
            if self.start.next is not None:
                self.start.next.prev = None
            self.start = self.start.next

    def use(self, key: int) -> int:
        node = self.entries[key]

        # node is already most recent
        if node is self.end:
            return node.value

        # update start and end pointers
        if node is self.start:
            self.start = self.start.next
        if node is self.end:
            self.end = self.end.prev

        # remove node from list
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        # add node to the end
        if self.end is not None:
            self.end.next = node
        node.prev = self.end
        node.next = None

        # mark node as recently used
        self.end = node
        return node.value

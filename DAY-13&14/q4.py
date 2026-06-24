from typing import Any

# Node class - defined in q1.py
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_end(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self._size += 1
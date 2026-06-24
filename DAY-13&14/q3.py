from typing import Any

# Node class - defined in q1.py
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_beginning(self, data: Any) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1
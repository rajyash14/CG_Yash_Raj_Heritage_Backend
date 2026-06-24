from typing import Optional

# Node class - defined in q1.py
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self._size: int = 0
from typing import Any

# Node class - defined in q1.py
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_position(self, data: Any, position: int) -> None:
        if position < 0 or position > self._size:
            raise IndexError(f'Position {position} out of range')
        
        if position == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            if current is not None:
                current = current.next
                
        if current is not None:
            new_node.next = current.next
            current.next = new_node
            self._size += 1
from typing import Optional

# Node class - defined in q1.py
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(self) -> None:
        prev: Optional[Node] = None
        current = self.head
        
        while current is not None:
            next_node = current.next   
            current.next = prev        
            prev = current             
            current = next_node        
            
        self.head = prev               
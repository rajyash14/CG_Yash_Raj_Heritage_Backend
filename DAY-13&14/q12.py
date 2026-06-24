from typing import Optional

# BSTNode class - defined in q11.py
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Optional[BSTNode] = None
        self._size: int = 0
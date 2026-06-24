from typing import Optional, Any

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

    def insert(self, data: Any) -> None:
        self.root = self._insert_recursive(self.root, data)

    def _insert_recursive(self, node: Optional[BSTNode], data: Any) -> BSTNode:
        if node is None:
            self._size += 1
            return BSTNode(data)

        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        elif data > node.data:
            node.right = self._insert_recursive(node.right, data)
        return node

    def search(self, data: Any) -> bool:
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node: Optional[BSTNode], data: Any) -> bool:
        if node is None: 
            return False
        if node.data == data: 
            return True
        if data < node.data:
            return self._search_recursive(node.left, data)
        return self._search_recursive(node.right, data)
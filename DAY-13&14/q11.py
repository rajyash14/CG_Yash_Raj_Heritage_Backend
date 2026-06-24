from typing import Any, Optional

class BSTNode:
    """A single node in the Binary Search Tree."""
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.left: Optional['BSTNode'] = None
        self.right: Optional['BSTNode'] = None

    def __repr__(self) -> str:
        return f'BSTNode({self.data})'
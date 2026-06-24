from typing import List, Any
from collections import deque

def level_order(self) -> List[Any]:
        if not self.root: 
            return []
        result: List[Any] = []
        queue: deque = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.data)
            if node.left:  
                queue.append(node.left)
            if node.right: 
                queue.append(node.right)
        return result
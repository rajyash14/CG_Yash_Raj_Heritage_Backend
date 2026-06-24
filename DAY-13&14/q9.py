from typing import List

def traverse(self) -> None:
        elements: List[str] = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print(' → '.join(elements) + ' → None')
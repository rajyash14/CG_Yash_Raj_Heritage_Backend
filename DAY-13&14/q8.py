from typing import Any

def search(self, value: Any) -> int:
        """Returns the index of the value, or -1 if not found."""
        current = self.head
        index = 0
        while current is not None:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1
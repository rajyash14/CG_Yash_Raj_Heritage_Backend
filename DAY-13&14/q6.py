from typing import Any

def delete_by_value(self, value: Any) -> None:
        if self.head is None:
            raise ValueError('Cannot delete from an empty list')
            
        if self.head.data == value:
            self.head = self.head.next
            self._size -= 1
            return
            
        current = self.head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                self._size -= 1
                return
            current = current.next
            
        raise ValueError(f'{value} not found in list')
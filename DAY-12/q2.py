#Stack Operations (Push, Pop, Peekk)
class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __repr__(self):
        if self.is_empty():
            return "Stack: [EMPTY]"
        return f"Stack [bottom→top]: {self._data}"


book_stack = Stack()

book_stack.push("Python Basics")
book_stack.push("Data Structures")
book_stack.push("Algorithms")
book_stack.push("System Design")
book_stack.push("Clean Code")

print(f'Peeking: {book_stack.peek()}')

print(f'\n--- Removing books one by one (LIFO) ---')
removed = book_stack.pop()
print(f'Removed: {removed:<20} | Stack size: {book_stack.size()}')

removed = book_stack.pop()
print(f'Removed: {removed:<20} | Stack size: {book_stack.size()}')

removed = book_stack.pop()
print(f'Removed: {removed:<20} | Stack size: {book_stack.size()}')

print(f'\nRemaining: {book_stack}')
print(f'Is empty? {book_stack.is_empty()}')

book_stack.pop()
book_stack.pop()

print(f'\nNow is empty? {book_stack.is_empty()}')

try:
    book_stack.pop()
except IndexError as e:
    print(f'Error caught: {e}')
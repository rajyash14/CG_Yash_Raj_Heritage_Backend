from collections import deque

def check_brackets(a):
    b = []
    c = {")": "(", "}": "{", "]": "["}
    for d in a:
        if d in c.values():
            b.append(d)
        elif d in c.keys():
            if not b or b.pop() != c[d]:
                return False
    return not b

print(check_brackets("()"))
print(check_brackets("()[]{}"))
print(check_brackets("(]"))
print(check_brackets("([)]"))
print(check_brackets("{[]}"))

a = deque()

a.append("Customer 1")
print(f"Queue: {list(a)}")
a.append("Customer 2")
print(f"Queue: {list(a)}")
a.append("Customer 3")
print(f"Queue: {list(a)}")

b = a.popleft()
print(f"Served: {b}, Queue: {list(a)}")
b = a.popleft()
print(f"Served: {b}, Queue: {list(a)}")
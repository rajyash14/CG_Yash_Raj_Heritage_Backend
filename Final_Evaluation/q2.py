# Linear Search Time Complexity: O(n)
def linear_search(a, b):
    for c in range(len(a)):
        if a[c] == b:
            return c
    return -1

# Binary Search Time Complexity: O(log n)
# Why binary search requires a sorted array: 
# It works by checking the middle element and eliminating half of the list. 
# It checks that everything to the left is smaller 
# and everything to the right is larger. If the list is unsorted, it might 
# accidentally throw away the half that actually contains the target number.
def binary_search(a, b):
    c = 0
    d = len(a) - 1
    while c <= d:
        e = (c + d) // 2
        if a[e] == b:
            return e
        elif a[e] < b:
            c = e + 1
        else:
            d = e - 1
    return -1

a = [4, 2, 7, 1, 9, 3, 6, 8, 5, 0]
b = 6

c = linear_search(a, b)
print(f"Linear Search found {b} at index {c}")

d = sorted(a)
e = binary_search(d, b)
print(f"Binary Search found {b} at index {e}")
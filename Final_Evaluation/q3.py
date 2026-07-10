# Bubble Sort Complexity -> Best: O(n), Average: O(n^2), Worst: O(n^2)
def bubble_sort(a):
    b = a[:]
    for c in range(len(b)):
        for d in range(0, len(b)-c-1):
            if b[d] > b[d+1]:
                b[d], b[d+1] = b[d+1], b[d]
        print(f"Bubble step: {b}")
    return b

# Selection Sort Complexity -> Best: O(n^2), Average: O(n^2), Worst: O(n^2)
def selection_sort(a):
    b = a[:]
    for c in range(len(b)):
        d = c
        for e in range(c+1, len(b)):
            if b[e] < b[d]:
                d = e
        b[c], b[d] = b[d], b[c]
        print(f"Selection step: {b}")
    return b

# Insertion Sort Complexity -> Best: O(n), Average: O(n^2), Worst: O(n^2)
def insertion_sort(a):
    b = a[:]
    for c in range(1, len(b)):
        d = b[c]
        e = c - 1
        while e >= 0 and d < b[e]:
            b[e + 1] = b[e]
            e -= 1
        b[e + 1] = d
        print(f"Insertion step: {b}")
    return b

# Merge Sort Complexity -> Best: O(n log n), Average: O(n log n), Worst: O(n log n)
def merge_sort(a):
    if len(a) > 1:
        b = len(a) // 2
        c = a[:b]
        d = a[b:]

        merge_sort(c)
        merge_sort(d)

        e = f = g = 0
        while e < len(c) and f < len(d):
            if c[e] < d[f]:
                a[g] = c[e]
                e += 1
            else:
                a[g] = d[f]
                f += 1
            g += 1

        while e < len(c):
            a[g] = c[e]
            e += 1
            g += 1

        while f < len(d):
            a[g] = d[f]
            f += 1
            g += 1
        print(f"Merge step: {a}")
    return a

# Quick Sort Complexity -> Best: O(n log n), Average: O(n log n), Worst: O(n^2)
def quick_sort(a):
    if len(a) <= 1:
        return a
    b = a[len(a) // 2]
    c = [x for x in a if x < b]
    d = [x for x in a if x == b]
    e = [x for x in a if x > b]
    f = quick_sort(c) + d + quick_sort(e)
    print(f"Quick step: {f}")
    return f

a = [64, 34, 25, 12, 22, 11, 90, 45]

print("Bubble:")
bubble_sort(a)
print("Selection:")
selection_sort(a)
print("Insertion:")
insertion_sort(a)
print("Merge:")
b = a[:]
merge_sort(b)
print("Quick:")
quick_sort(a)
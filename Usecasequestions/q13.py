class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder_list(root, result):
    if root != None:
        inorder_list(root.left, result)
        result.append(root.val)
        inorder_list(root.right, result)

def kth_smallest(root, k):
    result = []
    inorder_list(root, result)
    return result[k - 1]

root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(2)
root.left.right = Node(4)
root.left.left.left = Node(1)

print(kth_smallest(root, 3))
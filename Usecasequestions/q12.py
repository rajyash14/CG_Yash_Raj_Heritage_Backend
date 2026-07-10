class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def array_to_bst(arr):
    if len(arr) == 0:
        return None
    
    mid = len(arr) // 2
    root = Node(arr[mid])
    
    root.left = array_to_bst(arr[:mid])
    root.right = array_to_bst(arr[mid+1:])
    
    return root

def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

arr = [1, 2, 3, 4, 5, 6, 7]
bst_root = array_to_bst(arr)
inorder(bst_root)
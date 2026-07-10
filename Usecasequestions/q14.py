class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, val):
        if root == None:
            return Node(val)
        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        return root

    def search(self, root, val):
        if root == None or root.val == val:
            return root
        if val < root.val:
            return self.search(root.left, val)
        return self.search(root.right, val)

    def find_min(self, root):
        current = root
        while current.left != None:
            current = current.left
        return current

    def delete(self, root, val):
        if root == None:
            return root
        if val < root.val:
            root.left = self.delete(root.left, val)
        elif val > root.val:
            root.right = self.delete(root.right, val)
        else:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            temp = self.find_min(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)
        return root

    def display(self, root):
        if root != None:
            self.display(root.left)
            print(root.val, end=" ")
            self.display(root.right)

tree = BST()
root = None
root = tree.insert(root, 50)
root = tree.insert(root, 30)
root = tree.insert(root, 20)
root = tree.insert(root, 40)
root = tree.insert(root, 70)

tree.display(root)
print()

if tree.search(root, 40):
    print("Found 40")

root = tree.delete(root, 30)
tree.display(root)